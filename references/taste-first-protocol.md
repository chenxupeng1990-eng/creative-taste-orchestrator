# Taste-first protocol

Use this reference before a visual direction becomes a component list, prompt collection, HTML file, or full edit. The purpose is to force an authored choice while the cost of changing the premise is still low.

## The ten moves

### 1. Name the tension

State the relationship that must remain in the work. It should be more useful than a category label or mood word.

```yaml
business_truth: ""
audience_tension: ""
creative_tension: ""
```

Examples of useful tensions include tradition × everyday convenience, scientific authority × human warmth, archive × live event, precision × softness, or product utility × collectible desire.

### 2. Make one claim

Write one visual claim that a stranger could disagree with. Avoid a list of values.

```yaml
visual_claim: "The page should feel like ... because ..."
```

If the claim could describe ten unrelated brands, rewrite it.

### 3. Choose one gesture

Choose one repeated operation that carries the direction: an aperture opening, a measured cut, a subject emerging from a quiet field, a vertical scan, a folding plane, a slow reveal, a hard editorial crop, or another concrete behavior.

```yaml
dominant_gesture: ""
gesture_scope: [hero, scroll, section_transition, shot, interaction]
```

### 4. Define one signature

The signature should survive removal of the logo and most explanatory copy. It may be an object, a crop, a spatial relationship, a material reaction, a rhythm, or an interaction behavior.

```yaml
signature: ""
signature_survival_test: ""
```

### 5. Set the hierarchy

Name the dominant, supporting, and quiet layers. The work needs a lead actor and a controlled absence.

```yaml
hierarchy:
  dominant: ""
  supporting: ""
  quiet: ""
```

### 6. Choose restraint and sacrifice

Every distinct direction must refuse something. This is how a direction avoids becoming a pile of effects.

```yaml
restraint: ""
deliberate_sacrifice: ""
deliberately_absent: []
```

### 7. Set the risk budget

Use `balanced` by default. A `bold` move must serve the intended audience effect and preserve a legibility floor. It cannot be bold only because it is visually noisy.

```yaml
risk_budget: safe | balanced | bold
required_risk: ""
legibility_floor: ""
```

### 8. Translate into grammar

Convert the claim into observable rules. Do not write “futuristic” when the real decision is “title runs along a narrow vertical rail and the only saturated color appears when a fact is confirmed.”

```yaml
grammar:
  composition: ""
  scale: ""
  space: ""
  type_behavior: ""
  image_crop: ""
  light_and_color: ""
  material_behavior: ""
  motion_grammar: ""
  interaction_grammar: ""
```

### 9. Attack the default

List the default output inventory for the brief. For every retained default, write the premise it serves, the relationship it changes, and the cost it creates.

```yaml
default_output_inventory:
  - default: ""
    why_it_would_be_flat: ""
    replacement_or_exception: ""
    reason_if_retained: ""
```

### 10. Prototype the proof

Choose the smallest artifact that can prove or falsify the claim:

- web: first viewport, one scroll transition, and one content section;
- motion: rest, anticipation, action, settle, and hold in a 6–10 second proof;
- static visual: key visual at intended scale and one real application;
- PPT: cover or section transition plus one information page;
- detail page: first screen, purchase reason, and one evidence section.

Do not expand the system while the proof still looks generic.

## Direction card minimum

Every direction card must contain these six primitives:

```yaml
point_of_view: "What does this direction believe?"
tension: "What relationship creates energy?"
signature: "What can be remembered and repeated?"
hierarchy: "What overwhelms what?"
restraint: "What is deliberately absent?"
sacrifice: "What is given up for specificity?"
```

A card with only mood, palette, references, and component names is a style description, not a creative direction.

## Reference translation

For each important reference, record:

```yaml
reference:
  source: ""
  attractor: "The specific thing that attracts us"
  relation: "Composition, proportion, crop, space, or rhythm"
  behavior: "How type, material, object, camera, or motion responds"
  transform: "How the relation becomes this project's own"
  forbidden: "Surface details that must not be copied"
```

Use heterogeneous sources when helpful: architecture, editorial design, theatre, photography, industrial objects, film language, science instruments, or craft. Do not assemble a moodboard of similar interface screenshots and call it a visual system.
