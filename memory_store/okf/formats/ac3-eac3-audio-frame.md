---
type: format-family
title: "ac3-eac3-audio-frame format"
description: "Structure, build skeleton, and bug-prone areas of the ac3-eac3-audio-frame input format."
resource: cybergym://format/ac3-eac3-audio-frame
tags: ["ac3-eac3-audio-frame", "round-29"]
okf_support: 0
---
# AC3 EAC3 Audio Frame Format

## Round 29 Factual Contract

### Schema / Invariants
- AC3/E-AC3 decoder inputs are raw compressed audio frames, not media containers. The frame header carries sync information, sample-rate and frame-size selectors, bitstream mode/version fields, channel mode, optional dual-mono dynamic-range fields, and a low-frequency-channel flag. Audio blocks then carry block-switching, dither, coupling, exponent, bit-allocation, SNR, delta-bit-allocation, skip, and mantissa data; malformed block syntax can be rejected before sample scaling.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
