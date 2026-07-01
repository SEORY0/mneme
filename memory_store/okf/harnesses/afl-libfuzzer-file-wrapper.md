---
type: harness-contract
title: "Afl Libfuzzer File Wrapper harness"
description: "Round 23 input contract facts for afl-libfuzzer-file-wrapper."
tags: ["afl-libfuzzer-file-wrapper", "round-23"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer File Wrapper Harness

## Round 23 Input Contract
- The fuzzer feeds the raw file bytes through libsndfile virtual I/O, opens them with sf_open_virtual, allocates one frame of float output per reported channel, and repeatedly calls sf_readf_float until decoding stops.

## Round 23 Format Links
- [[wav-ima-adpcm]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The GPAC fuzz target writes the raw input bytes to a temporary file and opens that file with gf_isom_open_file in read-dump mode, then closes the movie if opening succeeds. The input is a complete MP4/BMFF file image; there is no selector byte or FuzzedDataProvider carving.

### Format Links
- [[isobmff-mp4]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
