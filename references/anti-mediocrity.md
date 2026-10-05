# Diagnose generic or weak work

Use after looking at a real proof. The aim is appropriate, well-executed work—not maximum novelty. A component name, color family, or animation primitive is never sufficient evidence of failure.

## Hard failures versus judgment probes

Hard failures come from the brief: wrong facts, lost required content, unusable controls, illegibility, prohibited assets, identity drift, or an explicit constraint breach. Fix or reject these. The following are diagnostic probes, not universal vetoes:

- **Specificity:** does the content-to-form relationship serve this project, or is it arbitrary styling? Shared grids and common navigation can remain.
- **Hierarchy:** where does attention land, and does that order serve the intended task? Do not demand a giant hero object in every dashboard, form, or information page.
- **Craft:** are typography, spacing, image crop, contrast, material, timing, and sound actually resolved? A promising concept can look cheap through poor execution.
- **Distinctiveness:** is there a useful recognizable relationship, not merely unusual decoration? A logotype or product can legitimately carry identity. Removing it is a probe, not a universal acceptance test.
- **Coherence:** do important elements belong together across states? Repetition may establish a system; forced variation can destroy it.
- **Subtraction or addition:** what would improve if changed? Delete noise, but do not delete necessary content to hit a percentage. Add or refine when something essential is missing.

Dark gradients, glass, bento grids, centered titles, cards, fades, and parallax are neither automatically good nor automatically bad. Diagnose their observed effect in this brief. A sophisticated explanation does not earn a weak effect; a familiar technique does not disqualify a strong one. Do not convert anti-template rules into a new template of giant type, diagonal layouts, and sparse content.

## Compact finding

```yaml
finding:
  category: "direction | craft | asset_content | technical"
  status: "observed_failure | observed_strength | uncertain | not_applicable"
  locator: "actual region, state, or timecode"
  observation: "what is present"
  consequence: "why it matters to this brief"
  proposed_cause: "hypothesis, not fact"
  next_test: "the smallest useful comparison"
```

Keep the one to three findings that change the decision. Include what must be preserved. Use [visual-feedback-loop.md](visual-feedback-loop.md) to compare a repair with the last-good baseline. Do not manufacture a fatal objection for a sound design.

When the user says “丑 / 普通 / 廉价 / 没感觉 / 像模板”, preserve the exact phrase. Do not defend the artifact with its rationale. Inspect whether the failure is the premise, execution, assets, or functionality. “User rejected this artifact” may be known; “user hates gradients forever” is not. Repeated failure calls for diagnosis, not automatic abandonment of the idea.
