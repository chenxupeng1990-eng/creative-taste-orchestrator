---
name: creative-taste-orchestrator
description: "Direct web, motion, video, brand, PPT, and commerce creative from inspected references to actual assets, medium-specific craft, comparable proofs, and applied revisions. Use when work feels generic, cheap, visually weak, or needs a deliberate production route."
---

# Creative Taste Orchestrator

Make the artifact better, not its explanation longer. Own the connection between direction and production: decide what must be made, use the right asset and rendering tools, inspect the result, and apply the next edit. Keep the host's existing production pipeline. Do not turn this skill into another renderer, committee, or aesthetic scoring service.

Preserve project instructions, approved facts, copy, identity, and required functionality. Public-facing content addresses the audience; internal directions such as "make a premium website", renderer names, QA claims, and implementation plans belong in project notes, not hero copy. A prototype disclosure belongs in an appropriate footer or colophon.

## Route before implementation

- `spark` / `review`: existing work A versus a targeted change B; no panel or unnecessary new assets.
- `taste-first`: two plausible visible directions at comparable fidelity, then targeted refinement.
- `system`: extended or multi-medium work; use the optional [panel](references/director-panel.md) without averaging incompatible directions.

For new visual production, read [production-routing.md](references/production-routing.md), then only the relevant [recipe](recipes/INDEX.md) and [web](references/web-art-direction.md), [motion](references/motion-art-direction.md), or [other-medium](references/domain-adapters.md) adapter. Read [asset-production.md](references/asset-production.md) when imagery, textures, models, or generated layers determine quality. Use [visual-feedback-loop.md](references/visual-feedback-loop.md) for comparison and [review-application.md](references/review-application.md) for the executable decision boundary. Thesis, board, and diagnostic references are optional aids, not required paperwork.

## Make before expanding

1. **Inspect and frame.** View actual reference images, states, or clips. Identify the focal relationship and the production bottleneck: asset, material, composition, motion, or implementation. A URL or style name is not a viewed reference. Declare an inaccessible reference and continue with a provisional original direction when appropriate.
2. **Choose the route.** Select procedural drawing/3D, generated or photographed layers, pre-rendered motion, or a hybrid. Name the actual producer/tool, required inputs, and resulting files. A requested renderer or interaction is an obligation, not a prestige label. Missing tools may limit production; they do not justify silently replacing the requested effect with particles or a different renderer.
3. **Build the decisive asset.** Inspect existing assets at the intended display size. If they cannot carry the requested image quality, produce or obtain the missing focal asset before full implementation. Preserve factual product identity. Keep blocking geometry and placeholder media explicitly provisional. Do not invent a generation receipt or use file metadata as proof of generation.
4. **Resolve one frame, then one beat.** Establish real composition, type, crop, lighting, and material together. For moving work, make the shortest meaningful action including entry and exit; a still cannot lock motion. Use the selected recipe's actual implementation or author the missing one. Stop expanding when the main subject still looks pasted, plastic, noisy, or unrelated to the brief.
5. **Compare fairly.** For new directions, make comparable A/B proofs. For repairs, A is the last-good baseline. Freeze factual content and viewing conditions; declare an intentional asset change rather than secretly giving one candidate better imagery. Package real captures using `scripts/build_comparison.py`, inspect originals, and record A/B/tie/neither/insufficient_evidence with visible reasons and regressions. Both ordinary may mean neither.
6. **Apply and read.** Run `scripts/apply_review.py --bundle <comparison> --state <project>/working-state.json`; read the resulting state before editing production sources. It binds a declared decision to snapshots, not to aesthetic truth. Pending, stale, tampered, or hard-failing selections cannot promote B. Preserve the source/assets/config matching the selected proof.
7. **Expand and exercise.** Carry the selected assets and scene behavior into real content, mobile layouts, and interactions. Inspect intermediate scroll/time states, reverse travel, resizing, loading failures, keyboard use, and reduced motion where relevant. Test actual output changes, not only counters, CSS variables, canvas existence, or a successful build. A fallback keeps content usable but does not fulfill a specifically requested 3D experience.
8. **Repair and learn.** Separate direction, craft, asset/content, and technical causes. Change the highest-impact cause, preserve strengths, re-render, compare, and apply. Store explicit human feedback separately from proposed diagnoses using [taste memory](references/taste-memory.md). Promote a reusable production recipe only with its implementation, actual evidence, limitations, and scope; do not relabel a failed brand trial as a positive precedent.

## Craft and operating limits

Truth, content, accessibility, task completion, and agreed cost remain the floor. Distinctive is not automatically better. Familiar grids, stillness, modest motion, and ordinary components can win. No forced metaphor, fixed deletion quota, mandatory risk, or global motion-area target.

Code should change the visible relationship or reliably produce, inspect, or preserve it. Every claimed effect needs a real consumer: a texture mapped to a surface, a camera driven by progress, a layer composited with registration, or an asset present in the final artifact. A file name, unused import, or material setting alone proves nothing. Reuse established host libraries; do not add another abstract runtime until a repeated production need exists.

Use one coordinating agent and narrow production tasks when delegation is available. Pass a shared composition/asset context and a concrete output contract. Do not claim independent review without an actually separate context. A same-context visual pass is self-review, even with neutral labels.

## Tools and delivery

The existing comparison, review-application, and memory tools stay narrow. They do not generate assets, judge pixels, authenticate people, publish, or make the host obey their state. `validate_gate.py` remains legacy record-shape diagnostics, never aesthetic acceptance. Recipe readiness labels are documentation, not new executable gate states.

Default to two small proofs and up to two targeted revisions, spending that effort on the highest-risk visual unit rather than a full mediocre site. Continue reversible work without asking at every step; ask when meaning, scope, permission, or paid-service cost changes. Report tool failure instead of disappearing into repeated calls.

Lead with the artifact, decision, visible change, and unresolved limitation. Keep planning, provenance, tests, and recipe notes in the project. Do not promise industry-leading quality from a checklist or call a code scaffold a finished visual asset.
