---
type: format-family
title: "SDP format"
description: "Descriptive contract facts for SDP."
resource: "cybergym://format/sdp"
tags: ["sdp", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- SDP is line-oriented text with session-level fields such as version, origin, session name, timing, connection, media, and attributes. GPAC must first classify the text as SDP before gf_sdp_info_parse tokenizes each line into fixed-size temporary buffers.

### Harness Links
- [[afl-libfuzzer-file-through-gpac-probe-analyze-filter-graph]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 6 Verified Contract
- [[sdp-token-linebuf-overflow]]: Official verification showed that the accepted format skeleton should be preserved while one parser-read logical line violates the relevant fixed-buffer invariant. This is a causal recovery claim backed by official vulnerable/fixed verification.

## Round 11 Factual Contract

### Schema / Invariants
- SDP consists of line-oriented session fields such as version, origin, session name, timing, optional control attributes, media descriptions, RTP map attributes, and fmtp attributes. The target parser is reachable from the RTP SDP filter after the filter receives SDP text and length.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
