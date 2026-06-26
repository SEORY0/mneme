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
