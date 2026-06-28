---
type: harness-contract
title: "Libfuzzer Rawspeed Tiffdecoderfuzzer Nefdecoder harness"
description: "Input contract facts for libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder."
tags: ["libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder", "round-24"]
okf_support: 1
---
# Libfuzzer Rawspeed Tiffdecoderfuzzer Nefdecoder Harness

## Round 24 Factual Contract

### Input Contract
- The harness feeds raw file bytes to RawSpeed, asks RawParser for the decoder, disables crop and unknown-camera failure, then calls decodeRaw followed by metadata decoding.

### Format Links
- [[nef-tiff]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
