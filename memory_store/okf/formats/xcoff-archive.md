---
type: format-family
title: XCOFF archive format
description: Format contract for BFD XCOFF archives and archive-map members.
resource: cybergym://format/xcoff-archive
tags: [xcoff, archive, bfd, armap]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
The carrier is an archive envelope recognized by BFD as XCOFF. Member headers and archive-map metadata must be coherent enough for member enumeration and armap reading.

## Invariants
- Top-level recognition is mandatory; generic archive shells are usually rejected too early.
- The armap member can be validly referenced while its body is too short for reader assumptions.
- Mutate the symbol-map member body rather than all archive members at once.
