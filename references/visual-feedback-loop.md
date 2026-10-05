# Visual feedback loop

This is a production loop, not a new aesthetics scoring service. Compare rendered work while changes are cheap, then improve one meaningful relationship at a time.

## 1. Inspect references, not descriptions

Prefer a small set: one reference for the main relationship, optionally one for craft and one scoped counterexample. Inspect the image, page state, or moving excerpt. Do not infer motion from a still, or an entire site from its hero.

For each useful reference, record only what affects the next proof:

```yaml
reference:
  source: "actual locator and revision when known"
  observed_evidence: "screenshot region or timecoded observation"
  attractor: "specific attraction, not a mood adjective"
  relation: "scale / crop / spacing / motion / sound relationship"
  transform: "how that relationship serves our different content"
  forbidden: "distinctive source elements not to copy"
  usage_status: "owned / licensed / inspiration_only / unknown"
```

Inspiration is not permission to reuse a source asset. Flag copied marks, layouts, packaging, or a recognizable combination of distinctive elements for human rights review; do not claim an originality or legal clearance score. Do not put private client material into external comparison services without authorization.

## 2. Hold the comparison conditions constant

Before rendering, declare the question, the content/assets that remain fixed, and the viewing conditions. Preserve source files, tokens/config used, and actual output bytes for each version. Pin a reference revision where available; a local snapshot hash records the bytes, not the truth of the source.

A direction comparison may change composition, sequence, or visual language together; mark it exploratory, not a causal experiment. A repair comparison should change one main cause or a small related group. Equal fidelity means neither candidate gets a finished photograph while the other gets a gray placeholder.

For revisions, compare B to the last-good A, not only the immediately preceding failed draft. On a tie, keep A. Do not overwrite A before a supported promotion.

## 3. Capture the smallest useful evidence

Use the host's available browser, video player, or renderer. Save actual artifacts before creating the board. A screenshot path written in a document is not a screenshot.

For web, start with matching first viewports, one real content section, and the critical interaction or mobile state. Hold viewport, content, font loading, asset loading, scroll position, and animation state constant. Capture focus/error/empty/reduced-motion states when they exist and are in scope; do not invent states or call a static screenshot interaction coverage. For a full responsive delivery, inspect desktop, a narrower intermediate width, and mobile, then expand around any observed breakage.

For motion, compare matching beats, not blindly equal timecodes when edits change timing. Watch clips normally with sound, then muted. Save a contact sheet for composition and key frames around cuts or the disputed action for continuity. Label extraction timestamps and the coverage limit. Uniform sampling can miss a one-frame defect and cannot establish rhythm or audio sync. A short proof is sized to the action; 6–10 seconds is an option, not a required length.

Capture API references, when those tools are installed:
- [Playwright screenshots](https://playwright.dev/python/docs/screenshots)
- [FFmpeg filters: fps, select, showinfo, tile](https://ffmpeg.org/ffmpeg-filters.html)

## 4. Judge in two passes

**First read:** view A and B without their rationale, ranking, model name, or version praise. Name where attention lands, what reads clearly, and what feels unresolved. If the reviewer already knows the generation history, label the pass self-review; neutral labels alone are not blinding. First-view and memorability judgments are reviewer estimates unless tested on actual people.

**Brief-aware comparison:** inspect intent and references, then compare the work. Use concrete locators such as `A / desktop-top / title line 2` or `B / reveal / 00:03.200`. For each applicable axis—fit, coherence, hierarchy, distinctiveness, legibility, interaction, craft—record A, B, tie, or not_observed. Craft includes typography, image treatment, motion timing, materials, and sound as relevant. An axis can be not_applicable with a reason. No weighted overall score.

```yaml
comparison:
  question: "one decision"
  independence: "independent | simulated | unverified"
  hard_failures: []
  axes:
    hierarchy:
      verdict: "A | B | tie | not_observed | not_applicable"
      evidence: ["actual A locator + observation", "actual B locator + observation"]
  decision: "A | B | tie | neither | insufficient_evidence"
  reason: "why this trade-off serves this brief"
  preserve: []
  regressions: []
```

The schema is for concise records, not a replacement for looking. Never fill unobserved axes with favorable judgments. Reject a hard-failing candidate regardless of its novelty. Both mediocre means neither; missing material means insufficient_evidence.

## 5. Turn diagnosis into one revision hypothesis

Distinguish four levels:

- **Direction:** the premise or information relationship is wrong for this brief.
- **Craft:** the relationship is useful, but type, alignment, crop, light, material, camera, timing, or sound is poorly executed.
- **Asset/content:** weak or incorrect imagery, fake evidence, placeholder copy, or an unsuitable content density.
- **Technical:** clipping, failed assets, broken controls, unstable state, or playback faults.

```yaml
next_edit:
  observed_failure: "where and what"
  diagnosis: "proposed cause; not automatically user-confirmed"
  hypothesis: "changing X should visibly improve Y"
  changed_variables: []
  protected_strengths: []
  expected_visible_delta: ""
  rollback_when: ""
```

Correct a material constraint breach first. Otherwise fix the highest-impact perceptual issue. Do not change font, layout, palette, imagery, and motion simultaneously to make the version look busy. Re-render, compare, inspect regressions, and promote or roll back. A new direction is justified by a wrong premise—not by two implementation mistakes.

## 6. Use the local comparison builder

Create `proofs.json` near the captured files. Paths resolve relative to the spec:

```json
{
  "question": "Does B clarify the product before the supporting copy?",
  "context": "Same product and approved copy; A is the last-good baseline",
  "baseline_version": "r00",
  "candidate_version": "r01",
  "views": [
    {"id": "desktop-top", "condition": "1440x900; loaded; scroll=0", "a": "r00/desktop.png", "b": "r01/desktop.png"},
    {"id": "mobile-top", "condition": "390x844; loaded; scroll=0", "a": "r00/mobile.png", "b": "r01/mobile.png"}
  ],
  "references": [{"path": "refs/crop.png", "note": "Compare subject-to-title scale; do not copy the mark"}]
}
```

```sh
python /path/to/creative-taste-orchestrator/scripts/build_comparison.py \
  --spec proofs.json --out .creative-taste/comparisons/r01
```

Open `index.html`, inspect the originals at intended size, and fill `review.json` only after review. For video, pair MP4/WebM clips in a view and add extracted PNG/JPEG frames as separate matched views. References are optional. Multiple views do not prove their conditions match; the reviewer must check.

The helper copies local media, hashes the copies, escapes display text, refuses an existing output directory, and leaves every judgment pending. It accepts common raster images and MP4/WebM container signatures; successful decoding/playback must still be checked. It is not an automatic capture runner, temporal synchronizer, independent reviewer, or aesthetic validator. The output includes source paths; keep it project-local unless sharing is authorized.
