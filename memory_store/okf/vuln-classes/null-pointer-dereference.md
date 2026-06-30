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
- observed: 40 traces; solved: 15 (illustrative — not for ranking)
- top input_formats: dxf (2), c-blosc2-frame (1), cff2-opentype-variable-font (1), clamav-scanfile-archive (1), curl-protocol-fuzzer-input (1), dns-message (1), dwg (1), elf (1)
- top harnesses: libfuzzer (24), afl-libfuzzer (1), afl-style-fuzzer (1), honggfuzz-libfuzzer-wrapper (1), honggfuzz-wrapper-svc-dec (1), libfuzzer-fluent-bit-parser-fuzzer (1), libfuzzer-freetype-ftfuzzer (1), libfuzzer-gdal-isce-fuzzer (1)
- observed strategies: construct (31), seed-mutate (8), seed-replay (1), tiny-probe (1)
- collapsed aliases: allocation-failure-null-deref, allocation-failure-null-dereference, dns-srv-owner-name-null-dereference, null-context-or-missing-stream-use, null-deref-or-invalid-access-after-allocation-failure, null-deref-or-invalid-token-metadata, null-dereference, null-dereference-from-xref-off-by-one, null-dereference-or-invalid-buffer-state, null-dereference-or-invalid-enum-use, null-dereference-read, null-dereference-under-oom, null-dereference-write, null-or-stale-pointer-dereference, null-pointer-dereference-or-invalid-pointer-read, null-pointer-dereference-read, string-null-termination, unchecked-return-value-or-null-state
<!-- END observed-census -->
