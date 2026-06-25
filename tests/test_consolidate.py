"""tests/test_consolidate.py — Task 9: offline, train-only, dry-run consolidation."""
from mneme import consolidate

SPLIT = {"train": ["t-train-1"], "eval": ["t-eval-1"]}


def test_refuses_eval_task():
    r = consolidate.propose({"task_id": "t-eval-1", "solved": True, "poc_path": "/x"}, SPLIT)
    assert getattr(r, "refused", False) is True


def test_refuses_unsolved():
    r = consolidate.propose({"task_id": "t-train-1", "solved": False, "poc_path": "/x"}, SPLIT)
    assert getattr(r, "refused", False) is True


def test_proposal_strips_forbidden_fields(tmp_path):
    # Put real leak tokens into sink_loc — the field that _build_markdown
    # actually renders and passes through redact_for_promotion.
    # arvo:12345 → _RAW_TASK_ID_RE, 0x4012 → _HEX_OFFSET_RE,
    # a1b2c3d4e5f0 → _HEX_CHECKSUM_RE (12 hex chars, ≥8).
    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"),
           "sink_loc": "parse_header at parser.c:128 arvo:12345 0x4012 a1b2c3d4e5f0",
           "vuln_class": "heap-buffer-overflow-write",
           "input_format": "tiff", "harness": "libfuzzer", "failure_class": "wrong_sink"}
    (tmp_path / "p").write_bytes(b"poc")
    p = consolidate.propose(res, SPLIT, out_dir=tmp_path)
    text = p.markdown
    # forbidden tokens gone from the in-memory markdown:
    assert "arvo:12345" not in text
    assert "0x4012" not in text
    assert "a1b2c3d4e5f0" not in text
    # abstract keys survive:
    assert "heap-buffer-overflow-write" in text
    assert "tiff" in text
    assert "libfuzzer" in text
    # the rendered file on disk is also redacted:
    disk_text = p.out_path.read_text()
    assert "arvo:12345" not in disk_text
    assert "0x4012" not in disk_text
    assert "a1b2c3d4e5f0" not in disk_text


def test_dry_run_does_not_touch_okf(tmp_path):
    """consolidate.propose must never mutate memory_store/okf policies."""
    from pathlib import Path
    okf_dir = Path(__file__).resolve().parents[1] / "memory_store" / "okf" / "causal-policies"
    before = {f: f.stat().st_mtime_ns for f in okf_dir.glob("*.md")}

    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"), "vuln_class": "x", "input_format": "y",
           "harness": "z", "failure_class": "no_crash"}
    (tmp_path / "p").write_bytes(b"x")
    p = consolidate.propose(res, SPLIT, out_dir=tmp_path)

    after = {f: f.stat().st_mtime_ns for f in okf_dir.glob("*.md")}
    assert before == after, "consolidation must not mutate memory_store/okf policies"

    # proposal lands under out_dir (tmp_path), never inside memory_store/okf:
    assert p.out_path.parent == tmp_path


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
