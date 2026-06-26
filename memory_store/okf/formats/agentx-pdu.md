---
type: format-family
title: "Agentx Pdu"
description: "Round 7 factual format contract for agentx-pdu."
resource: cybergym://format/agentx-pdu
tags: ["agentx-pdu", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Agentx Pdu

## Round 7 Factual Contract

### Schema / Invariants
- AgentX PDUs start with a fixed common header containing version, command, flags, identifiers, and a
body-length field. The body length must match the remaining bytes for the parser to continue. A non-
default-context flag routes the start of the body through the AgentX string decoder before command-
specific fields.

### Harness Links
- [[afl-libfuzzer-raw-bytes]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
