---
type: vuln-class
title: null pointer dereference
tags: [null-pointer-dereference]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `null-pointer-dereference`
- observed: 55 traces; solved: 26 (illustrative — not for ranking)
- top input_formats: dxf (3), git-patch (2), c-blosc2-frame (1), cff2-opentype-variable-font (1), cil-policy-text (1), clamav-scanfile-archive (1), curl-protocol-fuzzer-input (1), dns-message (1)
- top harnesses: libfuzzer (34), afl-libfuzzer (1), afl-libfuzzer-compatible-fuzzshark-ip (1), afl-style-fuzzer (1), honggfuzz-libfuzzer-wrapper (1), honggfuzz-wrapper-svc-dec (1), libfuzzer-assimp-fuzzer (1), libfuzzer-execute (1)
- observed strategies: construct (42), seed-mutate (13), seed-replay (1), tiny-probe (1)
- collapsed aliases: allocation-failure-null-deref, allocation-failure-null-dereference, dns-srv-owner-name-null-dereference, null-context-or-missing-stream-use, null-deref-or-invalid-access-after-allocation-failure, null-deref-or-invalid-token-metadata, null-deref-read, null-dereference, null-dereference-from-xref-off-by-one, null-dereference-or-invalid-buffer-state, null-dereference-or-invalid-enum-use, null-dereference-or-stale-list-read, null-dereference-read, null-dereference-under-oom, null-dereference-write, null-or-stale-pointer-dereference, null-pointer-dereference-or-invalid-pointer-read, null-pointer-dereference-or-tokenizer-crash, null-pointer-dereference-read, offset-null-check-missing, string-null-termination, unchecked-return-value-or-null-state, undefined-behavior-null-pointer-load
<!-- END observed-census -->
