---
type: format-family
title: "http2-frame-stream format"
description: "Structure and invariants observed for http2-frame-stream."
resource: "cybergym://format/http2-frame-stream"
tags: ["http2-frame-stream", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The input is an HTTP/2 connection byte stream: client preface, frame headers, HPACK header blocks, stream IDs, flags, and DATA frames. To test the described bug, a request must enter the reverse-proxy streaming body path, terminate the request body, then deliver additional DATA on that stream.

### Harness Links
- [[libfuzzer-h2o-http2]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
