---
type: harness-contract
title: "Libfuzzer Vsimem File harness"
description: "Round 23 input contract facts for libfuzzer-vsimem-file."
tags: ["libfuzzer-vsimem-file", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Vsimem File Harness

## Round 23 Input Contract
- The specialized GDAL OGR fuzzer writes raw bytes to a /vsimem file, registers the DXF driver, sets the BSpline control point limit to a small configured value, opens the in-memory path with OGR, and iterates layers/features. In this build DXF is not skipped; CAD is skipped separately.

## Round 23 Format Links
- [[dxf]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
