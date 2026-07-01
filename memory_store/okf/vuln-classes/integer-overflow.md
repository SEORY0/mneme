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
- observed: 27 traces; solved: 3 (illustrative — not for ranking)
- top input_formats: aac-loas-latm (1), audio-container (1), bcachefs-filesystem-image (1), blosc2-frame (1), dwg-r11 (1), elf-with-stabs-debug-sections (1), exiv2-image-metadata-container (1), fluent-bit-http-fuzzer-envelope (1)
- top harnesses: libfuzzer (16), afl-file (1), afl-stdin-libfuzzer-wrapper (1), decompress-frame-fuzzer (1), libfuzzer-assimp-importer (1), libfuzzer-directory-wrapper (1), libfuzzer-raw-mruby-source (1), libfuzzer-raw-ots-sanitizer (1)
- observed strategies: construct (19), seed-mutate (10), other (1), seed-sweep (1)
- collapsed aliases: integer-overflow-available-out, integer-overflow-before-decode, integer-overflow-length-computation, integer-overflow-or-constant-time-copy-width, integer-overflow-or-pointer-bounds, integer-overflow-read, integer-overflow-relocation-bounds, integer-overflow-to-invalid-memory-access, integer-overflow-to-negative-size, integer-overflow-underallocation, integer-overflow-wild-read, signed-integer-overflow, unsigned-integer-overflow
<!-- END observed-census -->
