---
type: harness-contract
title: "Libfuzzer Sndfile Virtual Io"
description: "Round 36 factual harness contract for libfuzzer-sndfile-virtual-io."
tags: ["libfuzzer-sndfile-virtual-io", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Libfuzzer Sndfile Virtual Io

## Round 36 Input Contract
- The sndfile fuzz harness passes the submitted bytes unchanged through libsndfile virtual I/O and calls sf_open_virtual in read mode. There is no leading selector byte, no external length prefix, no integrity wrapper, and no FuzzedDataProvider front/back split; the whole input must be a parseable audio container.

## Round 36 Format Links
- [[wav-riff-list-exif]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
