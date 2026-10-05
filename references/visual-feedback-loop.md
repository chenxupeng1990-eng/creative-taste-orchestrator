# Visual feedback loop

Improve the work while changing it is cheap. This is not an aesthetic scoring service. Use the host's actual capture and production tools.

## Reference and question

Inspect a small relevant set of images, page states, or clips. Record only what changes the next proof: source/revision, observed region or timecode, attractor, relation, transformation, forbidden surface copying, and asset usage status. Inspiration is not permission to reuse a source asset. Flag recognizable copied marks or distinctive combinations for human rights review; do not claim legal clearance from a similarity score.

Choose one question. Freeze the factual content, source assets, and viewing conditions. An exploratory direction comparison may change several relationships together; do not call it a causal experiment. A repair should change one main cause or a coherent small group. Neither option should receive better photography or more finished content merely to make it win.

## Actual proof coverage

Web: matching first viewports, a real content section, and critical mobile or interaction states. Hold viewport, loaded fonts/assets, scroll, and animation state constant. Full responsive work checks desktop, an intermediate width, and mobile; capture hover/focus, error/empty, and reduced-motion states only when they exist and matter. Do not invent states to fill a quota.

Video: compare corresponding beats, not blindly equal timecodes after timing edits. Watch normally with sound, then muted. Contact sheets reveal composition, not pacing or audio sync. Inspect frames around disputed cuts/actions. Uniform sampling can miss single-frame errors. Size the proof to the action; 6–10 seconds is an option, not a rule.

Unavailable capture is a declared limitation, not a fabricated screenshot path. Relevant implementation documentation when installed: [Playwright screenshots](https://playwright.dev/python/docs/screenshots), [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html).

## Compare and diagnose

First view A and B without rationale. Record where attention lands and what is unresolved. A same-context pass remains self-review, even with neutral labels. Then compare against the brief and actual references using applicable fit, coherence, hierarchy, distinctiveness, legibility, interaction, and craft axes. Record concrete A/B locators, not a weighted taste score. Use not_observed or not_applicable honestly.

The overall decision may be A, B, tie, neither, or insufficient_evidence. Both mediocre means neither. Missing coverage means insufficient evidence. More novel is not automatically better. Hard requirements cannot be traded for visual drama.

Separate direction failure from poor craft, weak assets/content, and technical defects. State the proposed cause, changed variables, protected strengths, expected visible delta, and rollback condition. Do not replace a good concept because two implementation details failed.

## Execute the decision

Capture -> `build_comparison.py` -> inspect -> fill `review.json` -> `apply_review.py` -> read working state -> implement -> re-render.

See [review-application.md](review-application.md) for the exact contract. The builder snapshots actual local images or clips and hashes the copies. Its pending review is bound to that manifest. Applying a reviewed decision verifies the snapshot bytes and prior baseline, then changes working state. Neither preserves last-good work; tie keeps A. Preserve original sources/tokens/config as well as proof snapshots.

The tools do not authenticate reviewers, inspect pixels, guarantee equal conditions, synchronize video, or publish. Their records include local paths and must not be shared outside the authorized project. A host that ignores working state is not using the execution loop. Formal user approval remains separate from internal selection.
