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

## Round 38 Factual Contract

### Schema / Invariants
- SAV files contain an SPSS header, dictionary variable records, optional machine and string metadata records, a dictionary terminator, and fixed-width row data. Long strings are stored across multiple row segments while metadata records describe the logical string length. The UTF-8 string path skips NUL characters while filling the raw string buffer, so a segment with only skipped characters can leave the raw-string-used counter at zero before the parser advances to the next segment.

### Harness Links
- [[libfuzzer-raw-sav]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
