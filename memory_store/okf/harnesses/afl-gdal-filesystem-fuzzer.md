---
type: harness-contract
title: "Afl Gdal Filesystem Fuzzer Harness"
description: "Input contract facts for afl-gdal-filesystem-fuzzer."
tags: ["afl-gdal-filesystem-fuzzer", "round-30"]
okf_support: 0
train_only: true
---
# Afl Gdal Filesystem Fuzzer Harness

## Round 30 Input Contract

### Input Contract
- The AFL-style GDAL filesystem harness writes the raw fuzz bytes to a temporary file and opens that path with the registered GDAL drivers. If a dataset opens, it reads bands, masks, metadata, georeferencing, GCPs, and overviews via checksum-style read operations. There is no FuzzedDataProvider layout or selector byte; reachability depends on the file content being recognized as a supported raster dataset.

### Format Links
- [[gdal-filesystem-raster]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
