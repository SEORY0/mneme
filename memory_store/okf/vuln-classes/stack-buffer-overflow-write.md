---
type: vuln-class
title: stack buffer overflow write
tags: [stack-buffer-overflow-write]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `stack-buffer-overflow-write`
- observed: 41 traces; solved: 28 (illustrative — not for ranking)
- top input_formats: binutils-disassembler-buffer-with-trailer-selector (2), opensc-pkcs15-reader-chunk-stream (2), pdf-with-embedded-type1c-cff-font (2), binutils-disassembler-buffer-with-selector-trailer (1), binutils-disassembler-fuzzer-input (1), config (1), cr3-isobmff-atoms (1), dwg-dxf-json-autodetect (1)
- top harnesses: libfuzzer (25), afl (2), afl-file (1), afl-libfuzzer-file-through-gpac-probe-analyze-filter-graph (1), afl-libfuzzer-wrapper (1), honggfuzz-libfuzzer-compat (1), honggfuzz-libfuzzer-file-input-to-pkcs15-reader (1), honggfuzz-llvmfuzzer (1)
- observed strategies: construct (35), seed-mutate (7)
<!-- END observed-census -->
