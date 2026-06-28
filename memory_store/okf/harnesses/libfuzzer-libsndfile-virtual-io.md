---
type: harness-contract
title: "Libfuzzer Libsndfile Virtual Io harness"
description: "Round 23 input contract facts for libfuzzer-libsndfile-virtual-io."
tags: ["libfuzzer-libsndfile-virtual-io", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Libsndfile Virtual Io Harness

## Round 23 Input Contract
- The libsndfile fuzzer feeds the complete raw input through virtual file I/O into the normal open path, then reads decoded floating-point frames. Short or inconsistent sample data can expose uninitialized reads only after the container has selected a conversion path.

## Round 23 Format Links
- [[audio-container-aiff-au]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
