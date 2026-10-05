---
name: creative-taste-orchestrator
description: "Improve web, motion, video, brand, PPT, and commerce creative through observed references, comparable rendered proofs, applied review decisions, and scoped human feedback. Use when selecting a direction or when work feels generic, cheap, or visually weak."
---

# Creative Taste Orchestrator

Make the artifact better, not its explanation longer. A thesis is a hypothesis; inspect actual work before defending it. Preserve approved business facts, copy, identity, and project instructions. Use the host's existing production tools, not a replacement framework.

## Floor and modes

Truth, required content, accessibility, task completion, and agreed limits are non-negotiable. Inside that floor, choose the relationships that suit the brief. Unusual is not automatically better. Familiar grids, stillness, modest interactions, and restrained typography can win. Do not require a dramatic metaphor, artificial risk, fixed deletion percentage, or a thesis reset after two implementation mistakes.

- `spark` / `review`: existing work A versus a targeted change B; no panel.
- `taste-first`: two plausible visible directions at comparable fidelity, then a decision and targeted refinement.
- `system`: an extended or multi-medium task; use the director panel without averaging incompatible directions.

Read [visual-feedback-loop.md](references/visual-feedback-loop.md) and the relevant [web](references/web-art-direction.md), [motion](references/motion-art-direction.md), or [medium](references/domain-adapters.md) adapter. Load the thesis, board, diagnosis, or examples references only when needed. [review-application.md](references/review-application.md) defines the executable decision boundary.

## Production loop

1. Frame one visual question using the real brief and assets. Retrieve a small set of relevant references and scoped feedback. A URL or style name is not an inspected visual source. If a reference cannot be viewed, disclose that gap and make an original provisional proof.
2. State the intended first impression, dominant relationship, quiet region, and expected visible result. Translate adjectives into scale, crop, typography, space, material, timing, and sound. Keep the brief compact.
3. Render comparable A/B proofs before expanding. Same content, assets, viewports, loaded fonts, and relevant states. For a revision, A is the last-good working baseline. Preserve source files as well as screenshots. Do not reward one candidate with better photography than the other.
4. Package actual captures with `scripts/build_comparison.py`. Inspect originals at intended size. Look first without rationale, then with the brief. Record `A`, `B`, `tie`, `neither`, or `insufficient_evidence`, located observations on both sides, hard failures, and regressions. Self-review is useful but is not independent review.
5. Apply the record with `scripts/apply_review.py --bundle <comparison> --state <project>/working-state.json`. Pending records, changed snapshots, stale baselines, unresolved hard failures, and mismatched review/manifest bindings cannot select a version. `B` promotes its exact proof snapshots; `A` or `tie` preserves A; `neither` requests revision without discarding the last-good version; insufficient evidence stays pending.
6. Read the resulting working state before production. Implement only the selected direction. Separate direction, craft, content/assets, and technical causes. Make one main revision hypothesis, protect existing strengths, and re-render. New evidence must win another comparison before replacing the baseline. Never rename screenshots to make a different revision look like A.
7. Expand the selected direction with real content and interactions. Check desktop, intermediate width, mobile, loading failures, keyboard focus, and reduced motion as relevant. Proof selection is not acceptance of an entire website or film.
8. Record human feedback separately from model diagnoses. Bind the case to the exact artifact ID/version before confirmation. A user's explicit preference does not require blind-review permission. Keep the proposed explanation unconfirmed until supported. Retrieve negatives within their scope next time.

## Small executable tools

The comparison builder snapshots supplied media and presents them; it neither captures nor judges. `apply_review.py` verifies snapshot bytes and applies the declared decision to a working baseline. It does not inspect pixels, authenticate a reviewer, modify production sources, grant publication, or establish audience response. A host must actually read its selected state. Source-code/asset archives still belong to the production project.

`validate_gate.py` is retained only as legacy record-shape diagnostics. `record_valid` never means accepted. It is no longer the required path for iteration or human preference confirmation. Do not claim formal creative acceptance from its exit code.

`taste_memory.py` keeps JSONL cases and artifacts as primary records. It no longer creates unused rules or a fragile derived index. Confirmation is idempotent by event, rejects artifact switches, and requires an explicit human event. Search filters confirmed supersessions and accepts exact `--scope` and `--verdict`; retrieval-log failure warns but does not prevent reading. These scripts are single-writer project tools, not an adversarial authorization service.

## Work budget and delivery

Default to two low-cost proofs and up to two targeted revision passes. Continue reversible production without asking for approval at every internal step. Ask only when a missing decision changes meaning, cost, permission, or scope. Do not stop at a proof plan when available tools can render it.

Lead with the working artifact, recommendation, visible reason, and remaining limitation. Save comparisons, tests, and source references in the project. Label synthetic examples, self-review, partial coverage, and pending human feedback honestly. A build, screenshot, test suite, or filled checklist alone cannot prove tasteful work.
