---
type: format-family
title: "Http2 Request Stream"
description: "Round 12 factual format contract for http2-request-stream."
resource: cybergym://format/http2-request-stream
tags: ["http2-request-stream", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Http2 Request Stream

## Round 12 Factual Contract

### Schema / Invariants
- The input is a raw HTTP/2 byte stream delivered as a client connection. A useful carrier begins with the HTTP/2 client preface, then binary HTTP/2 frames such as SETTINGS, PRIORITY, HEADERS, and stream-closing frames. Stream dependency and priority state, not a file header, control reachability.

### Harness Links
- [[afl-libfuzzer-compatible-stdin-harness]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The input is a raw HTTP/2 request stream, not HTTP/1 text. A useful carrier begins with the HTTP/2 client preface and a SETTINGS frame, then binary frame headers and HPACK-encoded request pseudoheaders. The request must omit END_STREAM on HEADERS so a body is expected, and DATA frame ordering controls the state-machine reachability.

### Harness Links
- [[libfuzzer-http2-socket]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
