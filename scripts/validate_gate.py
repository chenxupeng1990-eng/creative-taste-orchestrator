#!/usr/bin/env python3
"""Fail-closed validation for a creative production/review status record."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List


BLOCKING_STATES = {"blocked", "review_unverified", "memory_pending", "unverified"}
ALLOWED_STATUSES = {
    "draft", "blocked", "proposed", "rendered", "review_pending",
    "revision_required", "accepted_technical", "accepted_creative",
    "memory_pending", "confirmed", "rejected", "review_unverified",
}


def read_record(path: str) -> Dict[str, Any]:
    if path == "-":
        value = json.load(sys.stdin)
    else:
        with open(path, "r", encoding="utf-8") as handle:
            value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("gate record must be a JSON object")
    return value


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(record: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    status = record.get("status")
    independence = record.get("independence")
    if status not in ALLOWED_STATUSES:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUSES)}")
    if status in {"accepted_creative", "confirmed"} and independence != "independent":
        errors.append("creative acceptance requires independence=independent")
    if independence in {"simulated", "unverified"}:
        errors.append("simulated or unverified independence cannot pass a creative gate")
    if status in {"accepted_creative", "confirmed"}:
        manifest = record.get("artifact_manifest")
        if not isinstance(manifest, dict):
            errors.append("creative acceptance requires an artifact_manifest object")
        else:
            for field in ("artifact_id", "version", "source", "tool", "render_receipt", "hash_or_snapshot"):
                if not nonempty(manifest.get(field)) or manifest.get(field) == "unavailable":
                    errors.append(f"artifact_manifest.{field} must be present and verified")
            coverage = manifest.get("viewports_or_states") or manifest.get("timecode_or_coverage")
            if not isinstance(coverage, list) or not coverage:
                errors.append("artifact_manifest needs non-empty coverage evidence")
            source = manifest.get("source")
            if isinstance(source, str) and source.startswith("/") and not os.path.exists(source):
                errors.append(f"artifact_manifest.source does not exist: {source}")
        if not nonempty(record.get("producer_id")):
            errors.append("creative acceptance requires producer_id")
        review = record.get("review_receipt")
        if not isinstance(review, dict):
            errors.append("creative acceptance requires a review_receipt object")
        else:
            for field in ("reviewer_id", "reviewer_role", "observed_at"):
                if not nonempty(review.get(field)):
                    errors.append(f"review_receipt.{field} is required")
            if review.get("blind_to_history") is not True:
                errors.append("review_receipt.blind_to_history must be true")
            locators = review.get("evidence_locators")
            if not isinstance(locators, list) or not locators or not all(nonempty(item) for item in locators):
                errors.append("review_receipt.evidence_locators must contain locators")
            if review.get("reviewer_id") == record.get("producer_id"):
                errors.append("producer cannot be the independent reviewer")
        for field in ("hard_gates_unresolved", "fatal_objections_unresolved"):
            value = record.get(field, [])
            if not isinstance(value, list) or value:
                errors.append(f"{field} must be an empty list before creative acceptance")
    for field in BLOCKING_STATES:
        if record.get("status") == field:
            errors.append(f"status={field} is not an accepted state")
    if status == "confirmed":
        memory = record.get("memory_receipt")
        if not isinstance(memory, dict) or memory.get("state") != "confirmed":
            errors.append("confirmed status requires memory_receipt.state=confirmed")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, help="JSON record path, or - for stdin")
    args = parser.parse_args()
    try:
        record = read_record(args.record)
        errors = validate(record)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
