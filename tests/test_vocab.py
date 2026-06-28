"""Tests for mneme.vocab — canonical normalization of trace vuln_class / candidate_family.

The taxonomy census depends on these being deterministic and on collapsing the
free-form trace vocabulary onto stable canonical keys (see
docs/superpowers/specs/2026-06-28-okf-taxonomy-census-design.md).
"""
from mneme.vocab import canonicalize_vuln, canonicalize_strategy


class TestCanonicalizeVuln:
    def test_none_and_blank_are_unknown(self):
        assert canonicalize_vuln(None) == "unknown"
        assert canonicalize_vuln("") == "unknown"
        assert canonicalize_vuln("   ") == "unknown"

    def test_access_read_write_preserved(self):
        # read vs write is a real axis (different sinks) — keep it.
        assert canonicalize_vuln("heap-buffer-overflow-read") == "heap-buffer-overflow-read"
        assert canonicalize_vuln("heap-buffer-overflow-write") == "heap-buffer-overflow-write"
        assert canonicalize_vuln("stack-buffer-overflow-write") == "stack-buffer-overflow-write"

    def test_family_without_access_stays_bare(self):
        assert canonicalize_vuln("heap-buffer-overflow") == "heap-buffer-overflow"

    def test_access_suffix_dropped_when_direction_unknown(self):
        # "-access" carries no read/write direction -> drop it.
        assert canonicalize_vuln("out-of-bounds-access") == "out-of-bounds"

    def test_uaf_synonyms_collapse(self):
        assert canonicalize_vuln("uaf") == "use-after-free"
        assert canonicalize_vuln("use-after-free") == "use-after-free"
        assert canonicalize_vuln("heap-use-after-free") == "use-after-free"
        # access preserved through the synonym map
        assert canonicalize_vuln("heap-use-after-free-read") == "use-after-free-read"

    def test_oob_synonyms_collapse(self):
        assert canonicalize_vuln("oob") == "out-of-bounds"
        assert canonicalize_vuln("out-of-bounds-read") == "out-of-bounds-read"

    def test_null_deref_synonyms_collapse(self):
        assert canonicalize_vuln("null-dereference") == "null-pointer-dereference"
        assert canonicalize_vuln("null-pointer-dereference") == "null-pointer-dereference"

    def test_double_free_synonyms_collapse(self):
        assert canonicalize_vuln("double-free") == "double-free"
        assert canonicalize_vuln("heap-double-free") == "double-free"
        # invalid-free is a distinct class, NOT folded into double-free
        assert canonicalize_vuln("invalid-free") == "invalid-free"

    def test_uninitialized_family_collapses_and_drops_access(self):
        # use-of-uninitialized-value is intrinsically a read; never carries -read.
        assert canonicalize_vuln("use-of-uninitialized-value") == "use-of-uninitialized-value"
        assert canonicalize_vuln("uninitialized-read") == "use-of-uninitialized-value"
        assert canonicalize_vuln("uninitialized-value") == "use-of-uninitialized-value"
        assert canonicalize_vuln("uninitialized-memory-read") == "use-of-uninitialized-value"
        assert canonicalize_vuln("use-of-uninitialized-memory") == "use-of-uninitialized-value"

    def test_registered_keyword_classes(self):
        assert canonicalize_vuln("type-confusion") == "type-confusion"
        assert canonicalize_vuln("Type Confusion") == "type-confusion"
        assert canonicalize_vuln("integer-overflow") == "integer-overflow"

    def test_keyword_match_in_freeform_description(self):
        # hyper-specific descriptions still map by their sanitizer keyword
        assert canonicalize_vuln("aac-encoder-table-out-of-bounds-read") == "out-of-bounds-read"
        assert canonicalize_vuln("buffer-overrun") == "out-of-bounds"
        # terminal sink wins: an int-overflow that lands as an OOB read is OOB read
        assert canonicalize_vuln("integer-overflow-to-out-of-bounds-read") == "out-of-bounds-read"
        # stack scope/return UAF variants fold into use-after-free
        assert canonicalize_vuln("stack-use-after-scope") == "use-after-free"

    def test_unrecognized_goes_to_other_bucket(self):
        # genuine free-form with no sanitizer token -> one shared bucket, not a file each
        assert canonicalize_vuln("adpcm-block-size-validation") == "other"
        assert canonicalize_vuln("invalid-colorspace-validation") == "other"

    def test_slugging_is_applied(self):
        assert canonicalize_vuln("Heap Buffer Overflow READ") == "heap-buffer-overflow-read"


class TestCanonicalizeStrategy:
    def test_none_is_unknown(self):
        assert canonicalize_strategy(None) == ["unknown"]
        assert canonicalize_strategy("") == ["unknown"]

    def test_single_canonical(self):
        assert canonicalize_strategy("construct") == ["construct"]

    def test_underscore_normalized(self):
        assert canonicalize_strategy("seed_mutate") == ["seed-mutate"]
        assert canonicalize_strategy("seed_sweep") == ["seed-sweep"]

    def test_compound_splits_into_multiple_tags(self):
        assert canonicalize_strategy("seed_mutate_and_construct") == ["construct", "seed-mutate"]
        assert canonicalize_strategy("construct|seed_mutate") == ["construct", "seed-mutate"]
        assert canonicalize_strategy("seed_mutate+construct") == ["construct", "seed-mutate"]

    def test_recon_alias(self):
        assert canonicalize_strategy("recon_only") == ["analysis-only"]
        assert canonicalize_strategy("analysis_only") == ["analysis-only"]

    def test_freeform_construct_variant_matches_construct(self):
        assert canonicalize_strategy("construct_tiff_minimal_extra_alpha") == ["construct"]

    def test_smoke_aliases_to_tiny_probe(self):
        assert canonicalize_strategy("smoke") == ["tiny-probe"]

    def test_unmatched_goes_to_other(self):
        assert canonicalize_strategy("raw-cli-then-ipv6-payloads") == ["other"]

    def test_result_order_is_deterministic(self):
        # same multiset of tags regardless of input ordering
        assert canonicalize_strategy("construct_and_seed_mutate") == ["construct", "seed-mutate"]
