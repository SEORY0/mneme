---
type: format-family
title: "h264-annexb-mvc format"
description: "Structure and invariants for the h264-annexb-mvc input format."
tags: ["h264-annexb-mvc", "round-14"]
okf_support: 12
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is an H.264 elementary stream with Annex-B-style NAL units. The MVC decoder needs valid sequence/header information before frame decode. The target bug is in Film Grain Characteristics SEI parsing, which requires an SEI NAL payload with declared FGC syntax that outlives the available bitstream data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 18 Factual Contract

### Schema / Invariants
- The decoder consumes H.264 Annex B-style elementary streams made of start-code-prefixed NAL units. Sequence and picture parameter sets establish decoding state before slice and SEI NALs. SEI NALs can contain multiple payloads; each payload has a type, length, payload bytes, and rbsp trailing bits. The described sink involves film grain characteristics data inside MVC SEI parsing.

### Harness Links
- [[honggfuzz-libavc-mvc-decoder]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 27 Factual Contract

- The input is a raw H.264 Annex-B elementary stream.
- NAL units are start-code delimited; SPS and PPS establish decoder state before frame decode.
- SEI NAL payloads are a sequence of payload-type and payload-size fields followed by payload bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
