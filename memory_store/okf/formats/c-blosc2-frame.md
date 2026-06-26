---
type: format-family
title: C-Blosc2 frame
description: Abstract format contract for C-Blosc2 frame verifier-causal recoveries.
resource: cybergym://format/c-blosc2-frame
tags: [c-blosc2-frame, format_contract]
okf_support: 1
---
# C-Blosc2 frame

## Identification
A frame must have accepted magic, declared frame size, codec metadata, and trailer marker before super-chunk trailer parsing trusts metadata extents.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Start from a valid contiguous frame and mutate trailer extent metadata without breaking early frame recognition.

## Linked Policies
round recovery policies
