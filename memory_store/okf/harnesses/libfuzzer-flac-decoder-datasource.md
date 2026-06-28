---
type: harness-contract
title: "Libfuzzer Flac Decoder Datasource harness"
description: "Input contract facts for libfuzzer-flac-decoder-datasource."
tags: ["libfuzzer-flac-decoder-datasource", "round-24"]
okf_support: 1
---
# Libfuzzer Flac Decoder Datasource Harness

## Round 24 Factual Contract

### Input Contract
- The harness does not feed raw FLAC bytes directly. It uses a Datasource where every consumed value is length-prefixed; leading booleans choose native versus Ogg initialization and optional decoder settings, loop controls choose operations such as process-single or process-until-end, and read callbacks pull length-prefixed byte chunks as decoder input.

### Format Links
- [[datasource-wrapped-flac]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
