---
type: vuln-class
title: out of bounds
tags: [out-of-bounds]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `out-of-bounds`
- observed: 58 traces; solved: 10 (illustrative — not for ranking)
- top input_formats: aac-usac-mps (2), jpeg (2), rawspeed-decompressor-envelope (2), aac-bitstream (1), ac3 (1), asn1-der-rsa-key (1), bmp (1), cram (1)
- top harnesses: libfuzzer (33), afl-file (2), fuzzshark-ip (2), afl-compatible-raw-import-fuzzer (1), afl-libfuzzer-compatible-raw-stdin (1), afl-libfuzzer-file (1), afl-libfuzzer-wrapper (1), afl-style-file (1)
- observed strategies: construct (40), seed-mutate (14), other (3), seed-replay (2), seed-sweep (1), tiny-probe (1)
- collapsed aliases: axis-index-out-of-bounds, bounds-check, bounds-check-assertion, bounds-check-glyph-closure, bounds-check-logic-error, bounds-check-missing, bounds-check-missing-bitmap-length, bounds-check-missing-header-size, bounds-check-overflow, buffer-overflow-or-allocation-overrun, buffer-overrun, buffered-scanf-overrun, fixed-buffer-format-output-overrun, index-out-of-bounds, integer-overflow-bounds-check, integer-truncation-bounds-check-bypass, jpeg-marker-zero-length-overrun, operand-stack-out-of-bounds, out-of-bounds-access, out-of-bounds-access-from-bad-device-color-state, out-of-bounds-array-access, out-of-bounds-copy, out-of-bounds-index, out-of-bounds-iterator-access, out-of-bounds-pointer-use, out-of-bounds-table-index, planar-image-offset-buffer-overrun, state-stack-bounds-check, undefined-behavior-index-out-of-bounds, undefined-behavior-out-of-bounds, undefined-behavior-out-of-bounds-index, unsigned-integer-underflow-bounds-check, xref-index-out-of-bounds
<!-- END observed-census -->
