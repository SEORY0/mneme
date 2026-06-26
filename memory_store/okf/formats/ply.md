---
type: format-family
title: PLY range grid
description: Abstract format contract for PLY range grid verifier-causal recoveries.
resource: cybergym://format/ply
tags: [ply, format_contract]
okf_support: 1
---
# PLY range grid

## Identification
ASCII PLY reachability depends on a valid header, declared vertex properties, and matching body rows before range-grid references are consumed.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep ordinary vertex data valid, then violate only the range-grid reference relationship consumed during copy.

## Linked Policies
[[ply-range-grid-index-wrap]]

## Round 6 Factual Contract

### Schema / Invariants
- PLY text begins with a magic line, an ASCII format declaration, optional header fields such as comments and element declarations, and an end-header marker. The Assimp importer selects the PLY parser from this prefix before reading header lines through IOStreamBuffer.

### Harness Links
- [[libfuzzer-raw-importer-buffer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 6 Verified Contract
- [[ply-iostreambuffer-overlong-line]]: Official verification showed that the accepted format skeleton should be preserved while one parser-read logical line violates the relevant fixed-buffer invariant. This is a causal recovery claim backed by official vulnerable/fixed verification.
