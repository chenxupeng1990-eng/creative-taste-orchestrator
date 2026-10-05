# Director panel method

The panel is a deliberation device, not a request for three similar brainstorms. The outputs are independent hypotheses about the same brief.

## Context pack

Before calling a director, prepare one shared context pack:

```yaml
project:
  name: ""
  mediums: [video, web, brand, campaign, other]
  audience: ""
  intended_effect: ""
  deliverable: ""
  duration_or_scope: ""
  decision_owner: ""
  decision_deadline: ""
references:
  baseline: []
  borrowable_relationships: []
design_read: "One sentence describing the intended visual or experiential read"
dials:
  variance: 1-10
  motion: 1-10
  density: 1-10
system_locks:
  palette: []
  typography_or_voice: []
  shape_or_material: []
  interaction_or_editing: []
anti_patterns: []
facts:
  - id: ""
    statement: ""
    source: ""
    verified_at: ""
    sensitivity: public | internal | restricted
cross_domain_map:
  - premise: ""
    web: ""
    video: ""
    packaging: ""
    social: ""
constraints:
  hard:
    - id: ""
      owner: ""
      pass_condition: ""
      evidence_required: ""
  forbidden: []
  resources: []
acceptance:
  technical: []
  creative: []
  human_decision_required: true
open_questions: []
blockers: []
```

Do not let a director invent a missing business, legal, audience, claim, accessibility, or production fact. Mark low-impact assumptions and continue when a reasonable assumption is enough. Set a blocker and ask when the missing answer changes the direction materially. Freeze the context snapshot before independent runs; later facts are an explicit revision, not a silent change.

## Default lenses

Adapt these lenses to the medium while preserving their separation:

1. **Meaning director** — clarifies the premise, cultural or narrative point, audience understanding, and emotional after-effect.
2. **Form director** — designs the visual, sonic, verbal, material, typographic, or spatial language and its signature move.
3. **Experience director** — designs how the work unfolds, is used, is remembered, and can be produced consistently within the constraints.

For a video these may become narrative, visual-rhythm, and production-performance directors. For a website they may become editorial-IA, art-direction, and interaction-system directors. For a brand system they may become positioning, visual-material, and extension-system directors. Keep the roles independent; do not make every director solve every problem in the same way.

## Isolation receipt

When delegation or separate calls are available, run one director per isolated context. Pass only the frozen context snapshot and that director's lens. Do not pass another director's card, hidden reasoning, or ranking into a later director call. Save the run IDs and context revision. Run judges after all cards exist; blind the labels when practical.

When separate contexts are unavailable, make separate passes with the same frozen input and do not show earlier outputs to later passes. Mark the result `simulated` rather than `independent`. If the same pass is asked to invent, judge, and merge without isolation, mark independence `unverified` and keep creative acceptance blocked.

## Direction card

Require each director to return one complete card and an independence receipt:

```yaml
id: A
run_id: ""
context_snapshot: "sha256 or stable revision ID"
independence: independent | simulated | unverified
thesis: "The one-sentence creative bet"
audience_effect: "What a first-time viewer should feel, understand, or do"
formal_system:
  composition: ""
  material: ""
  type_or_voice: ""
  color_or_tone: ""
  behavior: ""
signature_move: "The memorable operation that makes this direction specific"
artifact_plan: []
assumptions: []
risks: []
reject_if: []
material_difference:
  changed_axes: [premise, formal_system]
  compared_with: [B, C]
  why_not_surface_only: ""
```

The three cards must differ on at least one material axis: premise, formal system, information structure, audience effect, interaction model, pacing, or production method. Surface-only variation does not count.

Before judging, run a difference check. Require at least two changed axes or one changed axis with a different audience effect and production behavior. If the cards are near-duplicates, regenerate the weakest card with an explicit anti-default constraint. Record the check instead of trusting the labels A/B/C.

## Independent judging

Judges receive the context pack and all direction cards, not the directors' hidden reasoning. Use at least three lenses:

- **Audience judge:** what is legible and memorable on first contact?
- **Taste judge:** what is specific, coherent, surprising, and free of default or derivative signals?
- **Producer judge:** what can be executed, tested, iterated, and extended without losing the idea?

Each judge must provide:

```yaml
strongest_evidence: ""
fatal_objection: ""
best_reusable_element: ""
merge_condition: ""
hard_gate_failures: []
evidence_locators: []
blind_to_generation_history: true
ranking: []
```

Use numeric scores only to expose disagreement or sort a shortlist. A high score without evidence is not approval. A hard-gate failure is a veto until its evidence changes. A fatal objection must be answered in the head-director record or remain `unresolved`; it cannot be hidden in a weighted average.

## Head-director synthesis

The head director makes a decision record rather than an average:

```yaml
primary_spine: ""
chosen_from: A | B | C
borrowed_elements:
  - source: B
    element: ""
    compatible_because: ""
rejected_elements:
  - source: C
    element: ""
    reason: ""
unresolved_risks: []
validation_artifacts: []
hard_gates_processed: []
fatal_objections_processed: []
conflicts: []
```

Choose one primary behavior for each important question. If two elements compete for the same role, keep one and log the rejection. The synthesis is successful when a stranger can describe one coherent direction, not when every director sees a fragment of their idea in it.

## Falsification pass

Before execution, run a red-team pass against the head-director decision. Give the critic only the context pack, decision record, and intended artifact contract. Require three strongest failure modes, the evidence that would expose each one, and the smallest change that could falsify the criticism. The head director must resolve, accept, or explicitly carry each objection into `unresolved_risks`; unresolved critical objections keep the decision at `revision_required`.

## Production handoff

Translate the decision into the medium's contract. For temporal or interactive work, define the trigger, start state, visible delta, duration or scope, end state, and handoff. For static work, define the hierarchy, material behavior, application context, and failure cases. Include a review plan before expensive generation or broad implementation begins.
