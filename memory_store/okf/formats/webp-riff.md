---
type: format-family
title: "Webp Riff format"
description: "Round 28 descriptive format facts for webp-riff."
resource: cybergym://format/webp-riff
tags: ["webp-riff", "round-28"]
okf_support: 0
---
# Webp Riff Format

## Round 28 Factual Contract

### Schema / Invariants
- WebP containers use a RIFF envelope with a WEBP form tag and chunk records. Chunks carry a four-character tag, a little-endian payload length, payload bytes, and padding for odd payload sizes. Extended WebP starts with VP8X and feature flags; metadata chunks are only stored by demux when the matching feature flag is present, and animation files combine VP8X, ANIM, and ANMF records.

### Harness Links
- [[fuzztest]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
