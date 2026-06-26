---
type: format-family
title: Zstd legacy frame
description: Abstract format contract for Zstd legacy frame verifier-causal recoveries.
resource: cybergym://format/zstd-legacy-frame
tags: [zstd-legacy-frame, format_contract]
okf_support: 1
---
# Zstd legacy frame

## Identification
Legacy decompression requires the harness prefix, frame-size scan, block structure, and terminal block marker to agree before literal handling runs.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Preserve the legacy block envelope, then place the boundary violation in the literal span selected by the block mode.

## Linked Policies
round recovery policies

## Round 7 Factual Contract

### Schema / Invariants
- Legacy zstd frames begin with a version-specific magic and then block headers. Compressed blocks
contain a literals sub-block before sequence data. Raw-literals headers encode a literal byte count,
and the vulnerable code path copies literals to an internal fixed-size literal buffer when the
declared raw literal count fits within the compressed block.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
