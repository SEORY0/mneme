---
type: vuln-class
title: undefined behavior
tags: [undefined-behavior]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `undefined-behavior`
- observed: 19 traces; solved: 12 (illustrative — not for ranking)
- top input_formats: ffmpeg-aac-decoder-packet-stream (2), aac-usac (1), binutils-disassembler-frame (1), bluetooth-hci-uart (1), coap-udp-pdu (1), encoded-image (1), ers-fuzzer-archive (1), file-magic-corpus-directory (1)
- top harnesses: libfuzzer (14), libfuzzer-raw-bytes (2), afl-wrapper (1), libfuzzer-ffmpeg-target-decoder (1), uart-transport-fuzzer (1)
- observed strategies: construct (15), seed-mutate (3), seed-replay (1)
- collapsed aliases: pointer-overflow-undefined-behavior, undefined-behavior-after-parse-failure, undefined-behavior-array-bounds, undefined-behavior-bad-cast, undefined-behavior-callinfo-reallocation, undefined-behavior-function-pointer, undefined-behavior-function-type-mismatch, undefined-behavior-in-debug-format-error-path, undefined-behavior-invalid-downcast, undefined-behavior-invalid-pointer-intermediate, undefined-behavior-negative-vlc-index
<!-- END observed-census -->
