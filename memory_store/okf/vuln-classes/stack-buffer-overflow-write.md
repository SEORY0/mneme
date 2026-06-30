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
- observed: 34 traces; solved: 21 (illustrative — not for ranking)
- top input_formats: pdf-with-embedded-type1c-cff-font (2), binutils-disassembler-fuzzer-input (1), config (1), cr3-isobmff-atoms (1), dwg-dxf-json-autodetect (1), elf-shared-object-with-versioned-dynamic-symbol (1), fio-ini (1), fuzzed-dataprovider-wide-uri (1)
- top harnesses: libfuzzer (23), afl (2), afl-file (1), afl-libfuzzer-file-through-gpac-probe-analyze-filter-graph (1), honggfuzz-libfuzzer-compat (1), honggfuzz-libfuzzer-file-input-to-pkcs15-reader (1), libfuzzer-compatible (1), libfuzzer-ghostscript-gstoraster (1)
- observed strategies: construct (29), seed-mutate (6)
<!-- END observed-census -->
