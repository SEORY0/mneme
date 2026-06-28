---
type: format-family
title: subrip format
description: Format contract for subrip.
resource: cybergym://format/subrip
tags: [subrip]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `subrip` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- SubRip cues use a numeric cue id, a timestamp range line, one or more text lines, and a blank-line
  cue terminator. The GStreamer parser escapes text, selectively unescapes supported inline tags, and
  then repairs malformed supported closing tags before emitting subtitle text.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
