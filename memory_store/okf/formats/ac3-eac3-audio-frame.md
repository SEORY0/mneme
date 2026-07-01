---
type: format-family
title: "ac3-eac3-audio-frame format"
description: "Structure, build skeleton, and bug-prone areas of the ac3-eac3-audio-frame input format."
resource: cybergym://format/ac3-eac3-audio-frame
tags: ["ac3-eac3-audio-frame", "round-29"]
okf_support: 2
---
# AC3 EAC3 Audio Frame Format

## Round 29 Factual Contract

### Schema / Invariants
- AC3/E-AC3 decoder inputs are raw compressed audio frames, not media containers. The frame header carries sync information, sample-rate and frame-size selectors, bitstream mode/version fields, channel mode, optional dual-mono dynamic-range fields, and a low-frequency-channel flag. Audio blocks then carry block-switching, dither, coupling, exponent, bit-allocation, SNR, delta-bit-allocation, skip, and mantissa data; malformed block syntax can be rejected before sample scaling.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- The fuzzer input is raw compressed AC3 or E-AC3 decoder packet data, not a media container. AC3/E-AC3 frames begin with a sync header, declare sample-rate and frame-size information, then carry bitstream metadata followed by one or more audio blocks. Coupling and spectral extension each have a band range plus either coded band structure bits or reuse/default semantics, followed by exponent, allocation, coordinate, and transform-coefficient data.
- The active input is raw compressed AC3-family frame data, not a media container. A frame starts with the AC3 sync word and header fields for sample rate, frame size, bitstream id, service mode, channel mode, and the low-frequency-channel flag. For normal AC3, the BSI section includes dual-mono dialog-normalization records and optional metadata flags, followed by per-block syntax for block switching, dither, dynamic range, coupling strategy, exponent strategies, channel bandwidth, exponents, bit allocation, SNR offsets, delta-bit-allocation, skip data, and transform coefficients.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
