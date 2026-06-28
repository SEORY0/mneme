---
type: format-family
title: "Opc Ua Binary Message format"
description: "Descriptive contract facts for Opc Ua Binary Message."
resource: "cybergym://format/opc-ua-binary-message"
tags: ["opc-ua-binary-message", "round-6"]
okf_support: 2
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

## Round 15 Factual Contract

### Schema / Invariants
- The OPC UA binary message corpus contains complete message chunks beginning with an ASCII message
  type and chunk marker, followed by little-endian size/channel fields and service payloads.
  FindServersOnNetwork requests encode scalar request fields followed by an array of capability-filter
  strings.

### Harness Links
- [[libfuzzer-afl]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
