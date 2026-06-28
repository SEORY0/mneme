---
type: format-family
title: http-response-stream format
description: "Round 23 descriptive structure and invariant facts for http-response-stream."
resource: cybergym://format/http-response-stream
tags: ["http-response-stream", "round-23"]
okf_support: 1
train_only: true
---
# Http Response Stream Format

## Round 23 Factual Contract

### Schema / Invariants
- The relevant curl path is HTTP over a synthetic server stream. HTTP/2 upgrade handling is normally reached from an HTTP/1.1 response that advertises switching protocols or HTTP/2 settings, after libcurl has prepared an upgrade request.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
