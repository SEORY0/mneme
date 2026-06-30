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
- observed: 31 traces; solved: 18 (illustrative — not for ranking)
- top input_formats: binutils-disassembler-fuzzer-input (1), config (1), cr3-isobmff-atoms (1), dwg-dxf-json-autodetect (1), elf-shared-object-with-versioned-dynamic-symbol (1), fio-ini (1), gpac-filelist-url (1), hdf5 (1)
- top harnesses: libfuzzer (20), afl (2), afl-file (1), afl-libfuzzer-file-through-gpac-probe-analyze-filter-graph (1), honggfuzz-libfuzzer-compat (1), honggfuzz-libfuzzer-file-input-to-pkcs15-reader (1), libfuzzer-compatible (1), libfuzzer-ghostscript-gstoraster (1)
- observed strategies: construct (26), seed-mutate (6)
<!-- END observed-census -->
