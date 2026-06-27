---
type: format-family
title: "Alpha Ecoff Object"
description: "Round 19 factual format contract for alpha-ecoff-object."
resource: cybergym://format/alpha-ecoff-object
tags: ["alpha-ecoff-object", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Alpha Ecoff Object

## Round 19 Factual Contract

- Alpha ECOFF objects use a COFF-family file header with Alpha magic, optional header size, section headers, raw section contents, and relocation records. Section headers name raw-data and relocation locations and counts. The target relation requires a recognized Alpha ECOFF object whose relocation vector is iterated during relocated section content generation.
- Harness link: [[honggfuzz-wrapper]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
