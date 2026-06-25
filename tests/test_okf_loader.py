from pathlib import Path
from memonaemo import okf, stats

STORE = Path(__file__).resolve().parents[1] / "memory_store"

def test_load_policies_have_match_keys():
    ps = okf.load_policies(STORE)
    assert ps
    assert any("bad_format" in p.match_keys for p in ps)

def test_compact_record_excludes_full_body():
    ps = okf.load_policies(STORE)
    p = next(p for p in ps if "bad_format" in p.match_keys)
    rec = okf.compact_record(p)
    assert set(rec) <= {"name", "policy", "procedure", "negative_memory", "evidence_level"}
    assert "## Evidence Shape" not in rec.get("policy", "")  # not the raw body

def test_rank_prefers_higher_success_rate(tmp_path):
    st = stats.Stats.load(tmp_path / "s.jsonl")
    ps = okf.load_policies(STORE)
    # Two policies that both match the query; success-rate must dominate text order.
    q = {"failure_class": "bad_format", "verifier_signal": "parser_not_reached"}
    matched = [p for p in ps if okf.matches(p, q)]
    assert matched, "expected at least one matching policy"
    name = matched[0].name
    stats.Stats.record(tmp_path / "s.jsonl", name, success=True)
    st2 = stats.Stats.load(tmp_path / "s.jsonl")
    ranked = okf.rank(ps, q, st2)
    assert ranked[0].name == name

def test_rank_is_not_text_similarity():
    # rank() must not import or use any embedding / vector lib.
    import inspect, memonaemo.okf as m
    src = inspect.getsource(m)
    assert "embedding" not in src.lower() and "cosine" not in src.lower()

def test_mini_yaml_coerces_booleans():
    from memonaemo.okf import _mini_yaml
    out = _mini_yaml("train_only: false\nallowed_scopes: [generate]\nname: foo")
    assert out["train_only"] is False
    assert out["allowed_scopes"] == ["generate"]
    assert out["name"] == "foo"
