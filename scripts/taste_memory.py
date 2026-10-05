#!/usr/bin/env python3
"""Append-only, confirmed-only storage for creative-taste cases.

The store preserves evidence and enforces state boundaries. It cannot prove that a
human really made an external decision; the confirm command makes that event
explicit instead of allowing a model-generated case to claim confirmation inline.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import tempfile
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set


STATES = {"proposed", "pending_human", "confirmed", "rejected", "stale", "superseded"}
MODEL_IDENTITIES = {"model", "assistant", "agent", "system", "codex"}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def is_iso_timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def read_json(path: str) -> Dict[str, Any]:
    if path == "-":
        value = json.load(sys.stdin)
    else:
        with open(path, "r", encoding="utf-8") as handle:
            value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("JSON input must be an object")
    return value


def store_paths(root: Path) -> Dict[str, Path]:
    return {
        "root": root,
        "cases": root / "cases.jsonl",
        "artifacts": root / "artifacts.jsonl",
        "rules": root / "rules.jsonl",
        "index": root / "index.json",
        "reviews": root / "reviews",
    }


def write_json_atomic(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    if not path.exists():
        return digest.hexdigest()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def init_store(root: Path) -> None:
    paths = store_paths(root)
    paths["root"].mkdir(parents=True, exist_ok=True)
    paths["reviews"].mkdir(parents=True, exist_ok=True)
    for key in ("cases", "artifacts", "rules"):
        paths[key].touch(exist_ok=True)
    if not paths["index"].exists():
        write_json_atomic(
            paths["index"],
            {
                "version": 2,
                "updated_at": now(),
                "case_ids": [],
                "artifact_ids": [],
                "cases_digest": digest_file(paths["cases"]),
                "artifacts_digest": digest_file(paths["artifacts"]),
            },
        )


def iter_jsonl(path: Path, label: str) -> Iterable[Dict[str, Any]]:
    if not path.exists():
        raise ValueError(f"memory_unavailable: missing {label}: {path}")
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at {path}:{line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"record at {path}:{line_number} is not an object")
            yield value


def load_index(root: Path) -> Dict[str, Any]:
    path = store_paths(root)["index"]
    if not path.exists():
        raise ValueError(f"memory_unavailable: missing index: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"memory_unavailable: invalid index: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("memory_unavailable: index is not an object")
    return value


def require_text(value: Any, field: str, errors: List[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")


def validate_artifact(artifact: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for field in ("artifact_id", "version", "source", "tool", "render_receipt", "hash_or_snapshot", "owner"):
        require_text(artifact.get(field), field, errors)
    if not is_iso_timestamp(artifact.get("registered_at")):
        errors.append("registered_at must be an ISO timestamp")
    return errors


def validate_case(case: Dict[str, Any], artifacts: Optional[Dict[str, Dict[str, Any]]] = None) -> List[str]:
    errors: List[str] = []
    state = case.get("state")
    if not isinstance(state, str) or state not in STATES:
        errors.append(f"state must be one of {sorted(STATES)}")
    for field in ("case_id", "created_at", "updated_at", "domain", "intent", "writer", "source_revision"):
        require_text(case.get(field), field, errors)
    for field in ("created_at", "updated_at"):
        if case.get(field) and not is_iso_timestamp(case.get(field)):
            errors.append(f"{field} must be an ISO timestamp")
    evidence = case.get("artifact_evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("artifact_evidence must be a non-empty list")
    else:
        for index, item in enumerate(evidence):
            if not isinstance(item, dict):
                errors.append(f"artifact_evidence[{index}] must be an object")
                continue
            require_text(item.get("locator"), f"artifact_evidence[{index}].locator", errors)
            require_text(item.get("observation"), f"artifact_evidence[{index}].observation", errors)
    if case.get("verdict") is not None and case.get("verdict") not in {
        "accepted",
        "rejected",
        "mixed",
        "accepted_after_revision",
    }:
        errors.append("verdict is invalid")
    if state == "confirmed":
        confirmer = case.get("confirmer_id")
        require_text(confirmer, "confirmer_id", errors)
        if isinstance(confirmer, str) and confirmer.lower() in MODEL_IDENTITIES:
            errors.append("confirmer_id must identify a human or external decision owner")
        if confirmer == case.get("writer"):
            errors.append("confirmer_id must differ from writer")
        event = case.get("confirmation_event")
        if not isinstance(event, dict):
            errors.append("confirmation_event must be a structured event object")
        else:
            for field in ("event_id", "source"):
                require_text(event.get(field), f"confirmation_event.{field}", errors)
            if event.get("source") in {"model", "assistant", "agent", "system"}:
                errors.append("confirmation_event.source cannot be a model identity")
            if event.get("human_asserted") is not True:
                errors.append("confirmation_event.human_asserted must be true")
        if not is_iso_timestamp(case.get("confirmed_at")):
            errors.append("confirmed_at must be an ISO timestamp")
        artifact_id = case.get("accepted_artifact_id")
        require_text(artifact_id, "accepted_artifact_id", errors)
        if artifacts is not None and artifact_id not in artifacts:
            errors.append("accepted_artifact_id is not registered in artifacts.jsonl")
        artifact_version = case.get("accepted_artifact_version")
        require_text(artifact_version, "accepted_artifact_version", errors)
        if artifacts is not None and artifact_id in artifacts and artifact_version != artifacts[artifact_id].get("version"):
            errors.append("accepted_artifact_version does not match registered artifact")
        if case.get("verdict") not in {"accepted", "rejected", "mixed", "accepted_after_revision"}:
            errors.append("confirmed case requires a valid verdict")
        require_text(case.get("scope"), "scope", errors)
        review = case.get("review")
        if not isinstance(review, dict):
            errors.append("confirmed case missing review receipt")
        else:
            for field in ("reviewer_id", "reviewer_role", "receipt"):
                require_text(review.get(field), f"review.{field}", errors)
            if review.get("reviewer_id") == case.get("writer"):
                errors.append("reviewer_id must differ from writer")
            if review.get("blind_to_history") is not True:
                errors.append("review.blind_to_history must be true")
            locators = review.get("evidence_locators")
            if not isinstance(locators, list) or not locators:
                errors.append("review.evidence_locators must be a non-empty list")
    return errors


def read_records(root: Path) -> tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    paths = store_paths(root)
    cases = list(iter_jsonl(paths["cases"], "cases.jsonl"))
    artifacts_list = list(iter_jsonl(paths["artifacts"], "artifacts.jsonl"))
    artifacts: Dict[str, Dict[str, Any]] = {}
    for artifact in artifacts_list:
        artifact_id = artifact.get("artifact_id")
        if artifact_id in artifacts:
            raise ValueError(f"duplicate artifact_id: {artifact_id}")
        artifact_errors = validate_artifact(artifact)
        if artifact_errors:
            raise ValueError(f"artifact {artifact_id}: {'; '.join(artifact_errors)}")
        artifacts[artifact_id] = artifact
    return cases, artifacts


def validate_store(root: Path) -> List[str]:
    if not root.exists() or not root.is_dir():
        return [f"memory_unavailable: root does not exist: {root}"]
    errors: List[str] = []
    try:
        index = load_index(root)
        cases, artifacts = read_records(root)
        case_ids: Set[str] = set()
        for case in cases:
            case_id = case.get("case_id")
            if case_id in case_ids:
                errors.append(f"duplicate case_id: {case_id}")
            case_ids.add(case_id)
            errors.extend(f"{case_id}: {error}" for error in validate_case(case, artifacts))
        artifact_ids = set(artifacts)
        if sorted(index.get("case_ids", [])) != sorted(case_ids):
            errors.append("index case_ids do not match cases.jsonl")
        if sorted(index.get("artifact_ids", [])) != sorted(artifact_ids):
            errors.append("index artifact_ids do not match artifacts.jsonl")
        if index.get("cases_digest") != digest_file(store_paths(root)["cases"]):
            errors.append("index cases_digest does not match cases.jsonl")
        if index.get("artifacts_digest") != digest_file(store_paths(root)["artifacts"]):
            errors.append("index artifacts_digest does not match artifacts.jsonl")
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    return errors


def append_jsonl(root: Path, key: str, record: Dict[str, Any]) -> None:
    path = store_paths(root)[key]
    serialized = json.dumps(record, ensure_ascii=False, sort_keys=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(serialized + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def refresh_index(root: Path) -> None:
    paths = store_paths(root)
    cases, artifacts = read_records(root)
    write_json_atomic(
        paths["index"],
        {
            "version": 2,
            "updated_at": now(),
            "case_ids": sorted(case.get("case_id") for case in cases),
            "artifact_ids": sorted(artifacts),
            "cases_digest": digest_file(paths["cases"]),
            "artifacts_digest": digest_file(paths["artifacts"]),
        },
    )


def append_artifact(root: Path, artifact: Dict[str, Any]) -> Dict[str, Any]:
    init_store(root)
    artifact = dict(artifact)
    artifact.setdefault("registered_at", now())
    errors = validate_artifact(artifact)
    if errors:
        raise ValueError("; ".join(errors))
    current_errors = validate_store(root)
    if current_errors:
        raise ValueError("store is not valid: " + "; ".join(current_errors))
    _, artifacts = read_records(root)
    if artifact["artifact_id"] in artifacts:
        raise ValueError(f"artifact_id already exists: {artifact['artifact_id']}")
    append_jsonl(root, "artifacts", artifact)
    refresh_index(root)
    return artifact


def append_case(root: Path, case: Dict[str, Any]) -> Dict[str, Any]:
    init_store(root)
    case = dict(case)
    timestamp = now()
    case.setdefault("case_id", f"case-{uuid.uuid4().hex}")
    case.setdefault("state", "pending_human")
    case.setdefault("created_at", timestamp)
    case.setdefault("updated_at", timestamp)
    case.setdefault("writer", "creative-taste-orchestrator")
    if case.get("state") == "confirmed":
        raise ValueError("confirmed cases must use the confirm command with a structured human event")
    current_errors = validate_store(root)
    if current_errors:
        raise ValueError("store is not valid: " + "; ".join(current_errors))
    cases, artifacts = read_records(root)
    if case["case_id"] in {item.get("case_id") for item in cases}:
        raise ValueError(f"case_id already exists: {case['case_id']}")
    errors = validate_case(case, artifacts)
    if errors:
        raise ValueError("; ".join(errors))
    append_jsonl(root, "cases", case)
    refresh_index(root)
    return case


def confirm_case(root: Path, case_id: str, confirmer_id: str, event_id: str, source: str, artifact_id: str) -> Dict[str, Any]:
    init_store(root)
    current_errors = validate_store(root)
    if current_errors:
        raise ValueError("store is not valid: " + "; ".join(current_errors))
    cases, artifacts = read_records(root)
    source_case = next((case for case in cases if case.get("case_id") == case_id), None)
    if source_case is None:
        raise ValueError(f"case not found: {case_id}")
    if source_case.get("state") in {"confirmed", "superseded"}:
        raise ValueError("case is already confirmed or superseded")
    if artifact_id not in artifacts:
        raise ValueError(f"artifact_id is not registered: {artifact_id}")
    confirmed = dict(source_case)
    confirmed["case_id"] = f"case-{uuid.uuid4().hex}"
    confirmed["state"] = "confirmed"
    confirmed["updated_at"] = now()
    confirmed["confirmed_at"] = now()
    confirmed["confirmer_id"] = confirmer_id
    confirmed["confirmation_event"] = {"event_id": event_id, "source": source, "human_asserted": True}
    confirmed["accepted_artifact_id"] = artifact_id
    confirmed["accepted_artifact_version"] = artifacts[artifact_id]["version"]
    confirmed["supersedes"] = [case_id]
    review = confirmed.get("review")
    if not isinstance(review, dict):
        raise ValueError("source case must contain a review receipt before confirmation")
    errors = validate_case(confirmed, artifacts)
    if errors:
        raise ValueError("; ".join(errors))
    append_jsonl(root, "cases", confirmed)
    refresh_index(root)
    return confirmed


def searchable_text(case: Dict[str, Any]) -> str:
    return json.dumps(case, ensure_ascii=False, sort_keys=True).lower()


def search_cases(root: Path, query: str, domain: Optional[str], states: Set[str]) -> List[Dict[str, Any]]:
    errors = validate_store(root)
    if errors:
        raise ValueError("memory_unavailable: " + "; ".join(errors))
    cases, _ = read_records(root)
    terms = [term for term in query.lower().split() if term]
    results = []
    for case in cases:
        if case.get("state") not in states:
            continue
        if domain and case.get("domain") != domain:
            continue
        haystack = searchable_text(case)
        if all(term in haystack for term in terms):
            results.append(case)
    audit = {
        "retrieval_id": f"retrieval-{uuid.uuid4().hex}",
        "queried_at": now(),
        "query": query,
        "domain": domain,
        "states": sorted(states),
        "result_case_ids": [case.get("case_id") for case in results],
    }
    write_json_atomic(store_paths(root)["reviews"] / f"{audit['retrieval_id']}.json", audit)
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create an empty memory store")
    init_parser.add_argument("--root", required=True, type=Path)

    artifact_parser = subparsers.add_parser("register-artifact", help="register an inspected artifact")
    artifact_parser.add_argument("--root", required=True, type=Path)
    artifact_parser.add_argument("--artifact", required=True, help="JSON file path, or - for stdin")

    add_parser = subparsers.add_parser("add", help="append a proposed or pending case")
    add_parser.add_argument("--root", required=True, type=Path)
    add_parser.add_argument("--case", required=True, help="JSON file path, or - for stdin")

    confirm_parser = subparsers.add_parser("confirm", help="append a confirmed revision through an explicit event")
    confirm_parser.add_argument("--root", required=True, type=Path)
    confirm_parser.add_argument("--case-id", required=True)
    confirm_parser.add_argument("--confirmer-id", required=True)
    confirm_parser.add_argument("--event-id", required=True)
    confirm_parser.add_argument("--source", required=True, choices=("user_message", "approval_record", "project_decision"))
    confirm_parser.add_argument("--artifact-id", required=True)

    search_parser = subparsers.add_parser("search", help="search validated retrievable cases")
    search_parser.add_argument("--root", required=True, type=Path)
    search_parser.add_argument("--query", default="")
    search_parser.add_argument("--domain")
    search_parser.add_argument("--states", default="confirmed", help="comma-separated states")

    validate_parser = subparsers.add_parser("validate", help="validate the append-only store")
    validate_parser.add_argument("--root", required=True, type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "init":
            init_store(args.root)
            print(json.dumps({"status": "initialized", "root": str(args.root)}, ensure_ascii=False))
            return 0
        if args.command == "register-artifact":
            artifact = append_artifact(args.root, read_json(args.artifact))
            print(json.dumps({"status": "registered", "artifact": artifact}, ensure_ascii=False, indent=2))
            return 0
        if args.command == "add":
            case = append_case(args.root, read_json(args.case))
            print(json.dumps({"status": "appended", "case": case}, ensure_ascii=False, indent=2))
            return 0
        if args.command == "confirm":
            case = confirm_case(args.root, args.case_id, args.confirmer_id, args.event_id, args.source, args.artifact_id)
            print(json.dumps({"status": "confirmed", "case": case}, ensure_ascii=False, indent=2))
            return 0
        if args.command == "search":
            requested = {item.strip() for item in args.states.split(",") if item.strip()}
            invalid = requested - STATES
            if invalid:
                raise ValueError(f"invalid states: {sorted(invalid)}")
            results = search_cases(args.root, args.query, args.domain, requested)
            print(json.dumps(results, ensure_ascii=False, indent=2))
            return 0
        if args.command == "validate":
            errors = validate_store(args.root)
            print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
