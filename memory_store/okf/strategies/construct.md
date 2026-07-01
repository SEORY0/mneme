---
type: strategy
title: construct strategy
description: What
resource: cybergym://strategy/construct
tags: [construct, format_complex, nested_structures, binary_format]
timestamp: 2026-06-24T00:00:00Z
okf_support: 11
---
## What
Build a structurally-valid input declaratively (`construct` for binary containers, or raw
`struct.pack`/templates for flat/text formats), then violate exactly one field.

## When
No usable seed, and the format is a nested/chunked/box container (PNG/MNG, PDF content streams, …)
where hand-counting offsets is error-prone.

## Steps
1. Declare the skeleton with `construct` (use `Rebuild(Int32xb, len_(this.data))` so lengths auto-compute).
2. `build()` a baseline with every field valid (magic, header, ≥1 record/box/chunk).
3. Change the ONE field that violates the just-added check (short length, oversized index, deep nesting).
4. CRC/checksum fields are usually unchecked → set to 0.
5. Validate locally; iterate with `coverage_check` if the sink is not reached.

## Pitfalls
- Keep the prefix valid — decoders bail on bad magic/first record before reaching the sink.
- Only the violation field should be "wrong"; an over-corrupt input crashes the fix too (score 0).

## Observed
- Support: 11 train-set solves.
- Winning strategies (observed): {'construct': 11}
- Format families (observed): {'chunked-image': 1, 'json': 1, 'cff2-font': 1, 'yara-rules': 1, 'sip-text': 1, 'text-expr': 1, 'media-container': 3, 'md3-model': 1, 'pdf': 1}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, heap-buffer-overflow:WRITE, heap-use-after-free:READ, stack-overflow:?, undefined-behavior:?, use-after-poison:READ, use-of-uninitialized-value:?

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `construct`
- observed: 1189 traces; solved: 447 (illustrative — not for ranking)
- top vuln_classes: other (292), heap-buffer-overflow-read (206), use-of-uninitialized-value (158), out-of-bounds-read (97), heap-buffer-overflow-write (62), use-after-free (53), out-of-bounds (44), null-pointer-dereference (35)
- top input_formats: pdf (61), mruby-script (18), elf (11), json (11), mruby-source (11), mvg (11), php-script (11), opensc-virtual-reader-chunk-stream (8)
- collapsed aliases: construct-allocation-sweep, construct-and-malloc-sweep, construct-and-seed-from-geos-cases, construct-and-seed-informed, construct-and-seed-mutate, construct-and-seed-probe, construct-and-seed-sweep, construct-archive-carrier, construct-asn1-and-chunked-reader, construct-asn1-and-reader-chunks, construct-carrier-wrap, construct-cil-policy-text, construct-cli-command, construct-cli-commands, construct-combined-object, construct-config, construct-corpus-directory-diagnostic-archive-carrier, construct-datasource-wrapped-flac, construct-differential-gated-gc, construct-disassembler-frame, construct-elf-debug-addr-section, construct-elf-dwp, construct-elf-stub, construct-encrypted-xpath, construct-fdp-tail, construct-from-assembler-instruction-bytes, construct-from-description, construct-from-minimal-cil-seed, construct-from-repo-examples, construct-from-valid-seed, construct-geometry-radius, construct-hdlc-spinel, construct-hdlc-spinel-and-seed-mutate, construct-hdlc-spinel-streams, construct-html-allocator-limit, construct-icc-desc-tag, construct-ieee1905-message, construct-ini, construct-jpeg-derived-jxl, construct-json-token-shapes (+69 more)
<!-- END observed-census -->
