---
type: harness-contract
title: "Libfuzzer Flac Decoder Datasource harness"
description: "Input contract facts for libfuzzer-flac-decoder-datasource."
tags: ["libfuzzer-flac-decoder-datasource", "round-24"]
okf_support: 4
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

## Round 33 Input Contract

### Input Contract
- The active decoder harness does not feed raw FLAC directly. Every harness value is a front-consumed datasource item encoded as a little-endian length followed by that many bytes. The first boolean selects native FLAC versus Ogg initialization. Several option booleans may consume additional scalar or data items. Operation-loop booleans and byte selectors call decoder operations such as process_single, process_until_end_of_metadata, process_until_end_of_stream, and seek_absolute. Decoder read callbacks pull FLAC stream bytes from subsequent length-prefixed datasource items; oversized items are truncated to the callback request, so long streams must be split into callback-sized chunks.
- The active decoder target is not a raw-file harness. It consumes a front-to-back datasource where each scalar or byte-vector read is encoded as a little-endian length-prefixed item. Initial boolean items select native versus Ogg decoding and optional decoder settings. The operation loop consumes a boolean and an operation byte; decoder read callbacks then consume length-prefixed byte chunks as stream data, and write callbacks can consume a boolean to decide whether to abort.

### Format Links
- [[datasource-wrapped-flac]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
