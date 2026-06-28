---
type: format-family
title: Openthread Cli Uart Or Ip6 Message format
description: Format contract for openthread-cli-uart-or-ip6-message.
resource: cybergym://format/openthread-cli-uart-or-ip6-message
tags: [openthread-cli-uart-or-ip6-message]
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
- OpenThread CLI input is textual UART command data. CoAP commands can start the service, register resources, set resource content, and send requests with URI, type, payload, and blockwise options. The vulnerable helper encodes uint options by trimming leading zero bytes before appending an option header and value.

### Harness Links
- [[honggfuzz-file]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
