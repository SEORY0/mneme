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

## Round 4 Verified Contracts
- [[xcoff-archive-short-armap-uninit-count]]: A recognized big archive can enable the 64-bit armap path while the member body is shorter than the initial symbol-count read.

## Round 9 Factual Contract

### Schema / Invariants
- The relevant format is an archive containing a XCOFF archive map.
- The outer archive has a global magic and fixed-width member headers; the vulnerable path is
  deeper, after BFD recognizes the file as an archive and parses the armap member with a symbol
  count and name table.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The big XCOFF archive path starts with a big-archive magic string, then fixed-width decimal archive-header fields for member-table and symbol-table offsets. The symbol-table offset names an archive member header, not the map body. That member header carries decimal size and linkage fields, a decimal name length, optional padded name bytes, an archive-member trailer, and then the armap contents. The armap body begins with a target-endian symbol count followed by per-symbol file offsets and trailing symbol-name strings.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
