---
type: format-family
title: "Ascii Armored Openpgp"
description: "Round 36 factual format contract for ascii-armored-openpgp."
tags: ["ascii-armored-openpgp", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Ascii Armored Openpgp

## Round 36 Factual Contract

### Schema / Invariants
- ASCII-armored OpenPGP input is organized as a dashed BEGIN line, optional textual header lines, a blank line, base64 payload, CRC line, and dashed END line. RNP's type classifier uses only the inner text between the dashed groups. A later OpenPGP armor sentinel in the initial source window can satisfy broad armored-source detection even when the first dashed pair is a shorter malformed header.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
