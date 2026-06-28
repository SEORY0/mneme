---
type: format-family
title: ass-subtitle format
description: Format contract for ass-subtitle.
resource: cybergym://format/ass-subtitle
tags: [ass-subtitle]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ass-subtitle` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- ASS input must include recognizable section headers, a style format matching the style record
  fields, an events format, and a dialogue event whose timestamp is rendered by the harness. Empty
  fields are accepted by the parser when the comma-separated field count is preserved.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
