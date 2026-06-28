---
type: format-family
title: "gpsd-raw-packet-stream format"
description: "Structure and invariants observed for gpsd-raw-packet-stream."
resource: "cybergym://format/gpsd-raw-packet-stream"
tags: ["gpsd-raw-packet-stream", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- gpsd packet streams are raw byte streams containing protocol-specific packets. NMEA is line-oriented text with optional checksums; SiRF and RTCM3 use binary leaders and embedded lengths; DLE-framed families use sentinel bytes and may have escaping or trailers.

### Harness Links
- [[libfuzzer-gpsd-fuzzpacket]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
