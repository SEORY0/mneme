---
type: format-family
title: "Raw Camera Image format"
description: "Round 8 descriptive format facts for raw camera image."
resource: cybergym://format/raw-camera-image
tags: ["raw-camera-image", "round-8"]
okf_support: 1
---
# Raw Camera Image Format

## Round 8 Factual Contract

### Schema / Invariants
- The LibRaw harness needs a recognizable raw camera container such as RAF, CR2, or NEF so open_buffer and unpack reach decoder-specific code. EOF truncation can create generic failures, but the target requires reaching phase-one correction and flat-field handling specifically.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

