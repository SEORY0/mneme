---
type: vuln-class
title: out of bounds write
tags: [out-of-bounds-write]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `out-of-bounds-write`
- observed: 19 traces; solved: 8 (illustrative — not for ranking)
- top input_formats: pdf (2), samsung-srw-tiff (2), assimp-model (1), elf-with-msp430-relocation-records (1), ffmpeg-dvbsub-packet-stream (1), gif (1), icu-calendar-fuzz-record-stream (1), jpeg-xl-codestream (1)
- top harnesses: libfuzzer (10), custom (1), libfuzzer-ffmpeg-target-decoder (1), libfuzzer-fuzzed-data-provider-style (1), libfuzzer-ghostscript-gstoraster (1), libfuzzer-gstoraster-stdin (1), libfuzzer-ndpi-process-packet (1), libfuzzer-opensc-pkcs15init (1)
- observed strategies: construct (14), seed-mutate (5)
- collapsed aliases: integer-overflow-to-out-of-bounds-write, out-of-bounds-index-write, out-of-bounds-read-or-write, out-of-bounds-write-or-read, undefined-behavior-out-of-bounds-write
<!-- END observed-census -->
