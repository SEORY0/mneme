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
- observed: 333 traces; solved: 31 (illustrative — not for ranking)
- top input_formats: pdf (19), mruby-script (9), opensc-virtual-reader-chunk-stream (5), opentype-font (5), upx-packed-elf (5), heif-isobmff (4), icc-profile (4), jpeg (4)
- top harnesses: libfuzzer (178), honggfuzz (6), libfuzzer-mupdf-pdf-renderer (4), afl-file-wrapper (3), afl-libfuzzer (3), libfuzzer-file-command-wrapper (3), libfuzzer-gstoraster (3), libfuzzer-mruby-load-string (3)
- observed strategies: construct (242), seed-mutate (60), seed-sweep (11), tiny-probe (11), analysis-only (9), other (6), seed-replay (5), fuzzer (1)
- collapsed aliases: adpcm-block-size-validation, algorithmic-complexity, algorithmic-complexity-or-redundant-parse, allocation-failure-state-bug, allocation-failure-unchecked-sort, allocator-failure-state-not-initialized, allocator-metadata-confusion, alpha-channel-handling-off-target-generic-crash, alpha-plane-copy-crash, api-initialization-error, arithmetic-overflow-to-renderer-crash, asn1-ecdsa-signature-parsing, assertion-failure, assertion-failure-in-compressed-raw-decode, assertion-failure-parser-state, assertion-or-bounds-failure-in-decompressor, assertion-or-invalid-extension-handling, attribute-type-invariant-violation, bad-api-argument, bad-elf-dynamic-table-handling, bad-elf-hash-chain, behavioral-reference-mismatch, behavioral-truncation, bfd-format-memory-management, bitstream-overflow, buffer-length-validation, buffer-over-read, buffer-under-read, buffer-underflow, buffer-underread, cff-parser-bounds, class-permission-verification-crash, cmap-state-split, cmap-value-size-bounds, codegen-stack-state, coff-aarch64-relocation, compile-time-missing-declaration, compressor-optimal-parser-state-bug, container-overflow-write, container-uniqueness-logic-error (+275 more)
<!-- END observed-census -->
