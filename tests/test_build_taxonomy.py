"""Offline tests for scripts/learning/build_taxonomy.py — the deterministic
taxonomy census that fills okf/vuln-classes and okf/strategies from traces.

No docker / network / model. Operates on a tmp okf + tmp traces.
See docs/superpowers/specs/2026-06-28-okf-taxonomy-census-design.md.
"""
import importlib
import json
import sys
from pathlib import Path

SCRIPTS_LEARNING = Path(__file__).resolve().parents[1] / "scripts" / "learning"
sys.path.insert(0, str(SCRIPTS_LEARNING))
bt = importlib.import_module("build_taxonomy")


def _trace(d: Path, name: str, **fields):
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{name}.json").write_text(json.dumps(fields))


def _make_traces(learning: Path):
    r1 = learning / "round-1" / "traces"
    _trace(r1, "a", vuln_class="heap-buffer-overflow-read", solved=True,
           input_format="tiff", harness="libfuzzer", candidate_family="construct")
    _trace(r1, "b", vuln_class="use-after-free", solved=False,
           input_format="pdf", harness="libfuzzer", candidate_family="seed_mutate")
    _trace(r1, "c", vuln_class="heap-use-after-free", solved=True,
           input_format="pdf", harness="afl", candidate_family="seed_mutate_and_construct")
    # an unregistered class — must still get a file (passthrough)
    _trace(r1, "d", vuln_class="type-confusion", solved=False,
           input_format="json", harness="afl", candidate_family="construct")


class TestAggregate:
    def test_synonyms_collapse_and_count(self, tmp_path):
        _make_traces(tmp_path)
        traces = list(bt.iter_traces(tmp_path))
        vuln, strat = bt.aggregate(traces)
        # use-after-free and heap-use-after-free fold into one canonical key
        assert vuln["use-after-free"]["count"] == 2
        assert vuln["use-after-free"]["solved"] == 1
        assert vuln["heap-buffer-overflow-read"]["count"] == 1
        assert "type-confusion" in vuln  # unregistered passthrough
        # compound strategy contributed to both construct and seed-mutate
        assert strat["construct"]["count"] == 3   # a, c, d
        assert strat["seed-mutate"]["count"] == 2  # b, c

    def test_malformed_trace_skipped(self, tmp_path):
        d = tmp_path / "round-1" / "traces"
        d.mkdir(parents=True)
        (d / "bad.json").write_text("{not json")
        _trace(d, "ok", vuln_class="integer-overflow", solved=True)
        traces = list(bt.iter_traces(tmp_path))
        vuln, _ = bt.aggregate(traces)
        assert vuln["integer-overflow"]["count"] == 1
        assert len(traces) == 1

    def test_through_round_filters(self, tmp_path):
        _trace(tmp_path / "round-1" / "traces", "x", vuln_class="integer-overflow")
        _trace(tmp_path / "round-2" / "traces", "y", vuln_class="type-confusion")
        assert len(list(bt.iter_traces(tmp_path, through_round=1))) == 1
        assert len(list(bt.iter_traces(tmp_path, through_round=2))) == 2


class TestUpsert:
    def _stats(self, tmp_path):
        _make_traces(tmp_path)
        return bt.aggregate(list(bt.iter_traces(tmp_path)))

    def test_new_file_created_with_census(self, tmp_path):
        vuln, _ = self._stats(tmp_path)
        f = tmp_path / "okf" / "vuln-classes" / "type-confusion.md"
        bt.upsert_census(f, "vuln-class", "type-confusion", vuln["type-confusion"])
        text = f.read_text()
        assert bt.BEGIN in text and bt.END in text
        assert "type-confusion" in text

    def test_idempotent(self, tmp_path):
        vuln, _ = self._stats(tmp_path)
        f = tmp_path / "okf" / "vuln-classes" / "use-after-free.md"
        bt.upsert_census(f, "vuln-class", "use-after-free", vuln["use-after-free"])
        first = f.read_text()
        bt.upsert_census(f, "vuln-class", "use-after-free", vuln["use-after-free"])
        assert f.read_text() == first

    def test_hand_authored_prose_outside_markers_preserved(self, tmp_path):
        vuln, _ = self._stats(tmp_path)
        f = tmp_path / "okf" / "vuln-classes" / "heap-buffer-overflow-read.md"
        f.parent.mkdir(parents=True)
        seed = (
            "---\ntype: vuln-class\ntitle: Heap-buffer-overflow READ\n---\n"
            "# Schema\n- Sink: precious hand-authored recipe that must survive.\n"
        )
        f.write_text(seed)
        bt.upsert_census(f, "vuln-class", "heap-buffer-overflow-read",
                         vuln["heap-buffer-overflow-read"])
        text = f.read_text()
        assert "precious hand-authored recipe that must survive." in text
        assert bt.BEGIN in text
        # second run still preserves prose and stays idempotent
        once = text
        bt.upsert_census(f, "vuln-class", "heap-buffer-overflow-read",
                         vuln["heap-buffer-overflow-read"])
        assert f.read_text() == once


class TestIndex:
    def test_index_sections_refreshed(self, tmp_path):
        idx = tmp_path / "index.md"
        idx.write_text(
            "# header\n\n## vuln-classes\n- [old](vuln-classes/old.md)\n\n"
            "## formats\n- [keepme](formats/keepme.md)\n\n"
            "## strategies\n- [oldstrat](strategies/oldstrat.md)\n\n"
            "## causal-policies\n- [policy](causal-policies/p.md)\n"
        )
        bt.update_index(idx, ["heap-buffer-overflow-read", "type-confusion"],
                        ["construct", "seed-mutate"])
        text = idx.read_text()
        # vuln-classes refreshed
        assert "[heap-buffer-overflow-read](vuln-classes/heap-buffer-overflow-read.md)" in text
        assert "old.md" not in text
        # strategies refreshed
        assert "[seed-mutate](strategies/seed-mutate.md)" in text
        assert "oldstrat" not in text
        # untouched sections preserved
        assert "[keepme](formats/keepme.md)" in text
        assert "[policy](causal-policies/p.md)" in text
