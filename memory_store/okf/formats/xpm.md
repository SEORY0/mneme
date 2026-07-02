---
type: format-family
title: "xpm format"
description: "Structure, build skeleton, and bug-prone areas of the xpm input format."
resource: cybergym://format/xpm
tags: ["xpm", "round-29"]
okf_support: 0
---
# XPM Format

## Round 29 Factual Contract

### Schema / Invariants
- XPM files for this reader start with an identifying comment-style magic and use C-source-like quoted strings. The first quoted record declares image dimensions, color count, and characters per pixel; following quoted records define color keys and then pixel rows. The reader strips unquoted C syntax, turns closing quotes into logical newlines, builds a text-list view over that reconstructed buffer, then parses the color table and pixel rows.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
