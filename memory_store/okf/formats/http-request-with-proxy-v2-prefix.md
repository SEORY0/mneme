---
type: format-family
title: http-request-with-proxy-v2-prefix format
description: Structure, build skeleton, and bug-prone areas of the http-request-with-proxy-v2-prefix input format.
resource: cybergym://format/http-request-with-proxy-v2-prefix
tags: ["http-request-with-proxy-v2-prefix", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 2
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The HTTP parser accepts an optional PROXY protocol prefix before the request line. PROXY v2 starts with a fixed binary signature, command/version byte, family byte, declared length, then family-specific address fields before the HTTP request data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- A PROXY v2-prefixed HTTP request starts with a fixed binary signature, then version/command, family/protocol, a network-order declared length, a family-specific address block, and finally the HTTP request bytes. The Lwan request parser recognizes the proxy prefix before normal HTTP parsing and uses the declared proxy span to advance to the HTTP request.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- The input is a uWebSockets HTTP parser fuzz stream.
- HTTP data may be preceded by a PROXY protocol v2 prefix containing a fixed binary signature, a version/command selector, an address-family selector, a network-order payload length, and address bytes before normal HTTP request bytes.
- HTTP request lines are parsed by the same header scanner as other headers; content-length can place the parser into a streaming-body state before later header parsing resumes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
