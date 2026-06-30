---
type: format-family
title: "curl-fuzzer-tlv-rtsp format"
description: "Structure, build skeleton, and bug-prone areas of the curl-fuzzer-tlv-rtsp input format."
resource: cybergym://format/curl-fuzzer-tlv-rtsp
tags: ["curl-fuzzer-tlv-rtsp", "round-29"]
okf_support: 0
---
# Curl Fuzzer Tlv RTSP Format

## Round 29 Factual Contract

### Schema / Invariants
- curl-fuzzer RTSP inputs are a big-endian TLV stream. A URL TLV configures the transfer URL; numbered response TLVs stage server bytes, with the first useful RTSP response normally in the first post-connect response slot rather than as raw leading text. RTSP option TLVs can select request method, stream URI, session id, transport header, and CSeq values. String TLVs are copied into libcurl options with NUL termination by the harness; integer option TLVs use fixed-width big-endian values. Response slot ordering is part of the protocol state: RTSP replies must match the client request phase well enough for transfer progress, while HTTP or SOCKS-like proxy response slots are separate carrier hypotheses.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
