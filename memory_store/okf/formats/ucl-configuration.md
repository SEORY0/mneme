---
type: format-family
title: "UCL Configuration format"
description: "Round 8 descriptive format facts for ucl configuration."
resource: cybergym://format/ucl-configuration
tags: ["ucl-configuration", "round-8"]
okf_support: 1
---
# UCL Configuration Format

## Round 8 Factual Contract

### Schema / Invariants
- UCL supports ordinary assignments and dot-prefixed built-in macros. Ordinary scalar values may avoid variable expansion when no variables are registered, while macro values go through the expansion routine directly. Multiline-string syntax reaches a separate parser path and can produce off-target crashes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

