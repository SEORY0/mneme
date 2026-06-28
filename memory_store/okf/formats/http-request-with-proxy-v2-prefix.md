---
type: format-family
title: http-request-with-proxy-v2-prefix format
description: Structure, build skeleton, and bug-prone areas of the http-request-with-proxy-v2-prefix input format.
resource: cybergym://format/http-request-with-proxy-v2-prefix
tags: ["http-request-with-proxy-v2-prefix", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The HTTP parser accepts an optional PROXY protocol prefix before the request line. PROXY v2 starts with a fixed binary signature, command/version byte, family byte, declared length, then family-specific address fields before the HTTP request data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
