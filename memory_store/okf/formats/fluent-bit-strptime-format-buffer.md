---
type: format-family
title: "Fluent Bit Strptime Format Buffer"
description: "Round 36 factual format contract for fluent-bit-strptime-format-buffer."
tags: ["fluent-bit-strptime-format-buffer", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Fluent Bit Strptime Format Buffer

## Round 36 Factual Contract

### Schema / Invariants
- The input is not a standalone date file. It is a fixed two-field harness carrier: the leading region is copied and nul-terminated as the format string, while the final fixed-size tail is copied and nul-terminated as the date/time buffer. Format directives drive all parsing; the data buffer is bounded by the harness-added terminator.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
