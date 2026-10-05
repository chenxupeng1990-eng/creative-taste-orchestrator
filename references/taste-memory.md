# Taste memory: feedback, diagnosis, and reuse

Store decisions with evidence and scope, not aesthetic slogans. “The user rejected r01” and “the user dislikes all gradients” are different claims. The first may be observed; the second usually is an unsupported generalization.

## Three separate records

1. **User observation/verdict:** exact wording, message/decision locator, artifact and version, accepted/rejected/mixed.
2. **Model diagnosis:** proposed failure type and cause, evidence location, uncertainty, and the next comparison that could test it.
3. **Confirmed remedy or rule:** what changed, the user's response to that version, scope, and conditions for reuse.

Never label the model's explanation user-confirmed merely because the user said “丑” or approved the finished artifact. Artifact approval also does not confirm every proposed universal rule. Avoid making the user complete a taxonomy; record the wording and do the diagnostic work.

## Existing storage and commands

Use a project-local writable root by default:

```text
<project>/.creative-taste/cases.jsonl
<project>/.creative-taste/artifacts.jsonl
<project>/.creative-taste/rules.jsonl
<project>/.creative-taste/reviews/
<project>/.creative-taste/index.json
```

The existing [taste_memory.py](../scripts/taste_memory.py) supports init, register-artifact, add, confirm, search, and validate. `add` cannot create a confirmed case. `confirm` requires a registered artifact, human/external confirmer, explicit event, and a blind review receipt. Never invent a receipt to satisfy that contract; retain a pending case when it cannot be met. A command argument is not authentication of a real human event.

Use shared memory only with user permission. Keep sensitive media out of the store; retain authorized local locators, hashes, and brief observations. The ignored project directory is not automatically synchronized or backed up. If persistence is unavailable, provide a patch and state memory_pending or memory_unavailable.

## Case shape

Retain the fields consumed by the existing script. Additional calibration fields are descriptive metadata, not new automatic behavior:

```yaml
case_id: ""
state: "pending_human"
created_at: "ISO timestamp"
updated_at: "ISO timestamp"
writer: ""
source_revision: ""
domain: "web"
intent: ""
context_summary: ""
artifact_evidence:
  - locator: "actual artifact region or timecode"
    observation: "what is present"
review:
  reviewer_id: ""
  reviewer_role: ""
  blind_to_history: false
  receipt: ""
  evidence_locators: []
verdict: "rejected"
human_rationale: "exact user wording, not an invented cause"
scope: "medium, intent, audience, project"
calibration:
  feedback_locator: ""
  failure_type: "direction | craft | asset_content | technical | uncertain"
  proposed_cause: ""
  diagnosis_status: "hypothesis"
  next_avoidance_test: ""
  exceptions: []
pairwise_decision:
  baseline_artifact: ""
  candidate_artifact: ""
  decision: "A | B | tie | neither | insufficient_evidence"
  evidence_locators: []
  preserved_strengths: []
rule_candidate: ""
reuse_evidence: []
supersedes: []
```

A confirmed record additionally needs the actual confirmer/event/time and accepted_artifact_id/version required by the script. Despite the legacy name `accepted_artifact_id`, a confirmed case can have a rejected verdict. Keep confirmation state distinct from approval polarity.

## Retrieval before the next proof

Search a small relevant set by medium, intent, and failure wording. The current script performs lexical matching, not semantic search or automatic style learning. With Chinese or differently worded feedback, use several concise queries or a broader domain query, then inspect the results.

```sh
python /path/to/skill/scripts/taste_memory.py search \
  --root .creative-taste --domain web --states confirmed --query "hierarchy"
```

The default confirmed filter returns confirmed decisions of multiple verdicts, not only positive examples. Before using the results, the orchestrating agent must:

- separate accepted/accepted_after_revision precedents from rejected counterexamples and inspect mixed cases;
- honor supersession links and exclude old/stale interpretations; the CLI does not resolve this automatically;
- match scope and user intent, preferring explicit current project decisions over older or shared preferences;
- treat pending diagnoses as hypotheses, never positive authority;
- record the retrieved IDs and one concrete implication for the next proof.

Do not retrieve a quota of cases if only one is useful. Do not append every historic aesthetic preference to the prompt. “Avoid this repeated equal-weight card hierarchy in dense evidence pages” is useful; “never use cards” is not.

## Close the loop without inventing learning

At the next applicable task: retrieve the counterexample, name the failure to avoid, inspect the new proof for it, and record whether the remedy held. Keep a pairwise comparison and the user's subsequent response. Append a new case rather than silently rewriting prior evidence.

This is an agent-executed retrieval and comparison procedure. The CLI does not automatically trigger on feedback, classify taste, rank by scope, promote rules, retire cases, or populate rules.jsonl. That file remains reserved. Do not claim these capabilities because metadata fields exist. This iteration changes the protocol, not the memory engine.

A rule becomes durable only with scoped human confirmation or an explicit project principle. Successful reuse supports a rule; repeated contradiction calls for narrowing or supersession, not an ever-growing prohibition list. Case history and skill methodology versions remain separate.
