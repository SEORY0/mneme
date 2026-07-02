---
type: harness-contract
title: "libfuzzer-graphicsmagick-coder-write harness"
description: "Input contract facts for libfuzzer-graphicsmagick-coder-write."
tags: ["libfuzzer-graphicsmagick-coder-write", "round-35"]
okf_support: 1
train_only: true
---
# libfuzzer-graphicsmagick-coder-write Harness

## Round 35 Input Contract
### Input Contract
- The libFuzzer harness passes the raw input blob to Magick++ as a PTIF image, catches read exceptions, and only after a successful read writes the image back as PTIF. There is no FuzzedDataProvider carving or mode byte. Reaching the target requires a blob that decodes successfully first; the writer then derives output compression from the decoded image state.

### Format Links
- [[tiff-webp-ptif]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
