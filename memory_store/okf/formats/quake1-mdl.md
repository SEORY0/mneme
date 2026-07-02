---
type: format-family
title: "Quake1 Mdl Format"
description: "Round 27 descriptive format facts for quake1-mdl."
resource: cybergym://format/quake1-mdl
tags: ["quake1-mdl", "round-27"]
okf_support: 1
---
# Quake1 Mdl Format

## Round 27 Factual Contract

- Quake1 MDL is a whole-file binary model.
- The header carries signature, version, scale/translation, skin dimensions, skin count, vertex count, triangle count, and frame count.
- After the header come optional skins, one texture-coordinate record per declared vertex, one triangle record per declared triangle, then frame data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
