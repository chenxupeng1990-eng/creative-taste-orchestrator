import base64
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_comparison.py"
SPEC = importlib.util.spec_from_file_location("build_comparison", SCRIPT)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j5N0AAAAASUVORK5CYII=")


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "before.png").write_bytes(PNG)
        (self.root / "after.png").write_bytes(PNG)
        self.spec = {"question": "Is the hierarchy clearer?", "context": "Same copy and viewport",
                     "baseline_version": "r00", "candidate_version": "r01",
                     "views": [{"id": "desktop", "condition": "1440x900, first viewport",
                                "a": "before.png", "b": "after.png"}]}
        self.path = self.root / "spec.json"
        self.output = self.root / "comparison"

    def run_build(self):
        self.path.write_text(json.dumps(self.spec), encoding="utf-8")
        return module.build(self.path, self.output)

    def test_snapshot_hash_and_no_automatic_judgment(self):
        result = self.run_build()
        item = result["views"][0]["a"]
        self.assertEqual(item["sha256"], hashlib.sha256(PNG).hexdigest())
        self.assertEqual((self.output / item["path"]).read_bytes(), PNG)
        review = json.loads((self.output / "review.json").read_text())
        self.assertEqual(review["decision"], "insufficient_evidence")
        self.assertIsNone(review["human_confirmation"])
        self.assertFalse(result["observed_by_builder"])

    def test_existing_directory_is_not_overwritten(self):
        self.output.mkdir()
        sentinel = self.output / "baseline.txt"
        sentinel.write_text("keep")
        with self.assertRaises(FileExistsError):
            self.run_build()
        self.assertEqual(sentinel.read_text(), "keep")

    def test_missing_file_does_not_create_output(self):
        self.spec["views"][0]["b"] = "missing.png"
        with self.assertRaises(ValueError):
            self.run_build()
        self.assertFalse(self.output.exists())

    def test_empty_media_is_rejected(self):
        (self.root / "after.png").write_bytes(b"")
        with self.assertRaises(ValueError):
            self.run_build()

    def test_bad_signature_is_rejected(self):
        (self.root / "after.png").write_text("not an image")
        with self.assertRaises(ValueError):
            self.run_build()

    def test_mixed_image_video_pair_is_rejected(self):
        (self.root / "test.mp4").write_bytes(b"\x00\x00\x00\x18ftypisom0000")
        self.spec["views"][0]["b"] = "test.mp4"
        with self.assertRaisesRegex(ValueError, "both be"):
            self.run_build()

    def test_duplicate_views_are_rejected(self):
        self.spec["views"].append(dict(self.spec["views"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.run_build()

    def test_reference_is_copied(self):
        self.spec["references"] = [{"path": "before.png", "note": "Compare scale, not color"}]
        result = self.run_build()
        self.assertEqual(len(result["references"]), 1)
        self.assertTrue((self.output / result["references"][0]["path"]).is_file())

    def test_html_escapes_untrusted_text(self):
        self.spec["question"] = '<script>alert("x")</script>'
        self.spec["views"][0]["id"] = "<img src=x onerror=alert(1)>"
        self.run_build()
        html = (self.output / "index.html").read_text()
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn("<img src=x", html)

    def test_relative_paths_do_not_depend_on_working_directory(self):
        result = self.run_build()
        self.assertEqual(result["views"][0]["a"]["source"], str(self.root / "before.png"))

    def test_network_urls_are_rejected(self):
        self.spec["views"][0]["a"] = "https://example.invalid/image.png"
        with self.assertRaisesRegex(ValueError, "local captured"):
            self.run_build()

    def test_no_views_is_rejected(self):
        self.spec["views"] = []
        with self.assertRaises(ValueError):
            self.run_build()

    def test_condition_is_required(self):
        self.spec["views"][0].pop("condition")
        with self.assertRaises(ValueError):
            self.run_build()

    def test_partial_failure_cleans_only_new_output(self):
        with patch.object(module, "snapshot", side_effect=OSError("copy failed")):
            with self.assertRaises(OSError):
                self.run_build()
        self.assertFalse(self.output.exists())
        self.assertEqual((self.root / "before.png").read_bytes(), PNG)

    def test_unsupported_active_format_is_rejected(self):
        (self.root / "bad.svg").write_text("<svg></svg>")
        self.spec["views"][0]["a"] = "bad.svg"
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            self.run_build()

    def test_multiple_views_keep_neutral_unique_paths(self):
        self.spec["views"].append({"id": "mobile", "condition": "390x844",
                                   "a": "before.png", "b": "after.png"})
        result = self.run_build()
        self.assertEqual(len(result["views"]), 2)
        self.assertNotEqual(result["views"][0]["a"]["path"], result["views"][1]["a"]["path"])


if __name__ == "__main__":
    unittest.main()
