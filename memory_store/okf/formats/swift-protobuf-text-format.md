---
type: format-family
title: "Swift Protobuf Text Format"
description: "Round 12 factual format contract for swift-protobuf-text-format."
resource: cybergym://format/swift-protobuf-text-format
tags: ["swift-protobuf-text-format", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Swift Protobuf Text Format

## Round 12 Factual Contract

### Schema / Invariants
- SwiftProtobuf text format accepts numeric field tags and named fields with colon-separated values. Floating values recognize nan/inf/infinity spellings with optional sign. The bug is in optional-infinity scanning, where a leading minus can advance the scanner before a later spelling check fails.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
