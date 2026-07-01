---
type: harness-contract
title: "Afl harness"
description: "Input contract facts for afl."
tags: ["afl", "round-32"]
okf_support: 2
---
# Afl Harness

## Round 32 Input Contract
- The harness is an AFL-style raw-buffer target. It wraps the entire PoC as an in-memory file, installs ReadStat buffer open/read/seek/update handlers, then calls readstat_parse_sas7bdat with no filename and no FuzzedDataProvider split, mode byte, argv file path, or stdin format wrapper.

## Round 32 Format Links
- [[sas7bdat]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The fuzzshark target registers the UDP dissector selected from the ip.proto table as a postdissector and passes the raw input as one packet tvb. Therefore the bytes need to begin with a UDP header; a GSMTAP payload then dispatches to the desired RRC subdissector. There is no FuzzedDataProvider layout.

### Format Links
- [[udp-gsmtap-umts-rrc-per]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
