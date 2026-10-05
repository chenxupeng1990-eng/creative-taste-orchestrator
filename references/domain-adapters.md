# Domain adapters and evidence

The creative method is shared, but the proof and failure modes are medium-specific. Read the relevant adapter before production. A generic checklist cannot judge a web scene, a motion system, a PPT argument, and a detail page with the same evidence.

## Shared artifact manifest

Create a manifest before expensive production and update it for every material revision:

```yaml
artifact_id: ""
version: ""
source: "file, URL, repository revision, or generation job"
tool: ""
render_receipt: "command, job ID, or explicit unavailable reason"
hash_or_snapshot: ""
viewports_or_states: []
timecode_or_coverage: []
domain_links:
  premise_to_assets: []
  assets_to_components_or_shots: []
  components_or_shots_to_applications: []
```

If a field cannot be produced, use `unavailable` with a reason. Do not describe an artifact that was not inspected. A successful render is technical evidence, not creative acceptance.

## Web

Read [web-art-direction.md](web-art-direction.md). Review the first viewport, one scroll transition, one real content section, and the mobile recomposition. Check opening scene, eye path, dominant/supporting/quiet hierarchy, section rhythm, authored typography, image crop, responsive transformation, and motion purpose. A screenshot of one state cannot prove an interaction system.

## Motion and video

Read [motion-art-direction.md](motion-art-direction.md). Compile the chosen direction into a treatment, beat sheet, shot contracts, and a proof render. Review full playback or the largest available excerpt, a contact sheet of rest/turning points/transitions/ending, and timecoded objections. Check subject continuity, camera grammar, light, material, typography, rhythm, holds, and afterimage. If a proof uses only selected stills, label playback coverage incomplete.

## PPT and argument pages

Treat a deck as argument and page rhythm, not a collection of cards. Separate visual KV pages from information-density pages. Review title judgment, evidence order, conclusion hierarchy, chapter transitions, page-to-page spine, real data, and actual 16:9 viewing size. A page that is attractive but has no conclusion or decision role is not complete.

## Detail pages and commerce visuals

Freeze the core purchase reason, decision barrier, evidence order, and brand signature before visual execution. Review first-screen comprehension, product-to-copy relation, proof credibility, content length, image crop, mobile reading, and whether the page could be swapped to another brand without changing its structure. Do not use visual effects to compensate for an unfrozen semantic proposition.

## Brand visual systems

Test the key visual in at least two real contexts: packaging, social, retail, print, live, or other relevant applications. Check whether the signature survives without the original mockup, whether the grammar extends without becoming a template, and whether the brand premise maps to visual behavior rather than only color and logo.

## Cross-domain mapping

When one idea spans media, maintain a traceable mapping:

```yaml
premise: ""
signature_behavior: ""
tokens_or_rules: []
applications:
  web: []
  video: []
  ppt: []
  detail_page: []
  packaging: []
invariants: []
allowed_adaptations: []
failure_cases: []
```

The shared idea must survive translation without forcing identical layouts. If the same asset, motion, or composition is copied mechanically across media, record the contradiction and adapt the behavior.
