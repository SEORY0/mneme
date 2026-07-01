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
- observed: 415 traces; solved: 65 (illustrative — not for ranking)
- top input_formats: pdf (24), mruby-script (10), opentype-font (8), tiff (7), upx-packed-elf (6), mruby-source (5), opensc-virtual-reader-chunk-stream (5), rar5 (5)
- top harnesses: libfuzzer (225), honggfuzz (6), libfuzzer-mupdf-pdf-renderer (5), libfuzzer-file-command-wrapper (4), afl-file-wrapper (3), afl-libfuzzer (3), libfuzzer-gstoraster (3), libfuzzer-mruby-load-string (3)
- observed strategies: construct (304), seed-mutate (91), seed-sweep (15), tiny-probe (12), analysis-only (9), other (6), seed-replay (6), fuzzer (1)
- collapsed aliases: adpcm-block-size-validation, algorithmic-complexity, algorithmic-complexity-or-redundant-parse, allocation-failure-invalid-buffer-access, allocation-failure-state-bug, allocation-failure-unchecked-sort, allocation-size-too-big, allocator-failure-state-not-initialized, allocator-metadata-confusion, allocator-state-preservation-bug, alpha-channel-handling-off-target-generic-crash, alpha-plane-copy-crash, api-initialization-error, arithmetic-overflow-to-renderer-crash, asn1-ecdsa-signature-parsing, assertion-abort, assertion-abort-debug-output-amplification, assertion-abort-invalid-datetime, assertion-failure, assertion-failure-in-compressed-raw-decode, assertion-failure-parser-state, assertion-or-bounds-failure-in-decompressor, assertion-or-invalid-extension-handling, atr-list-terminator, attribute-type-invariant-violation, bad-api-argument, bad-elf-dynamic-table-handling, bad-elf-hash-chain, bad-transform-unchecked-singular-matrix, behavioral-corruption, behavioral-reference-mismatch, behavioral-truncation, bfd-format-memory-management, bitstream-overflow, buffer-length-validation, buffer-over-read, buffer-under-read, buffer-underflow, buffer-underread, cff-parser-bounds (+340 more)
<!-- END observed-census -->
