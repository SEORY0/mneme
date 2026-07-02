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

## Round 26 Factual Contract


### Input Contract
- The harness writes the raw libFuzzer input bytes to a temporary file, initializes dlltool globals, sets the definition-file path to that temporary file, and calls process_def_file. There is no FuzzedDataProvider layout, no split object-file half in this generated task, and no prefix selector; the entire PoC is the definition file.

### Format Links
- [[dlltool-def-file]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
