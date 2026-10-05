# Creative Taste Orchestrator

A compact creative-direction skill with a real comparison-to-revision loop. It does not manufacture taste scores or treat a completed checklist as good design.

```text
inspect references -> render comparable proofs -> inspect A/B
-> apply the decision -> read the selected state -> revise/expand
-> record explicit human feedback separately
```

Load [SKILL.md](SKILL.md) in the host. Keep its existing image, browser, video, and production tools. Default to two small proofs and targeted refinement rather than a committee report.

## Executable core

Python 3.9+, standard library only:

```sh
python scripts/build_comparison.py --spec /project/proofs.json --out /project/comparison-r01
# Actually inspect the rendered media, then fill review.json.
python scripts/apply_review.py --bundle /project/comparison-r01 --state /project/working-state.json
python -m unittest discover -s tests -v
```

A comparison spec names question, context, baseline_version, candidate_version, and matching views:

```json
{"question":"Is the product hierarchy clearer?","context":"Same approved copy and assets","baseline_version":"r00","candidate_version":"r01","views":[{"id":"desktop","condition":"1440x900; loaded; scroll=0","a":"r00/desktop.png","b":"r01/desktop.png"}],"references":[]}
```

The builder makes an offline media board, immutable snapshot copies, manifest, and pending review. It checks container signatures, not decoding or aesthetic quality. Images and MP4/WebM are supported; videos use native controls, not synchronized playback.

`apply_review.py` verifies review/manifest binding and snapshot bytes. Pending, mismatched, stale, or hard-failing selections cannot promote B. A/tie keep A; neither retains the last-good baseline and requests revision; missing evidence stays pending. Retries are idempotent. The host must read the state and implement the chosen direction. It is working selection, not publication or human approval.

See [review application](references/review-application.md), [visual feedback](references/visual-feedback-loop.md), [web](references/web-art-direction.md), [motion](references/motion-art-direction.md), and [other media](references/domain-adapters.md).

## Human feedback, not a second judging committee

[taste_memory.py](scripts/taste_memory.py) keeps cases and artifacts in JSONL. It removes the unused rules file and fragile derived-index dependency. Confirmation requires an explicit event bound to the reviewed artifact, not a blind-review receipt. Repeated confirmation is idempotent; confirmed supersessions are filtered; exact scope and verdict filters separate relevant positive and negative cases. Optional retrieval-log failure does not prevent reads. See [memory](references/taste-memory.md) for migration and limits.

`validate_gate.py` remains only a legacy record-format diagnostic. Its `record_valid` result never authorizes creative acceptance. It is no longer the iteration path.

All tools assume a single writer. They do not authenticate humans, evaluate pixels, enforce model isolation, classify legal risk, or prevent an agent from editing both evidence and its records. Those concerns require real host permissions and review, not more self-reported fields.

## Regression protection

The test suite covers actual A/B image/video markup, snapshot copies, baseline preservation, decision effects, stale/tampered evidence, idempotency, atomic state replacement, human feedback without blind review, artifact binding, supersession, scoped negatives, and non-blocking retrieval logs. Media markup tests do not replace browser decoding tests.

The mesoestetic website trial is documented in [examples/mesoestetic-web-test.md](examples/mesoestetic-web-test.md). It is a real project trial with self-review, not an independent benchmark or official brand publication. A higher aesthetic score is not claimed from passing software tests.
