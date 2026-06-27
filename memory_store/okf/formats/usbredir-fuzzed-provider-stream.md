---
type: format-family
title: "usbredir fuzzed provider stream format"
description: "Descriptive format contract facts for usbredir fuzzed provider stream."
tags: ["usbredir-fuzzed-provider-stream", "round-18"]
okf_support: 1
train_only: true
---
# Usbredir Fuzzed Provider Stream Format

## Round 18 Factual Contract

### Schema / Invariants
- usbredir serialized state begins with a magic and length, followed by capability arrays, partial header/data fields, and a count-prefixed list of queued write buffers. The trigger relation is many outstanding queued write buffers during serialization, not malformed state magic alone.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
