# Visual director board

Create this board before writing full HTML/CSS, building a component system, generating a complete video, or producing a large image set. It is a compact art direction lock, not a moodboard and not a component inventory.

## Shared board

```yaml
visual_director_board:
  visual_world: "What kind of place, object, event, or editorial system is this?"
  opening_scene: "What does the viewer enter first?"
  focal_anchor: ""
  counterpoint: ""
  quiet_zone: ""
  composition_grammar: ""
  scale_relationship: ""
  type_behavior: ""
  image_or_asset_strategy: ""
  light_and_color_proportion: ""
  material_behavior: ""
  motion_or_interaction_grammar: ""
  signature_behavior: ""
  responsive_or_temporal_change: ""
  first_proof: ""
  deliberate_absence: []
```

The board must establish one dominant relationship. It must not list every page, shot, component, or effect before the first proof exists.

## Authored tokens

If a code system or design system is needed, derive its tokens from the board:

```yaml
authored_tokens:
  type_scale: ""
  measure_and_line_length: ""
  grid_offset: ""
  radius_policy: ""
  stroke_and_shadow: ""
  material_or_surface: ""
  color_proportion: ""
  motion_durations_and_eases: ""
```

Tailwind, shadcn, Framer, or another library may provide structure. It cannot supply the project's visual language by default.

## Content and asset direction

Do not use placeholder content as proof of taste. Before judging layout, define:

- copy tone, length, and line-break behavior;
- image subject, camera position, crop, light, and negative space;
- product or character invariants across a sequence;
- evidence, data, or claims that must be real;
- the relationship between image, title, object, and action;
- assets that are allowed to vary and assets that must remain stable.

If the content or asset is only a placeholder, call the result a concept proof, not a style-locked artifact.

## Proof sizes

Use the smallest proof that reveals the creative risk:

- web: first viewport plus one scroll state;
- motion: four states — rest, anticipation, action, settle — plus a hold;
- static: key visual at intended display size;
- PPT: one visual KV page and one information-density page;
- detail page: first screen, purchase reason, and evidence block.

Do not add polish to a proof whose visual world, hierarchy, or signature is not yet convincing.
