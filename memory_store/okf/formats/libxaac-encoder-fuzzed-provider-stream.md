---
type: format-family
title: "libxaac encoder fuzzed provider stream format"
description: "Descriptive format contract facts for libxaac encoder fuzzed provider stream."
tags: ["libxaac-encoder-fuzzed-provider-stream", "round-18"]
okf_support: 1
train_only: true
---
# Libxaac Encoder Fuzzed Provider Stream Format

## Round 18 Factual Contract

### Schema / Invariants
- The target is not an AAC file container; it is a provider-driven encoder configuration and sample stream. The bug relation is a scalefactor-band form-factor value becoming zero before the encoder's scalefactor estimation loop consumes it.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
