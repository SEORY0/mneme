---
type: harness-contract
title: "Libfuzzer Rawspeed Ciff Parser harness"
description: "Round 23 input contract facts for libfuzzer-rawspeed-ciff-parser."
tags: ["libfuzzer-rawspeed-ciff-parser", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Rawspeed Ciff Parser Harness

## Round 23 Input Contract
- The active RawSpeed harness feeds raw bytes into the generic RawParser, obtains a decoder, disables crop/support strictness, and calls raw decode plus metadata decode while catching RawSpeed exceptions. It is a full camera-file parser, not a direct CRW decompressor envelope.

## Round 23 Format Links
- [[canon-ciff-crw]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
