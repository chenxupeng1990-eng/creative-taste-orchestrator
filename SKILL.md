---
name: creative-taste-orchestrator
description: "Guide video, website, brand-visual, campaign, and other experience work through independent director proposals, structured judging, deliberate synthesis, artifact review, and human-confirmed taste memory."
---

# Creative Taste Orchestrator

Use this skill when creative direction is the work: defining a visual or experiential concept, planning a production, comparing directions, improving a rendered artifact, or reviewing a finished result. Do not invoke it for routine implementation, generic copyediting, or a simple visual tweak unless the user is asking for a taste or direction decision.

The skill has two connected jobs:

1. **Production guidance:** turn an ambiguous brief into competing creative hypotheses, a chosen direction, executable contracts, and a revision queue.
2. **Taste calibration:** compare the actual artifact with intent, references, and accepted precedents, then record only human-confirmed judgments for future work.

Read the repository's `AGENTS.md`, project brief, existing design system, and any project-specific creative protocol first. Project instructions and explicit user decisions take precedence over this skill. State important assumptions before committing to a direction.

Before starting, run a capability preflight:

- **Facts:** identify facts that can change the direction or acceptance decision. For claims, regulation, business goals, audience, accessibility, budget, or production limits, missing evidence is `blocked`, not a silent assumption.
- **Independence:** determine whether the director and judge passes can run in separate contexts or isolated calls. Record `independent`, `simulated`, or `unverified`; never present role-play in one context as verified independence.
- **Artifact access:** confirm a real file, URL, prototype, playback, renderer, or screenshot source is available. Without artifact evidence, the result is a proposal or desk critique, not a creative acceptance.
- **Memory:** identify a writable, versioned memory root. If none is available, return a memory patch for a human to apply and do not claim long-term persistence.
- **Reviewer separation:** identify who produced the artifact and who will review it. If the reviewer shares the producer's context or can see its generation history, mark the review `review_unverified` and block creative acceptance.

## Core workflow

Follow this sequence unless the user requests a narrower mode:

1. **Build a context pack.** Capture the audience, intended effect, all relevant mediums, duration or interaction scope, reference baseline, source-backed facts, cross-domain relationships, hard constraints, resources, forbidden patterns, and acceptance gates. For visual work, also write a one-line design read, set `variance`, `motion`, and `density` dials, and lock the palette, typography, material, and shape rules that must stay coherent. Separate facts, preferences, assumptions, and blockers.
2. **Run an independent director panel.** Produce three materially different directions. Use the default lenses in [director-panel.md](references/director-panel.md), then adapt them to the medium. Give every director the same frozen context snapshot, isolate their calls, assign a run ID, and record an independence receipt. If isolation is unavailable, label the panel simulated and lower the confidence.
3. **Judge the directions.** Compare them against the same intent, facts, and constraints. Blind labels where practical. Require each judge to name the strongest artifact or card evidence, every hard-gate failure, the fatal objection, and the conditions under which an element could be reused. Scores may help sort options; they never replace concrete objections or vetoes.
4. **Make a head-director decision.** Select one primary spine. Process every hard gate and fatal objection before borrowing anything. Borrow only elements that preserve the spine's meaning and behavior. Do not average three directions into a collage. Record chosen, borrowed, incompatible, rejected, and unresolved elements.
5. **Compile the direction for the medium.** Use the adapter in [domain-adapters.md](references/domain-adapters.md). Create a versioned artifact manifest before expensive production. Every motion or interaction must state its trigger, start state, visible delta, duration or scope, end state, and handoff. Every visual element needs a narrative, informational, brand, or interaction job.
6. **Render or prototype before judging.** Inspect the real artifact: playback and contact sheets for video, responsive states and interaction paths for web, application mockups and material tests for brand work. Record source, tool, version, hash or receipt, viewport/state coverage, and observation. Describe what a first-time viewer sees before explaining intent.
7. **Review independently.** A reviewer should see the intent, criteria, and artifact without the generation history. Record reviewer identity, role, blind status, time, evidence locator, observation, why it matters, and a falsifiable test. A producer reviewing its own work is `review_unverified`; no missing locator means no acceptance. Keep technical verification, creative acceptance, memory confirmation, and publication as separate gates.
8. **Revise with visible deltas.** For each fix, name the before state, the change, the reason, and the evidence that will decide whether it worked. Re-render the affected artifact and re-review when the change is material. Stop after the agreed revision budget or escalate unresolved objections; do not relabel an unresolved objection as success.
9. **Write taste memory only after confirmation.** Use [taste-memory.md](references/taste-memory.md). A model may propose a reusable rule, but it must not promote its own critique to a durable preference. Store accepted and rejected examples together, with scope, evidence, confirmation event, and version. Only `confirmed` cases may be retrieved as precedents.

## Operating rules

- Three proposals are a minimum deliberation pattern, not a quota. If a brief is too small for three full directions, produce three distinct hypotheses at the smallest useful scale and say what was reduced.
- Variation must be material. Changing only color, font, or surface treatment is not a new direction; change the premise, formal system, information structure, audience effect, interaction model, or production method.
- Preserve a causal chain for experience work: **trigger → ordered states → visible deltas → handoff**. No triggerless motion, decorative transition, or element without a job.
- Treat references as a baseline and relationship, not a moodboard to imitate. Name what is being borrowed: rhythm, material response, composition, joke structure, typography, or system behavior.
- Use dials and system locks to make taste operational, but keep them scoped to the brief. A dial controls exploration; it does not prove quality. An anti-pattern is a warning, not a substitute for a positive reference or a visible acceptance criterion.
- Do not use a single aggregate “taste score” as acceptance. Use hard gates plus specific evidence and objections.
- Do not claim an artifact is final because a build, schema, or render succeeded. Report technical status and creative status separately.
- Do not claim that a reviewer, artifact, render, or human decision exists unless its receipt, locator, or confirmation event is present.
- Do not write to long-term taste memory without an explicit human verdict such as accepted, rejected, or accepted with a named revision.
- When a merge creates a contradiction, choose a primary behavior and reject the conflicting element instead of hiding the conflict in prose.
- When critical facts, evidence, or gates are missing, fail closed with `blocked`, `review_unverified`, or `memory_pending`; do not fill the gap with confident prose.
- Before reporting `accepted_creative` or `confirmed`, run `scripts/validate_gate.py` against the status record. A passing text checklist is not a gate result.

## Output contracts

For production work, return:

- a concise context pack and assumptions;
- three direction cards with distinct theses, audience effects, formal systems, signature moves, risks, and rejection conditions;
- a judge comparison with strongest evidence, fatal objections, and merge conditions;
- a head-director decision record;
- medium-specific production contracts and an artifact review plan.

For review work, return:

- the intended effect and acceptance criteria;
- what a first-time viewer actually sees;
- timecode, frame, state, or component evidence for every major objection;
- ranked fixes with before/after deltas and validation evidence;
- a proposed memory case, marked as pending until the user confirms it.

Always include a status and receipts section in production or review output:

```yaml
status: draft | blocked | proposed | rendered | review_pending | revision_required | accepted_technical | accepted_creative | memory_pending | confirmed | rejected
independence: independent | simulated | unverified
artifact_manifest: "path or URL, version, hash/receipt, coverage"
review_receipt: "reviewer ID/role, blind status, observed_at, evidence locators"
memory_receipt: "case ID, state, confirmer, event, or pending reason"
```

Use the supporting references only when their mode is relevant:

- [director-panel.md](references/director-panel.md) for independent proposals, judges, and head-director synthesis;
- [domain-adapters.md](references/domain-adapters.md) for video, web, brand, and other medium-specific evidence;
- [taste-memory.md](references/taste-memory.md) for precedent storage, promotion, retrieval, and drift review.

The bundled validators are deliberately narrow: `scripts/validate_gate.py` checks status/receipt combinations, while `scripts/taste_memory.py` manages the structured memory store. They do not prove audience response, regulatory truth, or intrinsic aesthetic quality; those still require real artifacts, facts, and a trusted human decision.
