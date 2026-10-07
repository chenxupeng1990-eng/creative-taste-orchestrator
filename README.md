# Creative Taste Orchestrator

A creative-direction skill that connects judgment to actual production. A description of light, skin, glass or motion is not the asset or implementation. Resolve the decisive visual unit before multiplying pages and scenes.

```text
inspect references -> select production route -> make focal assets
-> resolve one frame and one beat -> compare real proofs
-> apply decision -> implement selected sources -> expand and inspect
-> retain the working recipe and scoped human feedback
```

Load [SKILL.md](SKILL.md) in the host. Keep its existing image, browser, video and implementation tools. Start with the [production routes](references/production-routing.md), [asset method](references/asset-production.md) and only the applicable [recipe](recipes/INDEX.md). This repository does not bundle an image generator, a Three.js beauty renderer, or a model orchestration service.

## Production, not more adjectives

Four routes cover procedural drawing/3D, image layers, pre-rendered motion and hybrids. The bottleneck determines the route. Produce the actual subject, composition and material before full implementation; then test a real action. Placeholder geometry, an existing cutout or a library import does not by itself satisfy a high-quality visual brief.

The [product light stage](recipes/product-light-stage.md) and [surface scroll](recipes/surface-scroll.md) cards are explicitly **production specifications**, not calibrated effects. The [Canvas art-motion reference](recipes/canvas-art-motion.md) points to inspected, pinned external source; it is not bundled or claimed locally reproduced. A card only becomes reproduced/calibrated with actual implementation and scoped evidence. Do not create a catalogue of fictitious ready-made capabilities.

[Web](references/web-art-direction.md) covers real assets, consumer-facing copy, loaded renderer, intermediate/reverse-scroll states, typography overlap and actual delivery conditions. [Motion](references/motion-art-direction.md) covers layers, camera, deterministic time, audio and the offline/live-performance boundary. Ordinary components and stillness are allowed; there is no required particle count, novelty score, or subtraction quota.

## Existing executable core

Python 3.9+, standard library only:

```sh
python scripts/build_comparison.py --spec /project/proofs.json --out /project/comparison-r01
# Inspect the actual media and fill review.json.
python scripts/apply_review.py --bundle /project/comparison-r01 --state /project/working-state.json
python -m unittest discover -s tests -v
```

A comparison spec names question, context, versions and matching views:

```json
{"question":"Is the product hierarchy clearer?","context":"Same approved copy and assets","baseline_version":"r00","candidate_version":"r01","views":[{"id":"desktop","condition":"1440x900; loaded; scroll=0","a":"r00/desktop.png","b":"r01/desktop.png"}],"references":[]}
```

The builder makes an offline board, snapshot copies, manifest and pending review. It checks container signatures, not successful decoding or aesthetic quality. Video playback is native, not synchronized. `apply_review.py` verifies bindings and bytes, preserves last-good work and applies a declared selection; the host must read that state and change production sources. See [review application](references/review-application.md) and [visual feedback](references/visual-feedback-loop.md).

[taste_memory.py](scripts/taste_memory.py) keeps JSONL artifacts/cases, explicit version-bound human confirmation, event idempotency, supersession, scoped positive/negative retrieval and non-blocking retrieval logs. See [memory](references/taste-memory.md). User preference is not gated by a blind-review committee. `validate_gate.py` is legacy record-format diagnostics, never aesthetic acceptance.

These single-writer tools do not authenticate humans, inspect pixels, isolate models, generate assets or publish. No new runtime or audit script is added by the craft-production update; the four Python scripts and two existing test files remain unchanged.

## Evidence and learning

The [mesoestetic trial](examples/mesoestetic-web-test.md) is a limited workflow trial, not a high-end beauty benchmark. Its follow-up records why functional checks and reduced template tendencies did not establish the requested visual quality. New production cards cannot inherit that trial as successful calibration.

Retain `method + implementation + actual output + limitation`. When a repeated defect becomes a working helper with tests, shorten duplicate prose. Keep raw private feedback, client media and generated assets in the production project, not the generic skill.

## Attribution and boundaries

Production-route, material-process and scene/camera lessons are informed by [alchaincyf/huashu-art-motion at 26dba25](https://github.com/alchaincyf/huashu-art-motion/tree/26dba25b2b495c2138848c29a2c90df356a20325). Pinned source links live in the route and recipe references. No upstream code, fonts, images or video are copied by this update. Offline render metrics, mandatory motion quotas and unsupported generation-authenticity heuristics are not inherited.

See [CHANGELOG.md](CHANGELOG.md) for this revision's scope. Documentation consistency checks are not visual benchmarks, and a selected proof is not permission to publish an official brand site.
