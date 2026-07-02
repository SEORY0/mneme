---
type: harness-contract
title: "Libfuzzer Jpegsave File harness"
description: "Input contract facts for libfuzzer-jpegsave-file."
tags: ["libfuzzer-jpegsave-file", "round-29"]
okf_support: 0
---
# Libfuzzer Jpegsave File Harness

## Round 29 Input Contract

- The observed active target is the file-based JPEG save libFuzzer harness. It receives raw input bytes, writes them unchanged to a temporary file, loads that file with sequential access, rejects oversized images or excessive band counts, and then calls JPEG save-to-buffer. There is no FuzzedDataProvider carving; the entire PoC is the file image consumed by the loader.

## Round 29 Format Links
- [[native-vips-image]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
## Round 37 Input Contract

### Input Contract
- The libFuzzer entrypoint writes the raw input bytes to a temporary file, opens it with libvips sequential access, rejects images above small geometry or band-count limits, then serializes the loaded image with the JPEG-save buffer API.
- There is no FuzzedDataProvider and no mode-selector byte; the entire PoC is the candidate image file.

### Format Links
- [[native-vips-image]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
