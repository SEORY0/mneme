---
type: format-family
title: "wpg format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/wpg"
tags: ["wpg", "round-35"]
okf_support: 1
train_only: true
---
# wpg Format

## Round 35 Factual Contract
### Schema / Invariants
- WPG files begin with a WPC signature and a little-endian header containing a data offset, product type, file type, version bytes, and encryption key. The first record begins at the declared data offset; sample level-1 files use the header end as the first record position, so adding separate reserved bytes without moving the data offset makes the parser read the wrong record. Level-1 records use a one-byte record type followed by a variable-length record size. Level-1 palette records carry a start index and entry count followed by RGB triples. Level-1 bitmap records carry geometry, dimensions, bit depth, resolution, and then WPG RLE raster data. The RLE stream uses control bits to choose repeated bytes, literal bytes, or repeated previous rows. Level-2 records add class, record type, extension length, and record length fields; compressed level-2 bitmap records use a different RLE token set with sample-size, XOR, block, reset, and white-run controls.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
