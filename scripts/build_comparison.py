#!/usr/bin/env python3
"""Bundle existing local proofs into an offline A/B board; never judge quality.

Python 3.9+, standard library only. Inputs are explicitly supplied local files.
The output directory must be new. No rendering, network access, or model calls.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import shutil
import sys
from pathlib import Path
from typing import Any

MEDIA = {
    ".png": ("image", "image/png"), ".jpg": ("image", "image/jpeg"),
    ".jpeg": ("image", "image/jpeg"), ".webp": ("image", "image/webp"),
    ".gif": ("image", "image/gif"), ".mp4": ("video", "video/mp4"),
    ".webm": ("video", "video/webm"),
}
AXES = ("fit", "coherence", "hierarchy", "distinctiveness", "legibility", "interaction", "craft")


def text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()


def local_media(value: Any, base: Path) -> Path:
    raw = text(value, "media path")
    if "://" in raw:
        raise ValueError("Use a local captured file, not a URL")
    path = Path(raw).expanduser()
    path = (base / path).resolve() if not path.is_absolute() else path.resolve()
    if path.suffix.lower() not in MEDIA:
        raise ValueError(f"Unsupported media extension: {path.suffix}")
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError(f"Missing or empty media: {path}")
    # Check the container signature, not pixel validity or successful playback.
    with path.open("rb") as handle:
        header = handle.read(16)
    ext = path.suffix.lower()
    signatures = {
        ".png": header.startswith(b"\x89PNG\r\n\x1a\n"),
        ".jpg": header.startswith(b"\xff\xd8\xff"),
        ".jpeg": header.startswith(b"\xff\xd8\xff"),
        ".gif": header.startswith((b"GIF87a", b"GIF89a")),
        ".webp": header[:4] == b"RIFF" and header[8:12] == b"WEBP",
        ".mp4": header[4:8] == b"ftyp",
        ".webm": header.startswith(b"\x1a\x45\xdf\xa3"),
    }
    if not signatures[ext]:
        raise ValueError(f"Unexpected media signature: {path}")
    return path


def snapshot(source: Path, output: Path, name: str) -> dict[str, Any]:
    relative = Path("media") / f"{name}{source.suffix.lower()}"
    destination = output / relative
    digest = hashlib.sha256()
    size = 0
    with source.open("rb") as src, destination.open("xb") as dst:
        for chunk in iter(lambda: src.read(1024 * 1024), b""):
            dst.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    if not size:
        raise ValueError(f"Media became empty during copy: {source}")
    kind, mime = MEDIA[source.suffix.lower()]
    return {"source": str(source), "path": relative.as_posix(), "sha256": digest.hexdigest(),
            "bytes": size, "kind": kind, "mime": mime}


def media_tag(item: dict[str, Any], label: str) -> str:
    src, alt = html.escape(item["path"], quote=True), html.escape(label, quote=True)
    if item["kind"] == "video":
        return f'<video controls playsinline preload="metadata" aria-label="{alt}"><source src="{src}" type="{item["mime"]}"></video>'
    return f'<img src="{src}" alt="{alt}" loading="lazy">'


def render_board(manifest: dict[str, Any]) -> str:
    sections = []
    for view in manifest["views"]:
        cards = "".join(
            f'<figure><figcaption>{side.upper()}</figcaption>{media_tag(view[side], side.upper())}'
            f'<a href="{html.escape(view[side]["path"], quote=True)}">Open original {side.upper()}</a></figure>'
            for side in ("a", "b")
        )
        sections.append(f'<section><h2>{html.escape(view["id"])}</h2><p>{html.escape(view["condition"])}</p><div class="pair">{cards}</div></section>')
    refs = "".join(f'<figure>{media_tag(ref, "Reference")}<figcaption>{html.escape(ref["note"])}</figcaption></figure>' for ref in manifest["references"])
    return """<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Visual comparison</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f3ef;color:#202020;font:16px/1.6 system-ui,sans-serif}
main{max-width:1600px;margin:auto;padding:32px}h1{font-size:clamp(24px,3vw,42px);line-height:1.2}
h2{font-size:20px}section{padding:20px 0;border-top:1px solid #bbb}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start}
figure{margin:0;min-width:0;background:white;padding:12px}figcaption{font-weight:650;margin:0 0 8px}
img,video{display:block;width:100%;height:auto;object-fit:contain;background:#e8e8e8}a{display:inline-block;margin-top:8px;color:#174e80}
a:focus-visible,summary:focus-visible{outline:3px solid #174e80;outline-offset:4px}
.notice{border-left:3px solid #777;padding:8px 16px}details{margin:24px 0}summary{cursor:pointer}
.refs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin-top:16px}
@media(max-width:720px){main{padding:16px}.pair{grid-template-columns:1fr}}
</style><main><p>VISUAL FEEDBACK / REVIEW PENDING</p>""" + (
        f'<h1>{html.escape(manifest["question"])}</h1><p>{html.escape(manifest["context"])}</p>'
        '<p class="notice">Describe A and B before opening references. Labels are not verified blinding. '
        'View originals at intended size; this page rescales previews. Play clips one at a time with sound, then muted. '
        'The builder does not inspect pixels, synchronize video, test interactions, or select a winner.</p>'
        + "".join(sections)
        + f'<details><summary>References — open after the first-view read</summary><div class="refs">{refs or "No visual reference supplied."}</div></details>'
        '<p>Record A / B / tie / neither / insufficient_evidence in review.json. '
        'A newer artifact is not automatically better. Keep the prior baseline until the comparison supports a change.</p>'
        '<p><a href="review.json">Review template</a> · <a href="manifest.json">Snapshot manifest</a></p></main></html>'
    )


def build(spec_path: Path, output: Path) -> dict[str, Any]:
    spec_path = spec_path.resolve()
    with spec_path.open(encoding="utf-8") as handle:
        spec = json.load(handle)
    if not isinstance(spec, dict):
        raise ValueError("Spec must be a JSON object")
    question = text(spec.get("question"), "question")
    context = text(spec.get("context"), "context")
    versions = {side: text(spec.get(key), key) for side, key in (("a", "baseline_version"), ("b", "candidate_version"))}
    views = spec.get("views")
    if not isinstance(views, list) or not views:
        raise ValueError("views must be a non-empty list")
    normalized, ids = [], set()
    for view in views:
        if not isinstance(view, dict):
            raise ValueError("Each view must be an object")
        identity = text(view.get("id"), "view.id")
        if identity in ids:
            raise ValueError(f"Duplicate view id: {identity}")
        ids.add(identity)
        condition = text(view.get("condition"), "view.condition")
        a, b = (local_media(view.get(side), spec_path.parent) for side in ("a", "b"))
        if MEDIA[a.suffix.lower()][0] != MEDIA[b.suffix.lower()][0]:
            raise ValueError("Paired proofs must both be images or both be videos")
        normalized.append((identity, condition, a, b))
    references = spec.get("references", [])
    if not isinstance(references, list):
        raise ValueError("references must be a list")
    refs = []
    for reference in references:
        if not isinstance(reference, dict):
            raise ValueError("Each reference must be an object")
        refs.append((local_media(reference.get("path"), spec_path.parent), text(reference.get("note"), "reference.note")))
    output = output.resolve()
    # Never overwrite the baseline or a previous comparison directory.
    output.mkdir(parents=True, exist_ok=False)
    try:
        (output / "media").mkdir()
        manifest: dict[str, Any] = {
            "schema_version": 1, "status": "review_pending", "independence": "unverified",
            "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "question": question, "context": context, "declared_versions": versions,
            "observed_by_builder": False, "conditions_verified_by_builder": False,
            "views": [], "references": [],
        }
        for number, (identity, condition, a, b) in enumerate(normalized, 1):
            manifest["views"].append({"id": identity, "condition": condition,
                "a": snapshot(a, output, f"v{number:03d}-a"), "b": snapshot(b, output, f"v{number:03d}-b")})
        for number, (path, note) in enumerate(refs, 1):
            item = snapshot(path, output, f"ref{number:03d}")
            item["note"] = note
            manifest["references"].append(item)
        review = {
            "status": "review_pending", "reviewer_id": "", "independence": "unverified",
            "first_read": {"a": "", "b": ""}, "observations": [], "hard_failures": [],
            "axes": {axis: {"verdict": "not_observed", "evidence": []} for axis in AXES},
            "decision": "insufficient_evidence", "reason": "", "preserve": [], "regressions": [],
            "next_edit": {"hypothesis": "", "changed_variables": [], "expected_visible_delta": "", "rollback_when": ""},
            "human_confirmation": None,
        }
        for name, value in (("manifest.json", manifest), ("input-spec.json", spec)):
            (output / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        review["manifest_sha256"] = hashlib.sha256((output / "manifest.json").read_bytes()).hexdigest()
        (output / "review.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (output / "index.html").write_text(render_board(manifest), encoding="utf-8")
        return manifest
    except Exception:
        shutil.rmtree(output)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", type=Path, required=True, help="JSON; media paths resolve relative to this file")
    parser.add_argument("--out", type=Path, required=True, help="New comparison directory; existing paths are rejected")
    args = parser.parse_args()
    try:
        manifest = build(args.spec, args.out)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"status": manifest["status"], "board": str(args.out.resolve() / "index.html"),
                      "views": len(manifest["views"]), "quality_judged": False}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
