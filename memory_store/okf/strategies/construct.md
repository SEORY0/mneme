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
- observed: 1305 traces; solved: 524 (illustrative — not for ranking)
- top vuln_classes: other (312), heap-buffer-overflow-read (235), use-of-uninitialized-value (178), out-of-bounds-read (100), heap-buffer-overflow-write (69), use-after-free (56), out-of-bounds (45), null-pointer-dereference (39)
- top input_formats: pdf (64), mruby-script (18), json (13), mruby-source (13), php-script (13), elf (11), mvg (11), opensc-pkcs15-reader-chunk-stream (10)
- collapsed aliases: construct-after-fuzz-probe, construct-allocation-sweep, construct-and-bounded-valid-spix-search, construct-and-malloc-sweep, construct-and-seed-from-geos-cases, construct-and-seed-informed, construct-and-seed-mutate, construct-and-seed-probe, construct-and-seed-sweep, construct-archive-carrier, construct-asn1-and-chunked-reader, construct-asn1-and-reader-chunks, construct-boundary, construct-carrier-wrap, construct-cil-policy-text, construct-cli-command, construct-cli-commands, construct-combined-object, construct-config, construct-corpus-directory-diagnostic-archive-carrier, construct-datasource-wrapped-flac, construct-differential-gated-gc, construct-direct-reader-chunks, construct-disassembler-frame, construct-elf-debug-addr-section, construct-elf-dwp, construct-elf-stub, construct-encrypted-xpath, construct-fdp-tail, construct-from-assembler-instruction-bytes, construct-from-description, construct-from-minimal-cil-seed, construct-from-repo-examples, construct-from-seed, construct-from-valid-seed, construct-geometry-radius, construct-hdlc-spinel, construct-hdlc-spinel-and-seed-mutate, construct-hdlc-spinel-streams, construct-html-allocator-limit (+81 more)
<!-- END observed-census -->
