# Creative Taste Orchestrator

An art-direction skill for making the visible work better—not just making its rationale sound better. This iteration adds a **visual feedback loop** while preserving the taste-first intent.

```text
inspect relevant references
→ form a small creative hypothesis
→ render comparable A/B proofs
→ compare actual work, not explanations
→ repair the highest-impact issue
→ recompare with the last-good baseline
→ expand, then record scoped human feedback
```

## Use

Load `SKILL.md` in your skill-capable agent environment. The host supplies its existing image, browser, video, and production tools. The skill does not bundle a model runner or renderer.

Example task:

> Use $creative-taste-orchestrator to redesign this page. Keep the approved copy and product facts. Inspect the supplied references; make two comparable first-view proofs before building the full page. Compare typography, hierarchy, imagery, and mobile reading. Recommend one, then revise only the highest-impact problem. Show the work, not a long design report.

For a revision, use the existing artifact as A and the proposed change as B. The outcome may be A, B, tie, neither, or insufficient evidence. More dramatic is not automatically better.

## What changed

- References must be actually viewed; their visual relationship is translated, not merely named.
- Real candidate and baseline comparisons happen before broad implementation.
- Direction, craft, assets/content, and technical defects receive different repairs.
- Familiar grids, cards, fades, stillness, and restrained design are allowed when they serve the brief.
- No mandatory risk, fixed subtraction quota, or automatic thesis reset after two failures.
- Truth, required content, accessibility, task completion, and agreed limits remain non-negotiable.
- The user receives artifacts and decisions; detailed working records stay in the project.

## Offline comparison helper

Requires Python 3.9+ and only the standard library. Capture/render your proofs with the host first; then create a JSON spec (paths are relative to that spec):

```json
{
  "question": "Is the revised hierarchy better?",
  "context": "Same product, approved copy, and viewing conditions",
  "baseline_version": "r00",
  "candidate_version": "r01",
  "views": [
    {"id": "desktop", "condition": "1440x900; loaded; scroll=0", "a": "r00/desktop.png", "b": "r01/desktop.png"}
  ],
  "references": []
}
```

```sh
python scripts/build_comparison.py --spec /path/to/proofs.json \
  --out /path/to/project/.creative-taste/comparisons/r01
```

Open the generated `index.html`. It contains A/B media for each matched view and an optional reference section. Review originals at their intended size and write the decision in `review.json`. MP4/WebM clips are supported alongside raster image pairs; videos have native playback controls, not synchronized or frame-accurate playback. Separate extracted frame pairs can supplement clips.

The helper snapshots the local files, calculates SHA-256 hashes of the copies, and refuses to overwrite an existing comparison directory. All judgments start pending. It checks file/container signatures, not successful decoding or visual quality. Verify that media actually loads and plays.

It does **not** take screenshots, generate frames, make aesthetic judgments, verify equal capture conditions, isolate reviewers, authenticate approval, or enforce the full workflow. Its manifest and review template are not automatically wired into the legacy acceptance gate. No aesthetic benchmark improvement is claimed by the tooling tests.

## Reading map

Start with [SKILL.md](SKILL.md) and [visual-feedback-loop.md](references/visual-feedback-loop.md). Add the [web](references/web-art-direction.md), [motion/video](references/motion-art-direction.md), or [other medium](references/domain-adapters.md) adapter. Use the [diagnostic guide](references/anti-mediocrity.md) for weak work and [taste memory](references/taste-memory.md) for scoped feedback. [Examples](references/examples.md) are hypothetical, not validated visual precedents.

## Tests

```sh
python -m unittest discover -s tests -v
```

The comparison tests cover snapshot hashes, pending decisions, missing/empty files, format checks, image/video pairing, references, duplicate views, HTML escaping, relative paths, failure cleanup, and baseline overwrite protection. The existing memory and formal status-gate scripts are unchanged in this iteration.

## Partial adapter synchronization

During this update, the connector blocked replacement of `references/web-art-direction.md` and `references/domain-adapters.md`. Those two remote files remain at their earlier versions; their revised drafts were not published. The core loop, comparison helper, diagnosis guide, motion adapter, examples, and memory protocol were updated. Do not treat this commit as a fully synchronized adapter rewrite.
