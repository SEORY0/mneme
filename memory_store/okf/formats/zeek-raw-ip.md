---
type: format-family
title: Zeek raw IP fuzzbuffer
description: Abstract format contract for Zeek raw IP fuzzbuffer verifier-causal recoveries.
resource: cybergym://format/zeek-raw-ip
tags: [zeek-raw-ip, format_contract]
okf_support: 1
---
# Zeek raw IP fuzzbuffer

## Identification
Zeek packet fuzzing wraps raw packets in a chunk envelope before protocol dispatch.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Preserve the chunk envelope and IP/UDP dispatch, then mutate tunnel-specific length fields only after the detector is selected.

## Linked Policies
[[zeek-teredo-auth-length-overread]]
