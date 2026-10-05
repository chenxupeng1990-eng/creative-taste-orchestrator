# mesoestetic website trial — 2026-10-05

Real brand front-end trial of the patched skill, using a project-provided photograph of melan tran3x concentrate. The site and local evidence archive were delivered in the conversation; brand image binaries are not embedded in the generic skill repository.

## Brief and facts

The brief is brand identity: make professional skincare roots legible and connect them to home care. Not a drink-led promotion, generic feature grid, invented clinic, or mock checkout. The project narrative remains a proposal, not an official slogan.

Official reference texts: https://www.mesoestetic.com/our-history ; https://www.mesoestetic.com/lines/tran3x ; https://www.mesoestetic.com/professional/melan-tran3x-concentrate.html ; https://www.mesoestetic.com/professional/lines/cosmelan . Official historical/product text was checked; the original project photo supplies the visual product authority. No complete visual capture of the official website is claimed.

## Executed loop

- r00 / A: cooler product-science direction.
- r01 / B: warmer pharmacy/editorial direction, using the same product photograph and copy.
- `build_comparison.py` bundled desktop/mobile A/B captures. A real self-review selected B, while noting that the photo's white rectangle looked pasted onto the scene.
- `apply_review.py` actually wrote working baseline r01.
- r02 repaired the real image silhouette and handheld product/caption overlap without rewriting packaging or changing the creative premise.
- A second bundled comparison against the saved r01 was viewed and applied. Actual working baseline became r02.
- The selected direction was then expanded into the full page: brand origin, professional/home-care tabs, product file dialog, FAQs, sources dialog, and responsive navigation.

## Checks run

42 Python unit tests passed. A mutation that removed all inline image/video markup caused the two new preview tests to fail; the production files were not mutated. Those are markup tests, not video-decoding tests.

The full site was rendered at 1440, 1024, 768, 390 and 360 pixels. At these widths: no horizontal document overflow, no unresolved fragment anchors, all product images loaded with alternate text, and no JavaScript page errors. Tested tab arrow-key behavior, product/source dialogs, Escape and focus return, FAQ keyboard activation, mobile menu open/close, and reduced-motion scrolling. Keyboard focus was visibly styled with a 2px solid outline. Selected solid-color text combinations measured at least 4.96:1; this is not a full accessibility audit.

The environment blocked file/HTTP navigation. Own HTML/CSS/JS and image bytes were inlined and rendered with Chromium `page.set_content`; this is real browser rendering, not an assertion that a hosted URL was tested. External links, deployment, other browser engines, commercial performance and audience response remain outside this test.

Review is same-context self-review, not an isolated reviewer or user-confirmed taste. Working proof selection is not acceptance of the entire website or permission to publish it as the official site. No user preference was confirmed from this internal run.

## Final source hashes

- `index.html`: `ab47fab727406efbcf2631a6e88998ff521dcf3cfad857cc6858ed58851e50d6`
- `style.css`: `e5ef04040b4e71c359c239ae1baf31ec6952f8e244a75a3c6adab8dc8fdf0e4b`
- `app.js`: `9d760feb723ff48857b690d39bdae873a9d0ff5d7a627c7de372ae86f2c3c957`

## Applied baseline snapshot hashes

- r02 / desktop: `933d776299a6a564dd2e63ccf3eacc1b5b5998245614a1874137dc398c222a1a`
- r02 / mobile: `824055326bfdfc7a46d2bfc059e88cb267f14a2ecfb1f82691450933dc6dbf34`
