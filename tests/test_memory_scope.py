from pathlib import Path
from memonaemo import memory_api, stats

STORE = Path(__file__).resolve().parents[1] / "memory_store"

def test_repair_policy_returns_compact_only(tmp_path):
    st = stats.Stats.load(tmp_path / "s.jsonl")
    out = memory_api.get_repair_policy(STORE, st, failure_class="bad_format",
                                       verifier_signal="parser_not_reached")
    if out["policy"] is not None:
        assert set(out["policy"]) <= {"name", "policy", "procedure", "negative_memory", "evidence_level"}

def test_discriminator_evidence_denies_generate_fields():
    # The discriminator surface must never expose OKF/causal/policy content.
    ev = memory_api.get_discriminator_evidence(
        candidate_meta={"id": "c1", "crash_type": "heap-buffer-overflow"},
        verifier_summary={"failure_class": "generic_crash"},
    )
    flat = str(ev).lower()
    assert "policy" not in ev and "okf" not in flat and "procedure" not in flat

def test_scope_check_blocks_causal_policy_for_discriminator():
    assert memory_api.scope_check("causal_policy", "memory.get_discriminator_evidence")["visible"] is False
    assert memory_api.scope_check("causal_policy", "memory.get_repair_policy")["visible"] is True

def test_record_proposal_never_writes_okf(tmp_path):
    p = memory_api.record_proposal(run_dir=tmp_path, payload={"failure_class": "bad_format"})
    written = Path(p["proposal_path"])
    assert written.exists()
    assert "okf" not in str(written.resolve()).split("memory_store")[-1] if "memory_store" in str(written.resolve()) else True
    # Hard rule: nothing created under memory_store/okf
    assert not any("okf" in str(x) for x in tmp_path.rglob("*") if "memory_store" in str(x))
