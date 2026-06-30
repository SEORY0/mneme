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

## Round 29 Factual Contract

### Schema / Invariants
- gpsd FuzzPacket inputs are raw byte streams that may contain several protocol families. Text packets include NMEA/AIS-style lines and Garmin text; binary packets include DLE-framed families, SiRF/Skytraq-style leaders with embedded lengths and trailers, UBX/Ally/CASIC-style leaders with length and checksum fields, RTCM3 messages with a leader, length, payload, and CRC, GREIS records with ASCII identifiers and hex lengths, and OnCore records with fixed command-specific payload sizes. Many packet families require both a recognizer state and a final checksum or length consistency check before packet acceptance.

### Harness Links
- [[libfuzzer-gpsd-fuzzpacket]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
