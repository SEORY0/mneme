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

## Round 22 Factual Contract

### Schema / Invariants
- The active input is raw SIP message text. A request line followed by colon-delimited headers is enough to enter message parsing; Via header bodies use a protocol/transport prefix, host text, optional semicolon parameters, and normally end at a header line terminator.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- SIP messages are text records with a request/status line followed by CRLF-delimited headers. A request needs a method, URI, version, and enough conventional headers to pass early message parsing before optional or malformed trailing headers are examined.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- SIP input starts with a request/status line, required routing headers such as Via, then header fields terminated by an empty line and optional body bytes. Content-Length parsing accepts horizontal whitespace and continuation-line whitespace around numeric text.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 28 Factual Contract

### Schema / Invariants
- SIP messages are ASCII start-line plus CRLF-delimited headers. A Via header carries a protocol/transport prefix followed by a sent-by host and optional port or parameters. Fuzzer inputs can omit the final header terminator, so a final truncated header is still enough to enter header-specific parsing before the buffer boundary is reached.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
