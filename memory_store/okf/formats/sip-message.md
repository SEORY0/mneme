---
type: format-family
title: "Sip Message"
description: "Round 7 factual format contract for sip-message."
resource: cybergym://format/sip-message
tags: ["sip-message", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Sip Message

## Round 7 Factual Contract

### Schema / Invariants
- SIP messages are line-oriented and OpenSIPS permits leading CR/LF pairs before the request or status
line. This parser path scans those leading separators before normal message-line parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 8 Factual Contract

### Schema / Invariants
- A useful input must be a SIP request/status message with a valid start line and CRLF-delimited headers. The target parameter parser is entered from a To header after a URI/body has ended and a semicolon starts parameters; tag and general parameters have distinct parser states.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
