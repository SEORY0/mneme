---
type: format-family
title: "Spss Sav"
description: "Round 19 factual format contract for spss-sav."
resource: cybergym://format/spss-sav
tags: ["spss-sav", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Spss Sav

## Round 19 Factual Contract

- SAV files begin with an SPSS file header, followed by variable records, optional information records such as character encoding, a dictionary terminator, and row data. String variables are processed in fixed-width row segments. For UTF-8 input, null bytes in string segments are skipped; the vulnerable relation needs a segmented string where a zero segment leaves the raw-string byte counter empty before the segment transition decrement.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
