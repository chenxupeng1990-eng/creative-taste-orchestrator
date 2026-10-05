# Domain adapters and evidence

The deliberation method is global. The artifact, proof, and failure modes are domain-specific.

## Artifact manifest

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

If a field cannot be produced, set it to `unavailable` with a reason. Do not fill it with a guessed path or a description of an artifact that was not inspected.

## Video and motion

Compile the chosen direction into a treatment, beat sheet, causal storyboard, shot contracts, and a render/review plan. Every shot should identify timing, subject, framing, action, camera or motion, graphic role, transition, and continuity requirements.

Review with:

- full-film playback or the largest available excerpt;
- contact sheets covering opening, turning points, lyric or narration entrances, transitions, and ending;
- timecoded objections tied to visible states;
- continuity checks for subject, material, light, typography, and recurring motifs;
- a before/after render when a revision changes the creative read.

Record frame or timecode coverage in the artifact manifest. If the review uses only selected stills, label playback coverage as incomplete.

Motion must serve a beat, lyric, event, hierarchy change, or state change. A successful render or frame-rate check is technical evidence only.

## Websites and interactive products

Compile the direction into information architecture, page or screen states, component rules, content hierarchy, responsive behavior, and interaction contracts. Specify the entry state, user trigger, visible response, and recovery or exit state for important interactions.

Review with:

- desktop and mobile screenshots or a live prototype;
- first-load, scroll, hover, focus, error, empty, and reduced-motion states where relevant;
- a first-time-user walkthrough with no design-history explanation;
- checks for repeated layout families, generic cards, weak hierarchy, fake content, and unmotivated animation;
- evidence that the visual system survives content and viewport changes.

Record first-load, scroll, hover/focus, error/empty, mobile, and reduced-motion coverage in the manifest when those states are in scope. A screenshot of one state cannot prove the interaction system.

## Brand visual systems

Compile the direction into a positioning statement, visual grammar, key visual, material/color/type rules, and application family. Test the idea in at least two real contexts rather than judging a single hero image.

Review with:

- the key visual at intended viewing scale;
- packaging, social, print, retail, or other relevant applications;
- small-size and low-quality reproduction;
- whether the signature survives without the original presentation mockup;
- whether the rules are extensible without becoming a template.

Map the brand premise to the key visual, then to packaging, social, retail, or other applications. A single hero mockup cannot prove system consistency.

## Copy, campaign, and other creative work

Use the same panel and decision record. Treat the artifact as the exact copy, storyboard, prototype, script, layout, or campaign mockup. Review comprehension, voice, distinctiveness, audience response, channel behavior, and production constraints with evidence appropriate to the medium.

## Cross-domain system mapping

When one idea spans multiple media, maintain a traceable mapping:

```yaml
premise: ""
signature_behavior: ""
tokens_or_rules: []
applications:
  web: []
  video: []
  packaging: []
  social: []
invariants: []
allowed_adaptations: []
failure_cases: []
```

The mapping proves that a shared idea survives translation without forcing identical layouts. It also makes a cross-domain contradiction visible to the head director.

## Shared review rubric

Use hard gates for explicit requirements and a short set of soft axes for comparison:

- intent fidelity;
- specificity and reference distance;
- coherence across elements and states;
- audience legibility;
- material or medium behavior;
- emotional or cultural effect;
- feasibility and extension.

Do not collapse these into a universal aesthetic number. A review must say what is wrong, where it is visible, why it matters, and what change would test the diagnosis. If a gate has no owner, pass condition, and required evidence, it is a preference or an open question, not a gate.
