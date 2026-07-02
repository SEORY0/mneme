---
type: format-family
title: "Dwg R11"
description: "Round 7 factual format contract for dwg-r11."
resource: cybergym://format/dwg-r11
tags: ["dwg-r11", "format-contract", "round-7"]
okf_support: 11
train_only: true
---
# Dwg R11

## Round 7 Factual Contract

### Schema / Invariants
- LibreDWG chooses binary DWG when the input begins with an AutoCAD version signature. Pre-R13/R11
files contain section boundary fields for entities and table sections, followed by header variables,
CRC/sentinel data, and entity/table payloads whose offsets must remain mutually consistent.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 19 Factual Contract

- R11 DWG files start with an AC legacy version marker and include pre-R13 section tables, sentinels, header variables, entity/block ranges, table records, optional auxheader data, and CRC/sentinel material. Small random corruption usually exits early.
- Harness link: [[libfuzzer-raw-dwg-dxf-json-dispatcher]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 27 Factual Contract

- R11 DWG files start with an AutoCAD release marker and carry a legacy header with entity, block, and extra-entity ranges plus table records containing size, count, flags, and payload address fields.
- R11 sections are guarded by fixed sentinels, and the table payload address is expected to point after the section's begin sentinel.
- Small entity-size, block-range, EED, or clean seed mutations can preserve parser reachability but miss this table-address relation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
