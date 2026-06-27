---
type: format-family
title: sip-message-with-sdp-body format
description: Structure and reachability facts for sip-message-with-sdp-body inputs.
tags: [sip-message-with-sdp-body]
okf_support: 0
---
# Sip Message With Sdp Body Format

## Round 10 Factual Contract

### Schema / Invariants
- The carrier is a complete SIP message with headers, Content-Type selecting SDP, Content-Length matching the body, and an SDP body with session lines and media/attribute lines. SDP parsing is line-oriented and depends on valid v/o/s/t/m lines before attributes are useful.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
