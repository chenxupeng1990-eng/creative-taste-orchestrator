# Taste memory and long-term improvement

Long-term memory stores evidence-backed decisions, not a growing list of slogans. Keep the project context and the scope of every rule so a local preference is not mistaken for universal taste. The skill must have an actual writable memory root to claim persistence; otherwise it returns an exportable memory patch.

## Storage contract

Use an append-only store with a stable root selected before the task:

```text
<memory-root>/cases.jsonl
<memory-root>/artifacts.jsonl
<memory-root>/rules.jsonl
<memory-root>/reviews/
<memory-root>/index.json
```

Use `scripts/taste_memory.py` to initialize, register an inspected artifact, append a proposed case, confirm a case through an explicit event, search, and validate this store. `add` cannot create a confirmed case; `confirm` requires a registered artifact, a non-model confirmer, a structured event, and a blind review receipt. Manual edits should be treated as untrusted until `validate` passes.

For a single project, prefer `<project>/.creative-taste/`. Use a shared cross-project root only when the user has requested global accumulation. Do not copy raw sensitive media into the store; keep a locator, hash, and short observation. Every append needs a timestamp, a unique case ID, source revision, and writer.

## Case record

Use a case record after a review reaches an explicit human verdict:

```yaml
case_id: ""
state: proposed | pending_human | confirmed | rejected | stale | superseded
created_at: ""
updated_at: ""
writer: "model or human identity"
source_revision: "project or artifact revision that produced this case"
domain: video | web | brand | campaign | other
context_summary: ""
intent: ""
references: []
artifact_evidence:
  - locator: "timecode, frame, URL state, component, or application"
    observation: "What is visibly present"
review:
  reviewer_id: ""
  reviewer_role: ""
  blind_to_history: true
  receipt: ""
verdict: accepted | rejected | mixed | accepted_after_revision
objections: []
revision:
  before: ""
  after: ""
  delta: ""
human_rationale: ""
confirmer_id: ""
confirmation_event:
  event_id: ""
  source: user_message | approval_record | project_decision
  human_asserted: true
confirmed_at: ""
accepted_artifact_id: ""
accepted_artifact_version: ""
rule_candidate: ""
scope: "project type, audience, medium, or style family"
confidence: low | medium | high
precedence: project_principle | confirmed_precedent | proposed_rule
reuse_count: 0
reuse_evidence: []
supersedes: []
superseded_by: []
follow_up: "What later use would validate or falsify this case"
```

Store positive and negative cases together. A rejected direction can be valuable as a boundary case, and an accepted direction can fail when the context changes.

## Promotion rules

- A model-generated observation is a proposal until the user confirms the verdict or names the revision that solved it.
- Promote a rule only when its scope is clear and it has either been reused successfully or is an explicit project principle.
- Preserve the original evidence and the human wording. Do not replace a concrete objection with a vague label such as “less tasteful.”
- Keep competing preferences when context explains the difference. Do not force them into one universal rule.
- Mark rules as stale when repeated work contradicts them; do not silently delete the history.
- Only `confirmed` cases and explicit project principles may enter precedent retrieval. `proposed`, `pending_human`, and `rejected` cases may be retrieved only as warnings or counterexamples. Use the script's default `search` state filter unless a deliberate counterexample review is being run.
- A confirmation must identify who confirmed which artifact version and when. A string inside a model-generated case is not a confirmation event.
- Resolve conflicts by scope: explicit project principle > project-local confirmed precedent > shared confirmed precedent > proposed rule. A narrower rule beats a broader rule when both apply.
- Never mutate an old case in place. Append a superseding case and preserve the old evidence.

## Retrieval before production

Before a new direction panel, retrieve:

- accepted precedents with a similar intent, medium, audience, or production constraint;
- rejected alternatives that resemble the current default;
- recurring objections and the fixes that resolved them;
- cases where a rule was valid only in a narrower context.

Give directors the relevant precedents as evidence, not as instructions to imitate. Ask them to state which relationship they are borrowing and what they are changing.

Retrieval must record the query, filters, returned case IDs, states, scopes, and the reason each case was relevant. Exclude pending cases from normal positive precedent retrieval. If the store is absent or unreadable, state `memory_unavailable` and continue without claiming accumulation.

## Drift and calibration review

Periodically inspect whether the system is:

- repeating one director's style regardless of brief;
- promoting surface patterns into universal rules;
- rejecting unusual work because it violates a familiar anti-pattern;
- accepting technically complete artifacts without audience evidence;
- storing scores without concrete visual, textual, or interactive proof.

The correction is a new comparison set, a narrower rule scope, or a changed director lens. Do not solve drift by adding more generic prohibitions.

Do not automatically rewrite the skill from one case. A methodology change requires either an explicit user decision or a repeated, confirmed failure pattern with a documented before/after comparison. Keep case memory and skill-version changes separate.

## Review record

Return this shape for a pending or completed audit:

```text
Intent:
First-view read:
Evidence:
Strongest objection:
Highest-impact fix:
Validation plan:
Memory status: pending | confirmed | rejected
```

## Fail-closed states

Use these states explicitly:

```text
memory_unavailable  no writable store or unreadable index
memory_pending      case proposed, human event missing
review_unverified   artifact or independent reviewer receipt missing
blocked             critical fact or hard-gate evidence missing
confirmed           human event names the accepted artifact version
```

Never treat `memory_pending`, `review_unverified`, or `blocked` as an accepted result.

## Taste calibration records

Memory should improve future choices, not merely preserve explanations. Prefer pairwise decisions and boundary cases:

```yaml
pairwise_decision:
  better_artifact: "A"
  worse_artifact: "B"
  user_wording: ""
  concrete_reason: "composition, hierarchy, material, type, rhythm, brand ownership, or other observable cause"
  scope: "medium, project type, audience, or brand"
```

Store rejected patterns as `anti_precedents` alongside accepted precedents. Retrieve relevant rejected patterns before production so the model can avoid a known failure, but do not turn one rejected surface treatment into a universal ban.

For a new creative task, retrieve a small relevant set: two to five accepted precedents, two to five anti-precedents, and the user's original wording. Prefer the same medium and intent. Do not inject every historical preference into the prompt; old style preferences can contaminate a new project.

Pairwise decisions and anti-precedents should retain the project scope, artifact version, evidence locator, and the exact user phrase that caused the decision. A record such as "less tasteful" without an observable reason is not useful calibration.