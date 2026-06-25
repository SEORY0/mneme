import inspect
from pathlib import Path
from memonaemo import memory_api, stats

STORE = Path(__file__).resolve().parents[1] / "memory_store"

def test_repair_policy_returns_compact_only(tmp_path):
    st = stats.Stats.load(tmp_path / "s.jsonl")
    out = memory_api.get_repair_policy(STORE, st, failure_class="bad_format",
                                       verifier_signal="parser_not_reached")
    # bad-format-repair.md matches bad_format/parser_not_reached — policy MUST be found.
    assert out["policy"] is not None
    # Compact record must have EXACTLY these keys — no extras, no omissions.
    assert set(out["policy"]) == {"name", "policy", "procedure", "negative_memory", "evidence_level"}
    # Full-body marker must not leak into any returned field.
    for val in out["policy"].values():
        assert "## Evidence Shape" not in str(val)

def test_discriminator_evidence_denies_generate_fields():
    # The discriminator surface must never expose OKF/causal/policy content.
    ev = memory_api.get_discriminator_evidence(
        candidate_meta={"id": "c1", "crash_type": "heap-buffer-overflow"},
        verifier_summary={"failure_class": "generic_crash"},
    )
    # Return dict must have EXACTLY these two keys — no more, no less.
    assert set(ev) == {"verifier_summary", "candidate_metadata"}
    # Structural isolation: get_discriminator_evidence must have no OKF-reaching parameters.
    sig = inspect.signature(memory_api.get_discriminator_evidence)
    okf_params = {"store_dir", "store", "okf", "policies"}
    assert not any(name in okf_params for name in sig.parameters), (
        f"get_discriminator_evidence has OKF-reaching parameter(s): "
        f"{set(sig.parameters) & okf_params}"
    )

def test_scope_check_blocks_causal_policy_for_discriminator():
    assert memory_api.scope_check("causal_policy", "memory.get_discriminator_evidence")["visible"] is False
    assert memory_api.scope_check("causal_policy", "memory.get_repair_policy")["visible"] is True

def test_record_proposal_never_writes_okf(tmp_path):
    p = memory_api.record_proposal(run_dir=tmp_path, payload={"failure_class": "bad_format"})
    written = Path(p["proposal_path"])
    assert written.exists()
    # Written path must be under run_dir (tmp_path).
    assert tmp_path in written.resolve().parents
    # Written path must not contain "memory_store" anywhere.
    assert "memory_store" not in str(written.resolve())
    # Hard rule: nothing created under memory_store/okf
    assert not any("okf" in str(x) for x in tmp_path.rglob("*") if "memory_store" in str(x))
