import base64
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_comparison as board
import apply_review as apply
import taste_memory as memory
PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j5N0AAAAASUVORK5CYII=')

class MediaParser(HTMLParser):
    def __init__(self): super().__init__(); self.media = []
    def handle_starttag(self, tag, attrs):
        if tag in {'img', 'source'}: self.media.append((tag, dict(attrs).get('src')))

class FlowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.state = self.root / 'state.json'
        (self.root/'a.png').write_bytes(PNG); (self.root/'b.png').write_bytes(PNG+b'B')
        self.spec={'question':'Which hierarchy?', 'context':'Same brief', 'baseline_version':'a1','candidate_version':'b1',
                   'views':[{'id':'desktop','condition':'1440x900','a':'a.png','b':'b.png'}]}
        self.bundle=self.make_bundle('comparison')
    def make_bundle(self,name):
        spec=self.root/(name+'.json'); spec.write_text(json.dumps(self.spec))
        out=self.root/name; board.build(spec,out); return out
    def review(self, decision='B', **changes):
        p=self.bundle/'review.json'; r=json.loads(p.read_text())
        r.update(status='reviewed', reviewer_id='self-review', decision=decision, reason='The title reads before supporting text',
                 observations=[{'side':s,'view_id':'desktop','observation':f'{s}: visible hierarchy'} for s in ['A','B']])
        r.update(changes); p.write_text(json.dumps(r)); return r
    def test_real_image_tags_point_to_both_snapshots(self):
        p=MediaParser(); p.feed((self.bundle/'index.html').read_text())
        m=json.loads((self.bundle/'manifest.json').read_text())
        self.assertIn(('img',m['views'][0]['a']['path']),p.media)
        self.assertIn(('img',m['views'][0]['b']['path']),p.media)
    def test_real_video_tags_point_to_both_snapshots(self):
        (self.root/'a.mp4').write_bytes(b'\x00\x00\x00\x18ftypisom0000')
        (self.root/'b.mp4').write_bytes(b'\x00\x00\x00\x18ftypisom0001')
        self.spec['views'][0].update(a='a.mp4',b='b.mp4'); out=self.make_bundle('video')
        p=MediaParser(); p.feed((out/'index.html').read_text())
        self.assertEqual(len([x for x in p.media if x[0]=='source']),2)
        self.assertIn('<video controls', (out/'index.html').read_text())
    def test_pending_review_cannot_promote(self):
        with self.assertRaises(ValueError): apply.apply(self.bundle,self.state)
        self.assertFalse(self.state.exists())
    def test_b_promotes_exact_snapshot(self):
        self.review(); s=apply.apply(self.bundle,self.state)
        self.assertEqual(s['baseline']['version'],'b1'); self.assertEqual(s['status'],'working_selected')
        self.assertEqual(s['baseline']['views']['desktop']['sha256'],hashlib.sha256(PNG+b'B').hexdigest())
    def test_tie_keeps_a(self):
        self.review('tie'); self.assertEqual(apply.apply(self.bundle,self.state)['baseline']['version'],'a1')
    def test_neither_creates_revision_not_baseline(self):
        self.review('neither',status='revision_required',hard_failures=['unreadable'])
        s=apply.apply(self.bundle,self.state); self.assertIsNone(s['baseline']); self.assertEqual(s['status'],'revision_required')
    def test_neither_preserves_last_good(self):
        self.review('A'); old=apply.apply(self.bundle,self.state)['baseline']
        self.bundle=self.make_bundle('second'); self.review('neither',status='revision_required')
        self.assertEqual(apply.apply(self.bundle,self.state)['baseline'],old)
    def test_insufficient_evidence_does_not_promote(self):
        self.review('insufficient_evidence'); self.assertIsNone(apply.apply(self.bundle,self.state)['baseline'])
    def test_hard_failures_block_even_b(self):
        self.review(hard_failures=['broken text'])
        with self.assertRaises(ValueError): apply.apply(self.bundle,self.state)
    def test_changed_snapshot_blocked(self):
        self.review(); (self.bundle/'media/v001-b.png').write_bytes(PNG)
        with self.assertRaisesRegex(ValueError,'Snapshot changed'): apply.apply(self.bundle,self.state)
    def test_wrong_manifest_blocked(self):
        self.review(manifest_sha256='fake')
        with self.assertRaisesRegex(ValueError,'bound'): apply.apply(self.bundle,self.state)
    def test_missing_observation_blocked(self):
        self.review(observations=[])
        with self.assertRaisesRegex(ValueError,'observation'): apply.apply(self.bundle,self.state)
    def test_apply_retry_idempotent(self):
        self.review(); a=apply.apply(self.bundle,self.state); b=apply.apply(self.bundle,self.state)
        self.assertEqual(a,b); self.assertEqual(len(b['history']),1)
    def test_rewriting_applied_review_blocked(self):
        self.review(); apply.apply(self.bundle,self.state); self.review('A')
        with self.assertRaisesRegex(ValueError,'already applied'): apply.apply(self.bundle,self.state)
    def test_stale_baseline_blocked(self):
        self.review(); apply.apply(self.bundle,self.state); self.bundle=self.make_bundle('second'); self.review()
        with self.assertRaisesRegex(ValueError,'Stale'): apply.apply(self.bundle,self.state)
    def test_atomic_failure_keeps_existing_state(self):
        self.review('A'); apply.apply(self.bundle,self.state); old=self.state.read_bytes()
        self.bundle=self.make_bundle('second'); self.review()
        with patch.object(apply.os,'replace',side_effect=OSError('disk')):
            with self.assertRaises(OSError): apply.apply(self.bundle,self.state)
        self.assertEqual(old,self.state.read_bytes())

class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.root=Path(self.tmp.name)
        for i in ('a','b'):
            memory.append_artifact(self.root,{'artifact_id':i,'version':'v1','source':i+'.png','tool':'browser',
                                           'render_receipt':'capture','hash_or_snapshot':i*64,'owner':'maker'})
        self.case={'case_id':'pending','domain':'web','intent':'Brand identity','writer':'model', 'source_revision':'v1',
                   'artifact_id':'a','artifact_version':'v1','artifact_evidence':[{'locator':'a/header','observation':'Too generic'}],
                   'verdict':'rejected','scope':'mesoestetic-web','review':{'blind_to_history':False},
                   'human_rationale':'普通','rule_candidate':'unconfirmed diagnosis'}
        memory.append_case(self.root,self.case)
    def confirm(self,case='pending',event='user-event',art='a'):
        return memory.confirm_case(self.root,case,'user',event,'user_message',art)
    def test_user_feedback_needs_no_blind_review(self):
        c=self.confirm(); self.assertEqual(c['state'],'confirmed'); self.assertEqual(c['verdict'],'rejected')
    def test_repeated_event_idempotent(self):
        self.assertEqual(self.confirm()['case_id'],self.confirm()['case_id'])
        self.assertEqual(len(memory.search_cases(self.root,'','web',{'confirmed'})),1)
    def test_event_reuse_for_other_case_blocked(self):
        self.confirm(); other=dict(self.case,case_id='other'); memory.append_case(self.root,other)
        with self.assertRaisesRegex(ValueError,'already used'): self.confirm('other')
    def test_artifact_switch_blocked(self):
        with self.assertRaisesRegex(ValueError,'bind'): self.confirm(art='b')
    def test_explicit_scope_and_negative_role(self):
        self.confirm(); results=memory.search_cases(self.root,'','web',{'confirmed'},'mesoestetic-web','rejected')
        self.assertEqual(results[0]['retrieval_role'],'negative')
        self.assertEqual(memory.search_cases(self.root,'','web',{'confirmed'},'other'),[])
    def test_pending_excluded(self): self.assertEqual(memory.search_cases(self.root,'','web',{'confirmed'}),[])
    def test_confirmed_supersession_filters_old(self):
        old=self.confirm(); newer=dict(self.case,case_id='replace',supersedes=[old['case_id']])
        memory.append_case(self.root,newer)
        # Explicit feedback revision is immutable and carries a new event.
        new=self.confirm('replace','event2')
        # Link its pending record to the old confirmed decision: transitive projection.
        found=memory.search_cases(self.root,'','web',{'confirmed'})
        self.assertEqual([x['case_id'] for x in found],[new['case_id']])
    def test_index_and_rules_not_created(self):
        self.assertFalse((self.root/'index.json').exists()); self.assertFalse((self.root/'rules.jsonl').exists())
    def test_old_corrupt_index_does_not_break_primary_records(self):
        (self.root/'index.json').write_text('old corrupt cache'); self.confirm()
        self.assertEqual(memory.validate_store(self.root),[])
    def test_audit_write_failure_does_not_break_search(self):
        self.confirm()
        with patch.object(memory,'write_json_atomic',side_effect=OSError('read-only')):
            self.assertEqual(len(memory.search_cases(self.root,'','web',{'confirmed'})),1)

if __name__=='__main__': unittest.main()
