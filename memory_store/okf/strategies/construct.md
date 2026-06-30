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
- observed: 964 traces; solved: 283 (illustrative — not for ranking)
- top vuln_classes: other (252), heap-buffer-overflow-read (152), use-of-uninitialized-value (124), out-of-bounds-read (85), use-after-free (47), heap-buffer-overflow-write (46), out-of-bounds (39), null-pointer-dereference (25)
- top input_formats: pdf (48), mruby-script (17), json (11), elf (10), mruby-source (10), mvg (8), opensc-virtual-reader-chunk-stream (8), php-script (8)
- collapsed aliases: construct-and-seed-from-geos-cases, construct-and-seed-informed, construct-and-seed-mutate, construct-and-seed-probe, construct-and-seed-sweep, construct-archive-carrier, construct-asn1-and-chunked-reader, construct-asn1-and-reader-chunks, construct-carrier-wrap, construct-cil-policy-text, construct-cli-commands, construct-combined-object, construct-config, construct-disassembler-frame, construct-elf-debug-addr-section, construct-elf-stub, construct-from-assembler-instruction-bytes, construct-from-description, construct-from-repo-examples, construct-geometry-radius, construct-html-allocator-limit, construct-icc-desc-tag, construct-ieee1905-message, construct-ini, construct-json-token-shapes, construct-l2cap-and-udp-encapsulation-probes, construct-long-line, construct-mach-o-headers-and-load-commands, construct-minimal-elf-marker, construct-minimal-shared-string-script, construct-mips-elf-relocation, construct-mruby-block-argument-programs, construct-negative-control, construct-patch-ipc-metadata, construct-pcap-rsh-candidate, construct-pdf-and-postscript-probes, construct-pdf-object-stream, construct-pdf-page-annotation, construct-pdf-render-features, construct-pdf-repair-graph (+34 more)
<!-- END observed-census -->
