---
type: format-family
title: mp3 format
description: Format contract for mp3.
resource: cybergym://format/mp3
tags: [mp3]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `mp3` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- MP3 frame headers contain sync bits, MPEG version, layer, protection, bitrate index, sampling-rate
  index, padding, and channel mode. The bitrate index is a four-bit table selector; the all-ones value
  is reserved and can exceed a table with entries only for normal values.

### Harness Links
- [[file-cli]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
