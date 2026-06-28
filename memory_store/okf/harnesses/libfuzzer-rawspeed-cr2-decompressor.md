---
type: harness-contract
title: "Libfuzzer Rawspeed Cr2 Decompressor harness"
description: "Round 23 input contract facts for libfuzzer-rawspeed-cr2-decompressor."
tags: ["libfuzzer-rawspeed-cr2-decompressor", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Rawspeed Cr2 Decompressor Harness

## Round 23 Input Contract
- The harness constructs a RawImage from the envelope, builds Cr2Slicing from three slice fields, constructs a Cr2Decompressor over the remaining byte stream, creates image data, decodes, and checks that the raw image memory was initialized. RawSpeed exceptions are treated as clean exits.

## Round 23 Format Links
- [[rawspeed-cr2-decompressor-envelope]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
