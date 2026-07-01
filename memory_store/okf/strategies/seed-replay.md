---
type: strategy
title: seed replay
tags: [seed-replay]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `seed-replay`
- observed: 30 traces; solved: 9 (illustrative — not for ranking)
- top vuln_classes: use-of-uninitialized-value (9), other (8), heap-buffer-overflow-read (4), out-of-bounds (2), out-of-bounds-read (2), heap-buffer-overflow-write (1), invalid-free (1), null-pointer-dereference (1)
- top input_formats: arrow-ipc-stream (2), opentype-font-subset-input (2), pdf (2), sctp-packet (2), aac-usac (1), aac-usac-mps (1), elf-dwarf-object (1), ffmpeg-wtv (1)
- collapsed aliases: construct-seed-replay, seed-replay-and-construct, seed-replay-and-metadata-mutate, seed-replay-and-trailer-mutation, seed-replay-pkcs15-reader-corpus, seed-replay-raw-samples-with-config-tail, seed-replay-seed-mutate-construct-rebuild
<!-- END observed-census -->
