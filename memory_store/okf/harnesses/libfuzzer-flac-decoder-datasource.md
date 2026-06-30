---
type: harness-contract
title: "Libfuzzer Flac Decoder Datasource harness"
description: "Input contract facts for libfuzzer-flac-decoder-datasource."
tags: ["libfuzzer-flac-decoder-datasource", "round-24"]
okf_support: 2
---
# Libfuzzer Flac Decoder Datasource Harness

## Round 24 Factual Contract

### Input Contract
- The harness does not feed raw FLAC bytes directly. It uses a Datasource where every consumed value is length-prefixed; leading booleans choose native versus Ogg initialization and optional decoder settings, loop controls choose operations such as process-single or process-until-end, and read callbacks pull length-prefixed byte chunks as decoder input.

### Format Links
- [[datasource-wrapped-flac]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 31 Input Contract

### Input Contract
- The libFuzzer target is the FLAC decoder datasource harness. The input is not passed directly as a FLAC byte stream: each harness value is a little-endian length-prefixed datasource item consumed front-to-back. Boolean controls select native versus Ogg initialization and optional decoder settings. Decoder read callbacks pull length-prefixed byte chunks from the same datasource. Single-step processing can return after metadata before reading the first audio frame, so the control sequence must account for metadata and frame processing separately.

### Format Links
- [[datasource-wrapped-flac]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
