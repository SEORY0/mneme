---
type: harness-contract
title: "Libfuzzer Tempfile harness"
description: "Input contract facts for libfuzzer-tempfile."
tags: ["libfuzzer-tempfile", "round-25"]
okf_support: 0
---
# Libfuzzer Tempfile Harness

## Round 25 Input Contract
- The fuzzer writes raw input bytes to a temporary config file, initializes an LXC config object, calls the normal config reader on the temp file, frees the config, and removes the temp file.

## Round 25 Format Links
- [[lxc-config-text]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
