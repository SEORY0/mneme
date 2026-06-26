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
