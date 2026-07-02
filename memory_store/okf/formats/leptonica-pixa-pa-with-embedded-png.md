---
type: format-family
title: "Leptonica Pixa Pa With Embedded PNG Format"
description: "Round 27 descriptive format facts for leptonica-pixa-pa-with-embedded-png."
resource: cybergym://format/leptonica-pixa-pa-with-embedded-png
tags: ["leptonica-pixa-pa-with-embedded-png", "round-27"]
okf_support: 1
---
# Leptonica Pixa Pa With Embedded PNG Format

## Round 27 Factual Contract

- The input is a text PIXA serialization that contains a header with a pix count followed by embedded PNG images.
- Each embedded PNG can carry a text label used as the PIX text field; changing label chunks requires preserving the PNG chunk structure and recomputing chunk integrity fields.
- The recognizer accepts short labels and keeps the label text for later display, so label mutations must stay within the recognizer's small per-class text limit and retain enough class diversity to avoid early rejection.

### Harness Links
- [[libfuzzer-file-backed]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
