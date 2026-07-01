---
type: harness-contract
title: "Afl harness"
description: "Input contract facts for afl."
tags: ["afl", "round-32"]
okf_support: 1
---
# Afl Harness

## Round 32 Input Contract
- The harness is an AFL-style raw-buffer target. It wraps the entire PoC as an in-memory file, installs ReadStat buffer open/read/seek/update handlers, then calls readstat_parse_sas7bdat with no filename and no FuzzedDataProvider split, mode byte, argv file path, or stdin format wrapper.

## Round 32 Format Links
- [[sas7bdat]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
