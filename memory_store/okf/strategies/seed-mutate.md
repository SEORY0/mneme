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
- observed: 452 traces; solved: 141 (illustrative — not for ranking)
- top vuln_classes: other (99), heap-buffer-overflow-read (97), use-of-uninitialized-value (60), out-of-bounds-read (44), use-after-free (22), heap-buffer-overflow-write (19), out-of-bounds (14), null-pointer-dereference (13)
- top input_formats: opentype-font (23), c-blosc2-frame (14), rar5 (14), pdf (12), pe-dotnet (11), tiff (8), jpeg (6), opensc-pkcs15-reader-chunk-stream (6)
- collapsed aliases: construct-and-seed-mutate, construct-hdlc-spinel-and-seed-mutate, construct-seed-mutate, construct-seed-mutate-bounded-sweep, construct-seed-mutate-flow-control, construct-seed-mutate-metadata, construct-then-seed-mutate, construct-then-seed-mutate-then-xref-stream-retarget, malformed-seed-mutate, regression-seed-mutate, seed-mutate-and-construct, seed-mutate-and-construct-postscript, seed-mutate-and-construct-tiff-ptif, seed-mutate-and-raw-layout-construct, seed-mutate-construct, seed-mutate-construct-bounded-fuzz, seed-mutate-dxf-leader, seed-mutate-flatbuffer-dictionary-delta, seed-mutate-ftp-wildcard-tlv, seed-mutate-h264-then-mpegvideo-elementary-streams, seed-mutate-image-corpus, seed-mutate-nal-boundary-truncate-selector-mutate, seed-mutate-ncp-state-and-truncated-spinel, seed-mutate-plus-construct, seed-mutate-rar5-fixtures, seed-mutate-rebuilt-directory, seed-mutate-tail-flags, seed-mutate-then-construct, seed-mutate-then-construct-encrypted-xpath, seed-mutate-then-metadata-construct, seed-mutate-then-minimize, seed-mutate-truncated-obu-header, seed-mutate-ttc, seed-replay-seed-mutate-construct-rebuild, seed-sweep-seed-mutate-construct
<!-- END observed-census -->
