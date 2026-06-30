---
type: strategy
title: seed-mutate strategy
description: seed-mutate
resource: cybergym://strategy/seed-mutate
tags: [seed-mutate]
timestamp: 2026-06-24T00:00:00Z
okf_support: 1
---
## What
Strategy `seed-mutate`.

## Observed
- Support: 1 train-set solves.
- Winning strategies (observed): {'seed-mutate': 1}
- Format families (observed): {'media-container': 1}
- Abstract sink shapes (observed): use-of-uninitialized-value:?

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `seed-mutate`
- observed: 301 traces; solved: 58 (illustrative — not for ranking)
- top vuln_classes: other (64), heap-buffer-overflow-read (51), use-of-uninitialized-value (46), out-of-bounds-read (35), use-after-free (17), heap-buffer-overflow-write (12), out-of-bounds (11), buffer-overflow (8)
- top input_formats: opentype-font (13), c-blosc2-frame (9), pdf (8), rar5 (5), tiff (5), pe-dotnet (4), blosc2-frame (3), dwarf-object-debug-file (3)
- collapsed aliases: construct-and-seed-mutate, construct-seed-mutate, construct-then-seed-mutate, regression-seed-mutate, seed-mutate-and-construct, seed-mutate-and-construct-postscript, seed-mutate-construct, seed-mutate-dxf-leader, seed-mutate-h264-then-mpegvideo-elementary-streams, seed-mutate-image-corpus, seed-mutate-rar5-fixtures, seed-mutate-tail-flags, seed-mutate-then-construct, seed-mutate-then-construct-encrypted-xpath
<!-- END observed-census -->
