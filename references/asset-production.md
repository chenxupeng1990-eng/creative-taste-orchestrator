# Asset production: make the visual subject, not a substitute

Use when image or material quality determines the result. An existing product cutout can be useful, but its existence does not prove that the requested hero image has been made. Inspect before deciding to reuse, generate, photograph, retouch, model, or render.

## Asset roles and authority

Separate factual assets (product geometry, packaging, labels, identity, approved claims) from expressive assets (staging, backgrounds, abstract materials, light studies). Preserve the former; create the latter when needed. Generated backgrounds must not be represented as actual factories, microscopy, clinical evidence, or product results. A procedural surface study is an illustration, not measured skin or penetration data.

When packaging must stay exact, composite the verified product/label or use an approved model/texture. Do not ask a generative model to reconstruct unreadable label text and accept the result because the bottle looks attractive. Exact page copy belongs in editable type, not in a generated hero image.

## Build the focal asset

1. Inspect source resolution, viewing scale, crop, silhouette, edge quality, label legibility, material, and light direction.
2. Make an explicit missing-asset list. For each missing item, identify the producer and the observable property it must provide. "Premium serum visual" is not enough: specify the focal angle, reflection, contact shadow, background relationship, and text-safe region.
3. Produce the shared composition frame before requesting separate layers. A blockout may establish positions; it cannot validate photo-real skin, glass, metal, or liquid.
4. Produce only the layers the scene will use. Preserve the original uncropped canvas or record the crop offset, source canvas size, pivot, and scale. Reconstruct the frame from those layers to test registration before animating.
5. Inspect the composite on its actual page background. Check white/green fringes, matte color contamination, contact shadow, perspective, light consistency, and whether the product looks pasted on. An alpha channel does not establish integration.
6. Verify each asset's real consumer and appearance in the delivered artifact. Retain original outputs and the source composite, not only a flattened screenshot.

A short project inventory is sufficient:

```yaml
asset:
  id: "hero-product"
  role: "focal subject"
  source: "original file or actual generation/render receipt"
  file: "existing local asset path"
  state: "planned / produced / inspected / integrated"
  preserved: ["bottle proportions", "label"]
  registration: "uncropped canvas, or crop offset + pivot + source size"
  consumer: "component, scene texture, or compositing layer"
  limitation: "none, or what this asset cannot support"
```

The inventory is consumed by the producer and reviewer. It is not an authorization record. Record actual tool receipts when available; metadata, PNG headers, dimensions, or an absence of editing tags cannot prove that an image was model-generated. Do not describe generated assets that the tool did not return.

## Texture and geometry are different deliverables

A beauty image is not automatically a PBR texture set. Distinguish base color, roughness, normals, displacement/geometry, alpha, and environment lighting when the chosen renderer needs them. Do not relabel a shaded photograph or arbitrary noise as a measured height map. Inspect inferred maps for baked shadows, seams, wrong scale, and inconsistent normals.

In Three.js, normal maps affect lighting rather than the silhouette; displacement affects vertex positions. Choose real geometry or displacement for a requested visible relief/cutaway, and use shading detail where the silhouette need not change. Check the installed version's material and color-space requirements: [MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html).

## Missing capability

Use an available native/connected generation tool when the task needs generated assets; code placeholders are not an equivalent fulfillment. If the needed producer is unavailable or fails, report which asset remains missing. Keep a provisional layout or use an approved alternative only within its stated scope. Do not bury that gap under added animation or claim a fallback as a completed high-end asset pass.
