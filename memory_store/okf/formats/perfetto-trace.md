---
type: format-family
title: "Perfetto Trace format"
description: "Round 8 descriptive format facts for perfetto-trace."
resource: cybergym://format/perfetto-trace
tags: ["perfetto-trace", "round-8"]
okf_support: 1
---
# Perfetto Trace Format

## Round 8 Factual Contract

### Schema / Invariants
- The trace processor expects raw Perfetto trace bytes, typically protobuf-framed trace packets. Invalid protobuf envelopes are accepted as fuzz input but are ignored or rejected without surfacing sanitizer findings.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

