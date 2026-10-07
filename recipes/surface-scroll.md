# Surface scroll study

Readiness: `production_spec`. No Three.js skin renderer, texture pack, scientific simulation, or accepted beauty benchmark is supplied. Build the unit in the host's real renderer before promoting this card.

Use when scrolling changes how one surface is observed. If real-time Three.js is requested, implement and inspect that path; an image sequence or video is an explicitly different alternative.

## Inputs

An inspected surface reference, coherent textures/geometry, a selected scale, material/light direction, and the actual explanatory copy. Use [asset-production.md](../references/asset-production.md) to distinguish generated texture illustrations from measured data and to protect product identity. Do not imply ingredient penetration, efficacy or anatomical accuracy without the corresponding support.

## One object, several views

Author one continuous scene. A useful sequence for testing is surface overview -> closer texture observation -> a bounded illustrative layer separation -> readable hold/exit. These are optional beats, not a required biological story. Their progress boundaries come from the content and viewing time, not a universal duration.

For each beat bind the visible change to its producer:

| Visible requirement | Implementation responsibility | Proof |
|---|---|---|
| Fine surface response | Coherent texture scale, normals/roughness, controlled lighting | Same camera with the material change, at intended display size |
| Actual relief or silhouette | Suitable geometry/displacement, not just a flat shaded image | Oblique view showing the required shape |
| Layer separation or cutaway | Explicit mesh/mask relationships and shared coordinates | Intermediate states without gaps, z-fighting, or clipping |
| Scroll focus transfer | Camera/object state plus separate screen-space copy | Forward and reverse traversal, including midpoints |

## State contract, not a new engine

Reuse the project's existing timeline or scene functions. Provide a way to set the same scene to an explicit progress/time state for capture. `scene = evaluate(progress, time, viewport, assets)` describes the contract; it is not a function already bundled here.

Evaluate positions, camera and material parameters from that input, rather than accumulating increments on each frame. Seed procedural variation. Freeze time when comparing the same progress state. User-input smoothing may use delta time, but exact seeking must bypass smoothing so a capture does not depend on the previous scroll path.

Let the browser scroll normally. Derive normalized progress from the section's actual travel; keep pinned content inside a container with enough travel. Do not remove the travel distance to fix overlap and leave the animation permanently at zero. Resize/reflow must recompute the mapping. Keep DOM copy in reserved regions, not on top of a moving mesh without an occlusion plan.

## Proof and acceptance boundary

Inspect start, end, beat boundaries and intermediate states, plus normal-speed forward/back scroll. Exercise resize, rapid scroll, reduced motion, offscreen/resume, and the final packaged entry point. A progress variable changing does not prove pixels changed; compare actual captures or recorded interaction. A zero-length travel range, frozen output, clipped label, obvious state jump, or inaccessible text needs repair before expansion.

Load the chosen engine and its actual assets successfully. Pin the dependency and use the project's bundler/local delivery when appropriate; do not depend on an untested CDN timeout path. Record fallback separately. Reduced-motion and WebGL-unavailable paths preserve readable content, not a false claim that the requested 3D ran.

Measure real-time frame cost on named devices or test environments. Offline 60fps export is not a 60fps interactive performance result. Render when needed, pause offscreen, cap resolution deliberately, and dispose resources using the installed engine's APIs. Relevant primary documentation: [rendering on demand](https://threejs.org/manual/en/rendering-on-demand.html), [material maps](https://threejs.org/docs/pages/MeshStandardMaterial.html), [cleanup](https://threejs.org/manual/en/cleanup.html).

## What to retain

Keep the scene entry, exact asset/config versions, explicit progress checkpoints, a short interaction recording and the highest-impact before/after comparison. Parameter names or unused textures do not establish a reusable surface capability.
