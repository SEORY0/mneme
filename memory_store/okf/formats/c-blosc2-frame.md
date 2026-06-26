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

## Round 6 Factual Contract

### Schema / Invariants
- A c-blosc2 frame has a header, chunk metadata, compressed chunk payloads, and optional trailer metadata. Trailer extent fields are validated against the frame buffer and can steer how much trailing metadata is considered available.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 7 Factual Contract

### Schema / Invariants
- A c-blosc2 frame has a recognizable frame header, declared frame size, compressed chunk metadata and
payloads, plus optional trailer metadata. The target usermeta read derives a trailer offset from
header and compressed-size fields, then reads a trailer usermeta length and copies that many bytes
from the in-memory frame.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
