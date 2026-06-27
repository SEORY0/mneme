---
type: format-family
title: "Pdf Cmap"
description: "Round 12 factual format contract for pdf-cmap."
resource: cybergym://format/pdf-cmap
tags: ["pdf-cmap", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Pdf Cmap

## Round 12 Factual Contract

### Schema / Invariants
- A PDF ToUnicode CMap is stored as a stream referenced by a font. It declares codespace ranges, then bfchar and bfrange mappings. One-to-many Unicode mappings can appear in bfchar entries or array-based bfrange entries, and overlapping ranges force cmap node splitting.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
