---
type: harness-contract
title: "Lcms Postscript Fuzzer Raw ICC Profile harness"
description: "Input contract facts for lcms-postscript-fuzzer-raw-icc-profile."
tags: ["lcms-postscript-fuzzer-raw-icc-profile", "round-20"]
okf_support: 1
---
# Lcms Postscript Fuzzer Raw ICC Profile Harness

## Round 20 Input Contract
- The harness rejects inputs smaller than a fixed minimum, creates an lcms context, opens the entire byte stream as a memory profile, derives flags and intent from fixed words in that stream, and calls cmsGetPostScriptCSA and cmsGetPostScriptCRD with a NULL output buffer.

## Round 20 Format Links
- [[icc-profile]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
