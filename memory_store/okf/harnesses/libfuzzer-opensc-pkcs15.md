---
type: harness-contract
title: "Libfuzzer Opensc Pkcs15 harness"
description: "Input contract facts for libfuzzer-opensc-pkcs15."
tags: ["libfuzzer-opensc-pkcs15", "round-20"]
okf_support: 1
---
# Libfuzzer Opensc Pkcs15 Harness

## Round 20 Input Contract
- The OpenSC harness family is raw libFuzzer input. One target passes the same bytes directly to PKCS#15 decoders; another consumes two-byte chunk lengths from the front and feeds chunks through a fake reader before binding a PKCS#15 card and invoking operations on discovered objects.

## Round 20 Format Links
- [[opensc-pkcs15-asn1-or-reader-chunks]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
