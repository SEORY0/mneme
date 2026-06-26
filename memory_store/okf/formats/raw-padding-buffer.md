---
type: format-family
title: Raw padding buffer
description: Abstract format contract for Raw padding buffer verifier-causal recoveries.
resource: cybergym://format/raw-padding-buffer
tags: [raw-padding-buffer, format_contract]
okf_support: 1
---
# Raw padding buffer

## Identification
A raw padding checker buffer has no container magic; the acceptance gate is reaching the mode-specific padding scan with a buffer whose semantic content is entirely padding-equivalent.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep the carrier minimal and drive the backward scan invariant, not unrelated decoder state.

## Linked Policies
round recovery policies
