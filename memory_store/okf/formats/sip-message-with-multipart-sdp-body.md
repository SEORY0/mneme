---
type: format-family
title: "SIP Message With Multipart Sdp Body"
description: "Round 19 factual format contract for sip-message-with-multipart-sdp-body."
resource: cybergym://format/sip-message-with-multipart-sdp-body
tags: ["sip-message-with-multipart-sdp-body", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# SIP Message With Multipart Sdp Body

## Round 19 Factual Contract

- The input is a SIP request with RFC-style headers and a body selected by Content-Type and Content-Length. For multipart bodies, the boundary parameter from Content-Type controls delimiter discovery. Each part begins after a delimiter line, carries its own part headers, and the SDP part must contain session lines such as version, origin, connection, timing, media, and attributes.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
