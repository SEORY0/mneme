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
- observed: 371 traces; solved: 100 (illustrative — not for ranking)
- top vuln_classes: other (82), heap-buffer-overflow-read (70), use-of-uninitialized-value (55), out-of-bounds-read (39), use-after-free (19), heap-buffer-overflow-write (15), out-of-bounds (14), buffer-overflow (11)
- top input_formats: opentype-font (18), c-blosc2-frame (11), pdf (11), rar5 (9), pe-dotnet (7), tiff (7), jpeg (5), opensc-pkcs15-reader-chunk-stream (4)
- collapsed aliases: construct-and-seed-mutate, construct-hdlc-spinel-and-seed-mutate, construct-seed-mutate, construct-seed-mutate-flow-control, construct-seed-mutate-metadata, construct-then-seed-mutate, construct-then-seed-mutate-then-xref-stream-retarget, regression-seed-mutate, seed-mutate-and-construct, seed-mutate-and-construct-postscript, seed-mutate-and-construct-tiff-ptif, seed-mutate-and-raw-layout-construct, seed-mutate-construct, seed-mutate-dxf-leader, seed-mutate-ftp-wildcard-tlv, seed-mutate-h264-then-mpegvideo-elementary-streams, seed-mutate-image-corpus, seed-mutate-nal-boundary-truncate-selector-mutate, seed-mutate-ncp-state-and-truncated-spinel, seed-mutate-plus-construct, seed-mutate-rar5-fixtures, seed-mutate-tail-flags, seed-mutate-then-construct, seed-mutate-then-construct-encrypted-xpath, seed-mutate-then-metadata-construct, seed-mutate-truncated-obu-header, seed-sweep-seed-mutate-construct
<!-- END observed-census -->
