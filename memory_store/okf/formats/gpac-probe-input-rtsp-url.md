---
type: format-family
title: "Gpac Probe Input Rtsp Url"
description: "Round 19 factual format contract for gpac-probe-input-rtsp-url."
resource: cybergym://format/gpac-probe-input-rtsp-url
tags: ["gpac-probe-input-rtsp-url", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Gpac Probe Input Rtsp Url

## Round 19 Factual Contract

- GPAC probe/analyze consumes raw files and routes by URL strings, container signatures, or elementary-stream signatures. RTSP URL inputs can be recognized directly by the filter graph; SDP-style text requires enough surrounding format recognition to be routed to an SDP/RTSP handler.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
