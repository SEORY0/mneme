---
type: format-family
title: "Fluent Bit Http Fuzzer Envelope format"
description: "Descriptive contract facts for fluent-bit-http-fuzzer-envelope."
resource: "cybergym://format/fluent-bit-http-fuzzer-envelope"
tags: ["fluent-bit-http-fuzzer-envelope", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The HTTP client parser expects response headers terminated by a blank line. Chunked decoding requires a transfer-encoding header, then hexadecimal chunk sizes followed by chunk data and line endings. The vulnerable value is the parsed chunk size before it is used for buffer adjustment.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- This input is a fixed carved Fluent Bit HTTP-client harness envelope rather than a raw HTTP request.
- A front selector controls whether a proxy field is present; subsequent fixed-width fields populate URI, method, auth, and size controls before a later fixed-size slice is copied as the response buffer.
- Chunked decoding requires normal HTTP headers ending in an empty line and a transfer-encoding header value that is accepted by a short prefix-style comparison.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
