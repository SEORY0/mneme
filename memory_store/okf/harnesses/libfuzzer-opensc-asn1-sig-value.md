---
type: harness-contract
title: "Libfuzzer Opensc ASN1 Sig Value harness"
description: "Input contract facts for libfuzzer-opensc-asn1-sig-value."
tags: ["libfuzzer-opensc-asn1-sig-value", "round-20"]
okf_support: 1
---
# Libfuzzer Opensc ASN1 Sig Value Harness

## Round 20 Input Contract
- The active OpenSC fuzz target consumes raw bytes directly. It first calls ASN.1 sequence-to-R/S conversion with an output buffer sized from the input length, then calls R/S-to-sequence conversion on the same raw input; no smart-card APDU or chunk-stream wrapper is involved.

## Round 20 Format Links
- [[der-ecdsa-signature]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
