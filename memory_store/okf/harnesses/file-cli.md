---
type: harness-contract
title: "File Cli harness"
description: "Input contract facts for file-cli."
tags: ["file-cli", "round-15"]
okf_support: 1
---
# File Cli Harness

## Round 15 Input Contract
- The generated runner invokes a GPAC command-line inspection path over the raw file. The bytes must
  be recognized as an MP3 input by GPAC's filter selection before the MP3 frame parser and bitrate
  lookup are reached; there is no libFuzzer byte carving.

## Format Links
- [[mp3]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
