---
type: format-family
title: "Gdal Filesystem Raster Format"
description: "Input contract facts for gdal-filesystem-raster."
tags: ["gdal-filesystem-raster", "round-30"]
okf_support: 0
train_only: true
---
# Gdal Filesystem Raster Format

## Round 30 Factual Contract

### Schema / Invariants
- The GDAL filesystem target accepts a complete raster file and lets GDAL identify the driver from file content. RMF raster files use a fixed header with raster dimensions, bit depth, tile geometry, optional overview and color-table areas, and a tile table made of offset/size entries followed by tile payloads. VRT files are XML descriptors that can reference sources, warped sources, resampling operations, derived bands, masks, and overviews.

### Harness Links
- [[afl-gdal-filesystem-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
