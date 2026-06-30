---
type: format-family
title: "Opcua Binary Message format"
description: "Round 28 descriptive format facts for opcua-binary-message."
resource: cybergym://format/opcua-binary-message
tags: ["opcua-binary-message", "round-28"]
okf_support: 0
---
# Opcua Binary Message Format

## Round 28 Factual Contract

### Schema / Invariants
- The input is a concatenation of complete OPC UA TCP binary chunks. Each chunk carries a message/chunk type, an internal chunk length, secure-channel metadata, request sequencing, and an encoded service NodeId followed by the service request body. Service requests after session creation depend on a valid authentication token; the fuzz build helps by copying the created token into subsequent request headers, so preserving seed chunk structure is more important than rebuilding the protocol from scratch.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
