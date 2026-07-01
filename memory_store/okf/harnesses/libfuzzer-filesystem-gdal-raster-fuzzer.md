---
type: harness-contract
title: "Libfuzzer Filesystem Gdal Raster Fuzzer harness"
description: "Input contract facts for libfuzzer filesystem GDAL raster fuzzer."
tags: ["libfuzzer-filesystem-gdal-raster-fuzzer", "round-16"]
okf_support: 1
---
# Libfuzzer Filesystem Gdal Raster Fuzzer Harness

## Round 16 Input Contract
- The wrapper runs GDAL’s filesystem fuzzer on the raw PoC file path. The file contents must be self-identifying enough for GDALOpen to select the GXF driver before checksum-style raster reading reaches scanline decoding.

## Round 16 Format Links
- [[gxf]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 34 Factual Contract

### Input Contract
- The GDAL raster libFuzzer wrapper treats the PoC as a raw file, stores it as a temporary or virtual dataset, calls GDALOpen, and then computes raster checksums. Parser reachability depends on the file being self-identifying enough for the GXF driver before checksum-driven band reads call the GXF scanline decoder.

### Format Links
- [[gxf]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
