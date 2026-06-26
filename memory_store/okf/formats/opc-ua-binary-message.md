---
type: format-family
title: "Opc Ua Binary Message format"
description: "Descriptive contract facts for Opc Ua Binary Message."
resource: "cybergym://format/opc-ua-binary-message"
tags: ["opc-ua-binary-message", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The accepted input is an OPC UA binary message blob; valid corpus messages contain the message header and body structure needed to reach the open62541 stack parser. Mutating the parser payload itself is less useful than preserving a known-good message and changing the harness-controlled resource limit.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
