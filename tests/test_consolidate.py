"""tests/test_consolidate.py — Task 9: offline, train-only, dry-run consolidation."""
from memonaemo import consolidate

SPLIT = {"train": ["t-train-1"], "eval": ["t-eval-1"]}


def test_refuses_eval_task():
    r = consolidate.propose({"task_id": "t-eval-1", "solved": True, "poc_path": "/x"}, SPLIT)
    assert getattr(r, "refused", False) is True


def test_refuses_unsolved():
    r = consolidate.propose({"task_id": "t-train-1", "solved": False, "poc_path": "/x"}, SPLIT)
    assert getattr(r, "refused", False) is True


def test_proposal_strips_forbidden_fields(tmp_path):
    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"), "sink_loc": "parser.c:128",
           "offset": "0x4012", "checksum": "a1b2c3d4e5", "vuln_class": "heap-buffer-overflow-write",
           "input_format": "tiff", "harness": "libfuzzer", "failure_class": "wrong_sink"}
    (tmp_path / "p").write_bytes(b"poc")
    p = consolidate.propose(res, SPLIT)
    text = p.markdown
    assert "t-train-1" not in text and "0x4012" not in text and "a1b2c3d4e5" not in text
    assert "heap-buffer-overflow-write" in text and "tiff" in text  # abstract keys kept


def test_dry_run_does_not_touch_okf(tmp_path, monkeypatch):
    # propose must never write under memory_store/okf
    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"), "vuln_class": "x", "input_format": "y",
           "harness": "z", "failure_class": "no_crash"}
    (tmp_path / "p").write_bytes(b"x")
    consolidate.propose(res, SPLIT, out_dir=tmp_path)
    assert not (tmp_path / "okf").exists()


def test_specialist_non_approving_blocks_proposal(tmp_path):
    """A non-approving specialist verdict marks the proposal blocked."""
    class FakeSpecialist:
        def review_consolidation(self, payload):
            return {"approved": False, "notes": "needs more evidence"}

    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"), "vuln_class": "heap-uaf", "input_format": "png",
           "harness": "libfuzzer", "failure_class": "generic_crash"}
    (tmp_path / "p").write_bytes(b"poc")
    p = consolidate.propose(res, SPLIT, specialist=FakeSpecialist())
    assert p.status == "blocked"
    assert p.specialist_verdict["approved"] is False
