---
type: harness-contract
title: "Honggfuzz Libfuzzer File Input To Pkcs15 Reader harness"
description: "Input contract facts for Honggfuzz Libfuzzer File Input To Pkcs15 Reader."
tags: ["honggfuzz-libfuzzer-file-input-to-pkcs15-reader", "round-6"]
okf_support: 1
---
# Honggfuzz Libfuzzer File Input To Pkcs15 Reader Harness

## Round 6 Input Contract
- The selected OpenSC target is the PKCS15 reader harness, not the direct ASN.1 printer. It installs a fake reader, consumes chunks front-to-back for connect and transmit calls, then binds a PKCS15 card and optionally exercises objects if binding succeeds.

## Format Links
- [[opensc-smart-card-response-stream-asn-1]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
