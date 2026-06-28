---
type: vuln-class
title: out of bounds read
tags: [out-of-bounds-read]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `out-of-bounds-read`
- observed: 126 traces; solved: 18 (illustrative — not for ranking)
- top input_formats: pdf (5), ecoff-bfd-object (3), opentype-font (3), fuzzing-datasource-rsa-fields (2), http-request (2), mruby-script (2), opensc-fuzz-reader-chunks (2), openstep-plist (2)
- top harnesses: libfuzzer (83), afl-libfuzzer-wrapper (3), honggfuzz-wrapper (2), afl-compatible-fuzzer (1), afl-file-openjpeg-decompress (1), afl-fuzzshark-ip (1), afl-hb-draw-fuzzer (1), afl-libfuzzer-compatible-raw-file (1)
- observed strategies: construct (84), seed-mutate (34), seed-sweep (6), analysis-only (3), other (2), tiny-probe (2), seed-replay (1)
- collapsed aliases: aac-encoder-quantizer-table-out-of-bounds-read, address-size-overread, bounds-check-missing-read, buffer-overread, buffer-overrun-read, dwarf-line-table-out-of-bounds-read, formatting-out-of-bounds-read, h3-localijtocell-out-of-bounds-read, instruction-buffer-out-of-bounds-read, integer-overflow-out-of-bounds-read, integer-overflow-to-out-of-bounds-read, memory-overread, one-byte-out-of-bounds-read, out-of-bounds-read-before-buffer, out-of-bounds-read-in-ecoff-symbol-table, out-of-bounds-read-or-assertion, out-of-bounds-read-or-divide-by-zero, out-of-bounds-read-or-unbounded-allocation, unaligned-or-overread, unchecked-length-out-of-bounds-read, undefined-behavior-out-of-bounds-read
<!-- END observed-census -->
