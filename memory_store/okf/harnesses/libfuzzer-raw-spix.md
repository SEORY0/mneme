---
type: harness-contract
title: "Libfuzzer Raw Spix harness"
description: "Input contract facts for libfuzzer-raw-spix."
tags: ["libfuzzer-raw-spix", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Spix Harness

## Round 17 Input Contract
- The selected fuzzer reads raw input with pixReadMemSpix, not PNG/TIFF/JPEG.
- It copies the PIX, calls mirror detection, then calls orientation correction with uninitialized local threshold variables and finally calls orientation detection.

## Round 17 Format Links
- [[leptonica-spix]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[leptonica-spix]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
