# Canvas art-motion: pinned external reference

Readiness: `external_source`. The source-level method and selected implementations were inspected. This update does not install the project, rerender its films, inherit the author's quality scores, or bundle its assets/fonts.

Upstream: `alchaincyf/huashu-art-motion`, commit `26dba25b2b495c2138848c29a2c90df356a20325`.

## Actual starting points

- [Style author contract](https://github.com/alchaincyf/huashu-art-motion/blob/26dba25b2b495c2138848c29a2c90df356a20325/references/08-%E9%A3%8E%E6%A0%BC%E4%BD%9C%E8%80%85%E8%A7%84%E8%8C%83.md): select a close implementation, understand physical drawing processes, and keep scene registration consistent.
- [Post-impressionist scene](https://github.com/alchaincyf/huashu-art-motion/blob/26dba25b2b495c2138848c29a2c90df356a20325/scripts/engine/scenes/09_postimp.js): separate base, regional stroke fields, props, characters, and contour recovery. Inspect actual `PAINT.strokes` calls instead of adding generic noise over a flat image.
- [Camera library](https://github.com/alchaincyf/huashu-art-motion/blob/26dba25b2b495c2138848c29a2c90df356a20325/scripts/engine/lib/camera.js): world/screen mapping, target anchoring, keyframed camera paths and layer relationships. This is Canvas camera math, not a Three.js renderer.
- [Frame renderer](https://github.com/alchaincyf/huashu-art-motion/blob/26dba25b2b495c2138848c29a2c90df356a20325/scripts/engine/render.py): explicit-time frame capture and offline video encoding.
- [Visual QA](https://github.com/alchaincyf/huashu-art-motion/blob/26dba25b2b495c2138848c29a2c90df356a20325/scripts/qa.py): sampled frame differences, jump/stillness clues and text-framing instrumentation. Read its blind spots and thresholds before use.

## Adaptation procedure

Fetch the pinned source through an available repository tool. Read dependency/license notices and the selected scene's actual imports before copying a coherent subset. Do not run arbitrary setup code or silently import external private assets. Keep upstream notices when copying source.

For an offline art-animation task, first reproduce one still from an appropriate scene, then one short moving beat. Change the subject and visual relationships for the actual brief, not just the scene title. Use generated/approved layers when procedural painting cannot represent the required subject. Keep continuous actions on a shared timeline so a transition does not restart the same gesture.

Feed the actual output into the existing comparison loop. A working import is not a reproduced effect; a rendered clip is not automatically good. Record local output and limitations before upgrading readiness.

## Do not transfer the wrong assumptions

Do not import the whole art-history engine for a small beauty website. Procedural paint, generated layers, and real-time PBR solve different problems. Do not copy its art-style motion quota into a restrained campaign, or treat an offline frame-render time as a browser frame budget. Do not use whole-frame motion area as an aesthetic score: camera movement, grain, flashes, or particles can move pixels without improving the subject.

The useful reusable unit is `method + implementation + visible result + known weakness`. The external library is an optional production starting point, not a replacement for this skill or proof that high-end beauty production is solved.
