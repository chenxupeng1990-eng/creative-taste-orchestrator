# Motion: assets, scene, camera, time

Choose a [production route](production-routing.md) before a renderer. Procedural drawing, generated layers, offline clips and real-time 3D have different strengths. Use [asset-production.md](asset-production.md) for required layers and [recipe index](../recipes/INDEX.md) for actual source references or build procedures. Do not replace a requested photographic/organic asset with arbitrary geometry simply because code is available.

## One frame, then the action

Resolve composition, subject identity, texture, light and type in an actual frame. Then render a short action with enough lead-in and exit to judge it. A static style frame cannot establish timing. Do not give an unfinished direction twenty more shots before its central visual unit works.

A useful scene plan contains only the production-driving choices:

```yaml
scene:
  subject_and_assets: "actual asset files or specific missing inputs"
  world_and_screen_space: "what moves with the camera; what stays readable"
  action: "visible subject change, not an effect name"
  camera_path: "target, framing and entry/exit continuity"
  material_response: "which light/geometry/texture relationship changes"
  timing_and_hold: "time after the information is actually readable"
  sound_cue: "actual cue, or deliberate silence"
  protected_invariants: ["identity, geometry, light, or position"]
```

The plan is a handoff to existing production tools, not a declaration that a scene exists.

## Reproducible state

Prefer the host's explicit-time render/seek facility. The same input time/progress, viewport and assets should reproduce the same intended state in that environment. Seed procedural variation; do not accumulate rotation or motion by frame count. Share time across continuous actions so changing a scene does not restart the same gesture.

Preserve layer canvas size, crop offsets, pivots and scale. Use a shared world/camera to cross views rather than enlarging an unrelated low-resolution screenshot. Distinguish continuous camera motion, object motion, state change and screen-space type. A material-specific movement comes from the object/light relationship, not a random particle overlay.

Rest, anticipation, action, settle and hold are options, not compulsory phases. Stillness, hard cuts and subtle fades may be correct. No minimum number of moving objects or target moving-pixel percentage. Reading time starts after information finishes arriving, not at the beginning of its draw-on effect.

## Playback and performance

Compare corresponding beats when a revision shifts timing. Watch normal-speed playback with sound, then muted. Check entry/exit, focus transfer, acceleration, readable holds, camera scale, subject continuity, light and material consistency. Inspect frames near the disputed cuts or overlaps; retain timestamps. Do not claim auditory review without listening.

An offline renderer can spend longer than a frame duration producing one frame. A 60fps encoded film therefore does not prove a 60fps interactive scene. For a website, measure actual live frame behavior and test reverse scroll, resize, offscreen/resume and reduced motion. For a film, inspect final encoding, audio and the complete relevant sequence.

QA helpers may locate frozen frames, jumps, text bounds, clipping or blank output. Camera shake or noise can inflate frame differences; geometry can obscure text beyond a text-bounds check. Treat metrics as places to look, not an aesthetic score. A contact sheet cannot prove pacing, sound sync, or absence of a single-frame defect.

## Repair and reuse

Separate an incorrect premise from weak assets, poor lighting/material, timing mistakes and runtime defects. Repair one cause, replay its lead-in and exit, compare with the last-good version and use [review application](review-application.md). Repeated visual failure may require returning to asset production or changing the route, not another explanatory paragraph.

After actual production, retain implementation, parameters, evidence and known weakness using [recipe promotion](../recipes/INDEX.md). Do not claim that an external sample or a self-review establishes project-level human approval.
