# Web art direction

Treat a website as an authored scene, editorial system, interactive installation, or product theatre. Do not start from a header, hero, cards, and footer inventory.

## Web contract

```yaml
web_art_direction:
  page_as: editorial_scene | interactive_installation | product_theatre | instrument | archive | other
  opening_scene: ""
  spine: "The relationship that persists while the user scrolls"
  focal_anchor: ""
  supporting_anchor: ""
  quiet_zone: ""
  interaction_verb: reveal | fold | cut | pin | orbit | scan | unfold | other
  section_rhythm: ""
  type_behavior: ""
  surface_behavior: ""
  image_crop_logic: ""
  signature: ""
  responsive_recomposition: ""
  forbidden_defaults: []
```

## Required checks

- **Opening scene:** the first viewport must feel like an authored scene, not a component assembly.
- **Eye path:** name the first, second, and quiet attention zones.
- **Asymmetry or intentional regularity:** state the grid break, offset, crop, or repeated constraint that gives the page its form.
- **Section rhythm:** each section must change at least one of scale, knowledge, spatial depth, pace, or emotional temperature.
- **Responsive recomposition:** mobile is a new composition. Explain what is removed, re-ordered, re-cropped, or turned into an interaction.
- **Motion purpose:** each important movement must reveal, compare, guide, transform, or hand off something. “It feels smoother” is not a purpose.
- **Content reality:** use realistic copy lengths and image ratios before claiming hierarchy.

## Default web failures

Return to art direction when the page is only:

- a centered gradient hero;
- a repeated three-card or four-card grid;
- a collection of glass panels and pills;
- a sequence of sections with identical density;
- a generic icon grid;
- a full-page fade-up animation;
- a desktop layout mechanically stacked on mobile.

These patterns may be retained only when the taste thesis gives them a specific semantic or brand role and the proof makes that role visible.

## Web proof

Before building the full site, inspect:

1. the first viewport at the intended desktop size;
2. one scroll transition that expresses the main interaction verb;
3. one content section with real copy and real asset proportions;
4. the corresponding mobile recomposition.

If these four states do not share a recognizable visual relationship, the system is not ready for expansion.
