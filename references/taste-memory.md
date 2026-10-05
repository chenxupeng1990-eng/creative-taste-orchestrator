# Taste memory: feedback is not blind-review approval

Keep three things separate: the user's exact verdict, the model's proposed diagnosis, and a subsequently confirmed remedy. “The user rejected r01” does not mean “all gradients are bad.” Approval of an artifact does not confirm every rule in its rationale.

## Store and identity

The single-writer CLI stores `cases.jsonl`, `artifacts.jsonl`, and optional retrieval logs under `reviews/`. JSONL is authoritative. No new `rules.jsonl` or `index.json` is created. Legacy cache files are ignored, not deleted. Malformed primary records still require repair; do not silently discard history. Project-local memory is not automatically backed up or shared.

Register the reviewed artifact first. Bind every proposed feedback case to `artifact_id` and `artifact_version` before confirmation. A minimal case includes:

```json
{
  "case_id": "feedback-r01",
  "state": "pending_human",
  "writer": "assistant",
  "source_revision": "r01",
  "domain": "web",
  "intent": "Explain the brand's professional skincare identity",
  "artifact_id": "site-r01",
  "artifact_version": "r01",
  "artifact_evidence": [{"locator": "desktop/title", "observation": "Title and product compete"}],
  "verdict": "rejected",
  "human_rationale": "Exact user wording, only when it exists",
  "scope": "brand-project/web",
  "rule_candidate": "Unconfirmed diagnosis, not a user preference",
  "supersedes": []
}
```

The add command supplies timestamps. Confirmation still requires an actual externally supplied decision event and named confirmer, but **does not require blind review**. A user can dislike a page after seeing its entire production history. The CLI's event declaration is not identity authentication.

`accepted_artifact_id` and `accepted_artifact_version` remain legacy field names for the reviewed artifact, even when the verdict is rejected. Confirmation state and approval polarity are different. The confirmer may not switch the pending case to another registered artifact.

## Replay and supersession

Repeating the same source/event for the same case, confirmer, and artifact returns the original confirmation. Reusing that event for a different decision is rejected. To revise feedback, append a bound pending case naming the old confirmed case in `supersedes`, then confirm using a new event. Confirmed supersession is excluded from default retrieval. Never rewrite the old evidence in place.

Old unbound pending cases need a new explicitly bound case before confirmation. Do not guess their missing artifact provenance. Existing valid confirmed history remains readable.

## Scoped retrieval

```sh
python scripts/taste_memory.py search --root .creative-taste \
  --domain web --scope brand-project/web --verdict rejected --query "hierarchy"
```

The default state is confirmed. `--scope` is exact; no implicit cross-project fallback. `--verdict` separates accepted, rejected, mixed, or accepted_after_revision. Results also identify positive/negative/mixed roles. Optional retrieval-log failure warns but does not break a successful read.

This is lexical retrieval, not semantic learning. Use concise alternate queries when wording differs. Before the next proof, the agent retrieves relevant feedback, inspects its context, names one applicable risk, and checks the new artifact for that risk. A no-hit search is not proof that the user has no preference.

Working A/B selection is not a human preference. Do not call confirm for an internal self-review. Store diagnoses as hypotheses until separately supported; retain artifact approval and rule approval independently. Shared/global accumulation requires the user's permission.
