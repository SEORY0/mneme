---
type: vuln-class
title: other
tags: [other]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `other`
- observed: 446 traces; solved: 77 (illustrative — not for ranking)
- top input_formats: pdf (27), mruby-script (10), opentype-font (9), tiff (7), mruby-source (6), upx-packed-elf (6), opensc-virtual-reader-chunk-stream (5), php-script (5)
- top harnesses: libfuzzer (243), honggfuzz (6), libfuzzer-mupdf-pdf-renderer (5), afl-libfuzzer (4), libfuzzer-file-command-wrapper (4), libfuzzer-mruby-load-string (4), afl-file-wrapper (3), libfuzzer-gstoraster (3)
- observed strategies: construct (329), seed-mutate (99), seed-sweep (15), tiny-probe (12), analysis-only (9), seed-replay (8), other (7), fuzzer (1)
- collapsed aliases: adpcm-block-size-validation, algorithmic-complexity, algorithmic-complexity-or-redundant-parse, allocation-failure-invalid-buffer-access, allocation-failure-state-bug, allocation-failure-unchecked-sort, allocation-size-too-big, allocator-failure-state-not-initialized, allocator-metadata-confusion, allocator-state-preservation-bug, alpha-channel-handling-off-target-generic-crash, alpha-plane-copy-crash, api-initialization-error, arithmetic-overflow-to-renderer-crash, asn1-ecdsa-signature-parsing, assertion-abort, assertion-abort-debug-output-amplification, assertion-abort-invalid-datetime, assertion-failure, assertion-failure-in-compressed-raw-decode, assertion-failure-parser-state, assertion-or-bounds-failure-in-decompressor, assertion-or-invalid-extension-handling, atr-list-terminator, attribute-type-invariant-violation, bad-api-argument, bad-elf-dynamic-table-handling, bad-elf-hash-chain, bad-free, bad-transform-unchecked-singular-matrix, behavioral-corruption, behavioral-reference-mismatch, behavioral-truncation, behavioral-truncation-or-parser-target-mismatch, bfd-format-memory-management, bitstream-overflow, buffer-length-validation, buffer-over-read, buffer-under-read, buffer-underflow (+358 more)
<!-- END observed-census -->
