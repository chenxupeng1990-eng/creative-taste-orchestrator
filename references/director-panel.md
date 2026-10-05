# Art director panel

The panel is a deliberation device, not a request for three balanced brainstorms. Its purpose is to protect a strong creative spine from premature feasibility and consensus.

## Default posture

For `taste-first` work, use:

1. **Primary Art Director** — makes one complete, specific, risky bet.
2. **Wild Card** — proposes one materially incompatible alternative that attacks the category default.
3. **Hostile Critic** — tries to kill the lead with concrete evidence, then names the smallest change that could save it.

Use the full panel only for `system` work. Never average directions, vote for a compromise, or hide incompatible behaviors in a synthesis.

## Frozen context

Before a full panel, prepare one shared context snapshot:

```yaml
project:
  name: ""
  mediums: [video, web, brand, campaign, ppt, detail_page, other]
  audience: ""
  intended_effect: ""
  deliverable: ""
  duration_or_scope: ""
  decision_owner: ""
  decision_deadline: ""
business_truth: ""
audience_tension: ""
references: []
design_read: ""
taste_thesis: {}
system_locks:
  palette: []
  typography_or_voice: []
  shape_or_material: []
  layout_or_composition: []
  image_or_asset: []
  motion_or_interaction: []
anti_patterns: []
facts: []
constraints:
  hard: []
  delivery: []
  forbidden: []
  resources: []
acceptance:
  technical: []
  creative: []
  human_decision_required: true
open_questions: []
blockers: []
```

Freeze the context before independent runs. Later facts are an explicit revision, not a silent change. Keep business and identity constraints ahead of ideation; solve delivery constraints after a primary spine exists unless they change the creative premise.

## Direction card

Every direction must return:

```yaml
id: lead | wild_card | other
run_id: ""
context_snapshot: ""
independence: independent | simulated | unverified
point_of_view: "What does this direction believe?"
tension: ""
thesis: "The one-sentence creative bet"
audience_effect: "What a first-time viewer should feel, understand, or do"
dominant_gesture: ""
signature: ""
hierarchy:
  dominant: ""
  supporting: ""
  quiet: ""
visual_grammar:
  composition: ""
  scale: ""
  space: ""
  type_or_voice: ""
  image_or_asset: ""
  material_or_light: ""
  motion_or_behavior: ""
restraint: ""
sacrifice: ""
reference_translation: []
proof_artifact: ""
assumptions: []
risks: []
reject_if: []
material_difference:
  changed_axes: []
  why_not_surface_only: ""
```

Changing only color, font, or surface treatment is not a new direction. In `system` mode, directions must differ on at least two of premise, composition, information structure, audience effect, interaction model, pacing, material behavior, or production method. Include one wildcard with a real risk and a stated legibility floor.

## Selection and attack

Select in this order:

1. brand or project specificity;
2. point of view and signature survival;
3. medium-native craft;
4. composition and hierarchy;
5. legibility and extension;
6. feasibility and cost.

Before any numeric comparison, run binary kill tests:

- the direction works for any brand;
- removing logo and copy removes the entire identity;
- the first view has no memorable object, relationship, or action;
- the result is only a component or transition inventory;
- the proof relies on polish to conceal a weak premise.

The head director must produce a single decision record:

```yaml
primary_spine: ""
chosen_from: lead | wild_card | other
signature_to_preserve: ""
deliberate_risk: ""
borrowed_elements: []
rejected_elements: []
deliberate_absence: []
unresolved_risks: []
validation_artifacts: []
hard_gates_processed: []
fatal_objections_processed: []
conflicts: []
```

## Critical review

The critic receives the proof before the rationale when possible. Require:

```yaml
blunt_verdict: ""
first_view_read: ""
strongest_evidence: []
generic_signals: []
signature_survival: ""
fatal_objection: ""
highest_leverage_change: ""
removal_candidates: []
evidence_locators: []
```

If the same spine is rejected twice, return to the thesis and replace it. Do not keep polishing a rejected premise.
