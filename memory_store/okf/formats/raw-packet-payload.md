---
type: format-family
title: Raw Packet Payload format
description: Format contract for raw-packet-payload.
resource: cybergym://format/raw-packet-payload
tags: [raw-packet-payload]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The active nDPI process-packet target treats the entire input as one packet payload. Protocol detectors call bounded substring helpers over payload slices such as HTTP headers, NATS control lines, BitTorrent handshakes, and other application data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
