#!/usr/bin/env python3
"""Apply an inspected A/B decision to a local working baseline, never publication.

Single-writer CLI. Checks snapshot bytes and stale baselines; trusts the stated
review, not reviewer identity or taste. All state is replaced atomically once.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

DECISIONS = {'A', 'B', 'tie', 'neither', 'insufficient_evidence'}


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError(f'Expected JSON object: {path}')
    return value


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def atomic_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.' + path.name)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(value, f, ensure_ascii=False, indent=2)
            f.write('\n'); f.flush(); os.fsync(f.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary): os.unlink(temporary)


def verify_snapshot(root: Path, item: dict) -> dict:
    if not isinstance(item, dict) or not isinstance(item.get('path'), str):
        raise ValueError('Invalid snapshot record')
    path = (root / item['path']).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f'Missing or out-of-bundle snapshot: {path}')
    if path.stat().st_size != item.get('bytes') or sha(path) != item.get('sha256'):
        raise ValueError(f'Snapshot changed: {path}')
    return {'path': str(path), 'sha256': item['sha256'], 'bytes': item['bytes']}


def apply(bundle: Path, state_path: Path) -> dict:
    bundle, state_path = bundle.resolve(), state_path.resolve()
    manifest_path, review_path = bundle / 'manifest.json', bundle / 'review.json'
    manifest, review = load(manifest_path), load(review_path)
    manifest_hash, review_hash = sha(manifest_path), sha(review_path)
    if review.get('manifest_sha256') != manifest_hash:
        raise ValueError('Review is not bound to this manifest; use its actual SHA-256')
    decision = review.get('decision')
    if not isinstance(decision, str) or decision not in DECISIONS:
        raise ValueError('Invalid decision')
    for field in ('reviewer_id', 'reason'):
        if not isinstance(review.get(field), str) or not review[field].strip():
            raise ValueError(f'{field} is required')
    if review.get('status') not in {'reviewed', 'revision_required'}:
        raise ValueError('Pending or unrecognized review cannot be applied')
    if not isinstance(review.get('hard_failures'), list):
        raise ValueError('hard_failures must be a list')
    # Revisions needed or unresolved hard failures never promote an option.
    if decision in {'A', 'B', 'tie'} and (review['hard_failures'] or review['status'] != 'reviewed'):
        raise ValueError('Unresolved hard failures/revisions prevent selection')
    versions, views = manifest.get('declared_versions', {}), manifest.get('views')
    if not isinstance(views, list) or not views:
        raise ValueError('No comparison views')
    candidates = {'a': {}, 'b': {}}
    for view in views:
        identity = view.get('id')
        if not isinstance(identity, str) or not identity or identity in candidates['a']:
            raise ValueError('Invalid or duplicate view ID')
        for side in candidates:
            if not isinstance(versions.get(side), str) or not versions[side]:
                raise ValueError('Missing declared version')
            candidates[side][identity] = verify_snapshot(bundle, view.get(side))
    for item in manifest.get('references', []): verify_snapshot(bundle, item)
    # Locators name actual views on both sides; the text still requires a viewer.
    if decision in {'A', 'B', 'tie'}:
        observations = review.get('observations', [])
        for side in ('A', 'B'):
            if not isinstance(observations, list) or not any(
                isinstance(o, dict) and o.get('side') == side and o.get('view_id') in candidates['a']
                and isinstance(o.get('observation'), str) and o['observation'].strip() for o in observations
            ):
                raise ValueError(f'Missing located observation for {side}')
    state = load(state_path) if state_path.exists() else {'schema_version': 1, 'baseline': None, 'history': []}
    history = state.get('history')
    if not isinstance(history, list): raise ValueError('Invalid working state')
    for event in history:
        if event['manifest_sha256'] == manifest_hash:
            if event['review_sha256'] != review_hash:
                raise ValueError('Decision already applied; make a new comparison to revise it')
            return state  # idempotent retry, including after a newer comparison
    baseline = state.get('baseline')
    if baseline:
        if baseline['version'] != versions['a']:
            raise ValueError('Stale baseline version; compare against the current working baseline')
        for view_id, old in baseline['views'].items():
            if view_id not in candidates['a'] or candidates['a'][view_id]['sha256'] != old['sha256']:
                raise ValueError('Baseline coverage/bytes changed; recapture as a new candidate, not A')
    side = 'b' if decision == 'B' else 'a'
    if decision in {'A', 'B', 'tie'}:
        state['baseline'] = {'version': versions[side], 'views': candidates[side], 'bundle': str(bundle)}
        state['status'] = 'working_selected'
    else:
        state['status'] = 'revision_required' if decision == 'neither' else 'review_pending'
    state['next_edit'] = review.get('next_edit', {})
    history.append({'manifest_sha256': manifest_hash, 'review_sha256': review_hash,
                    'decision': decision, 'reviewer_id': review['reviewer_id'], 'reason': review['reason'],
                    'independence': review.get('independence', 'unverified')})
    atomic_write(state_path, state)
    return state


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bundle', type=Path, required=True)
    p.add_argument('--state', type=Path, required=True)
    args = p.parse_args()
    try:
        state = apply(args.bundle, args.state)
        print(json.dumps({'status': state['status'], 'baseline': state['baseline'],
                          'human_confirmation': False, 'publication_authorized': False}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'error: {exc}', file=sys.stderr); return 2

if __name__ == '__main__': raise SystemExit(main())
