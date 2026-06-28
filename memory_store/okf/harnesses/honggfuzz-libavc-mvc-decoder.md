---
type: harness-contract
title: "honggfuzz-libavc-mvc-decoder harness"
description: "Descriptive harness contract facts for honggfuzz-libavc-mvc-decoder."
tags: ["honggfuzz-libavc-mvc-decoder", "round-18"]
okf_support: 1
train_only: true
---
# Honggfuzz Libavc Mvc Decoder Harness

## Round 18 Input Contract

### Schema / Invariants
- The verifier target is the libavc MVC decoder fuzzer. It accepts a raw elementary stream file and drives decoder initialization and frame decode directly; there is no FuzzedDataProvider split or external container demuxer.

### Format Links
- [[h264-annexb-mvc]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
