# Production routing: choose how the image will exist

Use before full page or film implementation, not before every small edit. Choose by the hardest visible requirement and actual host capabilities. Do not equate "code can draw it" with "code can draw it well enough".

| Route | Appropriate bottleneck | Make first | Execution |
|---|---|---|---|
| Procedural drawing / real-time 3D | Geometric systems, diagrams, authored paint, controllable geometry or lighting | A rendered frame with the real material/geometry method | Existing Canvas, SVG, WebGL/Three.js, or other project renderer |
| Image/layer-led | Photography, complex organic appearance, products, characters, fine material detail | An inspected composition and registered layers | Photography, approved assets, image generation, retouching, then DOM/canvas compositing |
| Pre-rendered motion | Organic motion or costly shading where fixed playback is acceptable | A short clip with readable entry, action, and exit | Video generation or offline rendering; code handles placement/playback |
| Hybrid | Image quality plus precise camera, labels, transitions, or interactivity | The focal asset plus one working interactive or temporal beat | Generated/photographed assets and a real scene share composition and timing |

These are routes, not a quality ladder. A simple static page may need no new imagery. A photo-real hero normally cannot be settled by a gray primitive. A requested real-time 3D feature cannot be marked complete by playing a video of one.

## One compact production decision

Record only what will change execution:

```yaml
production:
  medium: "web / video / static / other"
  hardest_visible_requirement: "what must actually be seen"
  route: "procedural / layers / prerendered / hybrid"
  producer: "available tool, existing skill, or implementation entry"
  inputs: ["approved product, content, reference, or required missing asset"]
  first_output: "specific frame, layer set, or short action"
  required_effect: "what this renderer must visibly do"
  fallback: "usable alternative, with the unmet requirement named"
```

This is a handoff, not a compulsory schema or another status service. Check that the tool exists before naming it as the producer. Never claim generation, asset availability, or a separate agent from a plan alone. Follow host permissions for external services and paid generation. Do not re-upload private project assets to a new provider merely to avoid a failed call.

## Make one unit end to end

A production unit is a hero plus its transition, a material study, or a short scene—not the whole site. Complete:

`reference observation -> asset/look development -> real frame -> real action -> visible comparison -> selected source snapshot`

A weak material calls for a material study; a weak asset calls for a new asset. Adding more sections or effects does not solve either. Do not make users approve prose instead of showing the unit when tools can produce it.

## Readiness is scoped

- A composition blockout permits layout decisions, not image-quality claims.
- A resolved still permits frame-level decisions, not motion acceptance.
- A working beat permits a motion/interaction decision, not acceptance of the full site.
- A fallback permits access to content, not substitution of a required effect.

Check load success, actual rendering and visible behavior separately. If a library cannot load, retain the diagnostic and resolve the dependency or report the limitation. Do not count a different canvas path as proof that Three.js ran.

## Delegation when available

Keep one coordinator. An asset producer receives the approved frame, subject invariants, layer roles, output size, and registration requirements. A scene implementer receives actual assets and the state/camera contract. A reviewer receives actual output and the brief, not a persuasive production history. Missing delegation means self-review, not simulated independence presented as fact.

## Why these routes

Method inspiration: [huashu-art-motion, four production routes](https://github.com/alchaincyf/huashu-art-motion/blob/26dba25b2b495c2138848c29a2c90df356a20325/references/03-%E4%B8%80%E5%B8%A7%E5%85%88%E8%A1%8C%E5%9B%9B%E6%9D%A1%E8%B7%AF%E7%BA%BF.md). The routing and wording here are adapted for this project's broader media, not a copied renderer. Do not inherit fixed candidate counts, motion quotas, unsupported generation-authenticity heuristics, or offline performance assumptions.
