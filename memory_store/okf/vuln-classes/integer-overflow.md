---
type: vuln-class
title: integer overflow
tags: [integer-overflow]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `integer-overflow`
- observed: 31 traces; solved: 4 (illustrative — not for ranking)
- top input_formats: aac-loas-latm (2), audio-container (2), sctp-packet (2), bcachefs-filesystem-image (1), blosc2-frame (1), cryptofuzz-binary-operation-stream (1), dwg-r11 (1), elf-with-stabs-debug-sections (1)
- top harnesses: libfuzzer (17), afl-file (1), afl-standalone-loas-decoder (1), afl-stdin-libfuzzer-wrapper (1), afl-style-usrsctp-listen-fuzzer (1), decompress-frame-fuzzer (1), libfuzzer-assimp-importer (1), libfuzzer-cryptofuzz-binary-operation-stream (1)
- observed strategies: construct (22), seed-mutate (11), other (1), seed-sweep (1)
- collapsed aliases: integer-overflow-available-out, integer-overflow-before-decode, integer-overflow-cookie-lifetime-policy-bypass, integer-overflow-length-computation, integer-overflow-or-constant-time-copy-width, integer-overflow-or-pointer-bounds, integer-overflow-or-range-validation, integer-overflow-read, integer-overflow-relocation-bounds, integer-overflow-to-invalid-memory-access, integer-overflow-to-negative-size, integer-overflow-underallocation, integer-overflow-wild-read, signed-integer-overflow, unsigned-integer-overflow
<!-- END observed-census -->
