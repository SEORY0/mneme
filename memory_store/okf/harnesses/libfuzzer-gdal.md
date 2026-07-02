---
type: harness-contract
title: "Libfuzzer GDAL Harness"
description: "Input contract facts for libfuzzer-gdal."
tags: ["libfuzzer-gdal", "round-27"]
okf_support: 1
---
# Libfuzzer GDAL Harness

## Round 27 Input Contract
- The run_poc wrapper reads the submitted file as raw bytes.
- The GDAL fuzzer places those bytes at a fixed in-memory filename, calls GDALAllRegister, opens that filename read-only, then probes raster bands and metadata.
- There is no FuzzedDataProvider, mode byte, checksum gate, or archive wrapper.

## Round 27 Format Links
- [[tiff]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
