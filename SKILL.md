---
name: creative-taste-orchestrator
description: "Improve web, motion, video, brand, campaign, PPT, and commerce creative through visible references, concrete art direction, comparable rendered candidates, and baseline-preserving revision. Use when choosing a direction or when work feels generic, ugly, cheap, or visually weak."
---

# Creative Taste Orchestrator

Make the artifact better, not its explanation longer. A taste thesis is a hypothesis; only the visible or audible work can support it. Specificity matters, but unusual is not automatically beautiful, effective, or appropriate.

Read project instructions, the brief, approved copy, existing design rules, and explicit user decisions in every mode. Preserve frozen business and content decisions. This skill directs and compares creative work; downstream tools or skills implement it. Do not replace an existing production pipeline with a new framework just to use this skill.

## Non-negotiable floor and creative ambition

Truth, required content, accessibility, core task completion, identity continuity, and agreed production limits are not traded for novelty. Within that floor, pursue a clear point of view, strong composition, appropriate distinctiveness, and medium-native craft. Choose the priorities that matter to this brief; do not calculate a universal taste score.

An ordinary grid, restrained typography, familiar interaction, or still frame can be the best choice. Do not require decorative signatures, forced asymmetry, a dramatic metaphor, a fixed deletion percentage, or a mandatory risk. A useful trade-off may be none. Diagnose a weak premise separately from poor execution of a good premise.

## Mode and reading budget

- `spark`: one local decision; compare the existing artifact with one revision. No panel.
- `taste-first` (default): one recommended direction and one genuinely plausible alternative, expressed as two small visible proofs. Then choose, refine, and expand.
- `system`: multiple media or an extended system; use [director-panel.md](references/director-panel.md) without averaging directions.
- `review`: inspect supplied work, preserve its strengths, and repair the highest-impact failure.

Read [visual-feedback-loop.md](references/visual-feedback-loop.md) plus the relevant medium adapter before the first proof. Load [taste-first-protocol.md](references/taste-first-protocol.md) or [visual-director-board.md](references/visual-director-board.md) only when the direction needs clarification. Use [anti-mediocrity.md](references/anti-mediocrity.md) for diagnosis, [examples.md](references/examples.md) for teaching examples, and [taste-memory.md](references/taste-memory.md) when retrieving or recording decisions. Do not dump all references into every task.

## Production loop

1. **Frame the decision.** Identify the intended effect, audience, real content/assets, hard constraints, and the one visual problem to solve. Reuse known context. Missing creative detail can become a stated hypothesis; do not invent missing product facts.
2. **Look before naming.** Inspect a small relevant set of actual reference images, pages, or clips and applicable accepted/rejected precedents. A URL, article summary, or remembered style name is not an inspected reference. If access is unavailable, state the gap and make an original provisional proof rather than inventing what a reference shows.
3. **Make a compact bet.** State the intended first impression, dominant visual relationship, what must stay quiet, and what the proof should demonstrate. Translate adjectives into scale, placement, crop, typography, material, light, timing, or sound. A few lines usually suffice.
4. **Render comparable proofs early.** Use the same content, product, scope, and viewing conditions. In a new direction task, render A and B at similar fidelity. In a revision task, A is the saved last-good baseline and B is the proposed change. Make the smallest proof that tests the risky decision; do not build the full site or film first.
5. **Compare the actual work.** First describe A and B without their design rationale; then compare with intent and references. Follow the pairwise contract in [visual-feedback-loop.md](references/visual-feedback-loop.md). Allow `A`, `B`, `tie`, `neither`, or `insufficient_evidence`. A new version is not presumed better.
6. **Diagnose and change.** Separate direction, execution/craft, asset/content, and technical failures. Preserve the strongest existing relationships. State one main hypothesis, change a small coherent set of variables, and name the expected visible delta and rollback condition. Deletion, refinement, addition, or replacement are all valid repairs.
7. **Re-render and compare again.** Keep source and proof versions. Check the changed region and at least one protected strength or neighboring state. Promote B to the working baseline only when the comparison supports it. If ambiguous, retain A and identify the next discriminating test.
8. **Expand the selected direction.** Apply the relevant [domain adapter](references/domain-adapters.md). Recheck a real content section, mobile composition, transition, later shot, or application—not just the hero. Selection of a proof is not acceptance of the entire artifact.
9. **Record the user's decision.** Preserve exact feedback, artifact version, observed failure, proposed cause, and confirmed remedy separately. Retrieve relevant negative cases next time, scoped to the medium and intent. Do not turn model diagnoses into user preferences.

## Iteration control

For an ordinary task, default to two low-cost proofs and up to two targeted revision passes, unless the user specifies otherwise. This is a work budget, not a guarantee of acceptance or a universal ban on further iteration. After repeated failure, identify whether the concept or its execution is responsible before changing the thesis. Repetition alone does not prove the concept is wrong.

Do not interrupt the user for approval at every internal step. If authorized to produce the work, make a recommendation and proceed through reversible decisions. Ask only when an unresolved choice materially changes scope, meaning, cost, or permission. Do not stop at a proof plan when the available tools can produce the proof now.

## Evidence and status

Keep capture, technical checking, comparative judgment, human preference, and publication separate. A screenshot proves a capture exists; it does not prove hierarchy. A pixel difference is not an aesthetic improvement. A successful render is not audience validation.

Use existing browser/rendering tools to create evidence. [build_comparison.py](scripts/build_comparison.py) packages existing local images or clips into an offline A/B board, saves snapshot hashes, and creates a pending review template. It does not capture screens, decode/inspect artwork, synchronize video, judge quality, enforce workflow execution, or confirm human decisions.

A rationale-free first pass in the same context is self-review, not verified blinding. A separate reviewer receives only the brief, criteria, and artifacts; record actual separation or mark it unverified. Missing separation does not prevent useful iteration, but does prevent a claim of independent acceptance.

For formal `accepted_creative` or `confirmed`, retain the existing structured artifact/reviewer/memory receipts and run [validate_gate.py](scripts/validate_gate.py). Its result is a record check, not a taste score. Working selection remains `rendered`, `review_pending`, or `revision_required` as appropriate; never rename an unreviewed proof to accepted. Do not claim the comparison helper and the legacy gate are automatically connected.

## Deliverable first

Lead with the artifact or comparison, the recommendation, the visible reason, and the next change if one remains. Save structured comparison and revision records in the project; do not make the user read a committee report or fill a dossier. Label synthetic examples, incomplete coverage, self-review, and memory pending honestly.
