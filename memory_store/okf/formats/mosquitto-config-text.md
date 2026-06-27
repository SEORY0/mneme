---
type: format-family
title: "Mosquitto Config Text"
description: "Round 12 factual format contract for mosquitto-config-text."
resource: cybergym://format/mosquitto-config-text
tags: ["mosquitto-config-text", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Mosquitto Config Text

## Round 12 Factual Contract

### Schema / Invariants
- Mosquitto config is newline-separated directive text. Default listener directives create or modify the implicit listener, while listener directives append explicit listeners. Later directives operate on the parser state established by earlier lines.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
