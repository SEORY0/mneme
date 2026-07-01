---
type: harness-contract
title: "Libfuzzer Spng Read harness"
description: "Input contract facts for libfuzzer-spng-read."
tags: ["libfuzzer-spng-read", "round-33"]
okf_support: 1
---
# Libfuzzer Spng Read Harness

## Round 33 Input Contract

### Input Contract
- The libspng read fuzzer passes the entire PoC as a PNG buffer with no leading selector and no FuzzedDataProvider carving. It sets CRC checking on both critical and ancillary chunks, computes the decoded RGBA size, allocates an output buffer, then calls image decode with tRNS, gAMA, and sBIT decode flags enabled.

### Format Links
- [[png]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
