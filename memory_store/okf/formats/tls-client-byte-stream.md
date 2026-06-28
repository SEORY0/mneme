---
type: format-family
title: tls-client-byte-stream format
description: Structure, build skeleton, and bug-prone areas of the tls-client-byte-stream input format.
resource: cybergym://format/tls-client-byte-stream
tags: [tls-client-byte-stream, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- TLS byte streams are record-framed with content type, protocol version, record length, and record body. A server-side handshake carrier begins with a ClientHello record containing coherent handshake length, version, random, session, cipher-suite, compression, and extension vectors. The target relation is in authenticated record processing after cipher and MAC parameters have been established.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
