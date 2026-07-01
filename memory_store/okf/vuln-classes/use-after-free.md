---
type: vuln-class
title: use after free
tags: [use-after-free]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `use-after-free`
- observed: 77 traces; solved: 20 (illustrative — not for ranking)
- top input_formats: pdf (6), cil-policy-text (4), rar (3), xml (3), html (2), libxml2-valid-fuzzer-envelope (2), opentype-font (2), wpantund-fuzz (2)
- top harnesses: libfuzzer (52), afl-file (2), afl-libfuzzer-file (2), afl (1), afl-file-fuzzer (1), afl-style-file-fuzzer-for-kimgio-karchive (1), honggfuzz-style-libxml2-fuzzer (1), libarchive-fuzzer (1)
- observed strategies: construct (53), seed-mutate (20), seed-sweep (4), analysis-only (2), other (1), seed-replay (1)
- collapsed aliases: double-close-use-after-free, hash-table-use-after-free-or-bucket-key-lifetime, heap-use-after-free, invalid-free-or-use-after-free, memory-management-invalid-free-or-use-after-free, stack-use-after-return, stack-use-after-scope, use-after-free-or-cleanup-state, use-after-free-or-close-order, use-after-free-or-double-release, use-after-free-or-exit-cleanup, use-after-free-or-invalid-reference, use-after-free-or-stale-message-pointer, use-after-scope, use-after-scope-or-stale-stack-reference
<!-- END observed-census -->
