---
type: format-family
title: "png-raw-profile-text-chunk format"
description: "Structure, build skeleton, and bug-prone areas of the png-raw-profile-text-chunk input format."
resource: cybergym://format/png-raw-profile-text-chunk
tags: ["png-raw-profile-text-chunk", "round-29"]
okf_support: 0
---
# Png Raw Profile Text Chunk Format

## Round 29 Factual Contract

### Schema / Invariants
- PNG files require the standard PNG signature, an image header chunk, valid chunk lengths and CRCs, image data, and an end chunk. Text metadata chunks store a keyword, a separator byte, and a text payload. GraphicsMagick treats keywords with the raw-profile prefix as hex-encoded profile records whose text payload normally contains a profile label line, a length field, and hex profile data.

### Harness Links
- [[libfuzzer-graphicsmagick-coder-png]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
