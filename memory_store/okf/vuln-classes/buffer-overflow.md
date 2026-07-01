---
type: vuln-class
title: buffer overflow
tags: [buffer-overflow]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `buffer-overflow`
- observed: 26 traces; solved: 3 (illustrative — not for ranking)
- top input_formats: pe-dotnet (5), coff-sh-object (1), curl-fuzzer-tlv (1), elf32-arm (1), elf32-relocatable-msp430 (1), gml-graph-text (1), icu-ucasemap-fuzzer-bytes (1), image-metadata (1)
- top harnesses: libfuzzer (12), honggfuzz-wrapper (2), afl-file-wrapper (1), ghostscript-gstoraster-raw-pdf (1), graphicsmagick-mvg-raw-file (1), honggfuzz-libfuzzer-compatible (1), honggfuzz-libfuzzer-wrapper (1), honggfuzz-style-file (1)
- observed strategies: construct (18), seed-mutate (12), other (1)
- collapsed aliases: asn1-oid-encoding-buffer-overflow, buffer-overflow-from-signed-xref-size, buffer-overflow-handling, buffer-overflow-invalid-data, buffer-overflow-or-abort, buffer-overflow-or-allocation-size-error, elf-plt-synthetic-symbol-buffer-overflow, integer-overflow-or-buffer-overflow, renderer-path-buffer-overflow
<!-- END observed-census -->
