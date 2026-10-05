# Apply an actual review

The minimal loop is capture -> bundle -> inspect -> decide -> apply -> read working state -> implement. No model runner, taste-score service, or extra committee is introduced.

The builder writes `manifest.json` and a pending `review.json` bound by `manifest_sha256`. After actually viewing the proofs, fill the reviewer, reason, observations, hard failures, decision, and next edit. Use `status: reviewed` for an actionable selection. A rejection can use `revision_required`.

```json
{
  "manifest_sha256": "actual SHA-256 of manifest.json",
  "status": "reviewed",
  "reviewer_id": "actual reviewer or self-review",
  "independence": "unverified",
  "decision": "B",
  "reason": "The product reads before supporting text without losing the CTA",
  "hard_failures": [],
  "observations": [
    {"side":"A","view_id":"desktop","observation":"Title and bottle have equal weight"},
    {"side":"B","view_id":"desktop","observation":"The bottle anchors the right field; the title remains readable"}
  ],
  "next_edit": {"hypothesis":"Check that the crop survives mobile"}
}
```

```sh
python scripts/apply_review.py --bundle /project/comparison-r01 --state /project/working-state.json
```

A/B/tie select a working proof, never publication. Neither leaves the last-good baseline untouched and marks revision required. Insufficient evidence stays pending. Snapshot hashes and sizes are recomputed. A changed applied decision needs a fresh comparison; retries of the same decision are idempotent. Revisions must carry forward the previous baseline version and captured views; expand coverage with matching A views, not by silently replacing them.

The scripts trust the review's declared observations. They cannot authenticate a human, certify originality, ensure equal fidelity, or resist an agent that rewrites both manifest and review. Use actual host permission boundaries for those concerns. Single-writer execution is required. All working state is saved by one atomic replacement; an interrupted replace preserves the previous state.

## Memory distinction

Working selection is not human taste confirmation. For a feedback case, `artifact_id` and `artifact_version` are bound before `confirm`; `accepted_artifact_id` is a legacy field naming the reviewed artifact even for a rejected verdict. Store exact `human_rationale`, and keep `rule_candidate` or diagnosis tentative. Use `--scope` for exact project scope, and `--verdict rejected` for confirmed negative precedents. The command asserts an externally supplied event; it does not authenticate it.

JSONL is now authoritative. Old `index.json` and `rules.jsonl` may remain untouched but are ignored. Old pending cases without explicit artifact binding must be superseded by a bound pending case before confirmation. Do not invent missing provenance. Malformed primary JSONL is still an error; only derived-cache and optional retrieval-log failures have been removed from the read path.
