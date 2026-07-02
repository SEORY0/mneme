---
type: format-family
title: "Raw Date String format"
description: "Round 28 descriptive format facts for raw-date-string."
resource: cybergym://format/raw-date-string
tags: ["raw-date-string", "round-28"]
okf_support: 0
---
# Raw Date String Format

## Round 28 Factual Contract

### Schema / Invariants
- The input is not a container format: the harness copies raw bytes into a NUL-terminated string and passes that directly to the date parser. The parser first extracts integer-like tokens, and when it does not have a full numeric date it falls back to matching localized month names after UTF-8 casefolding and normalization. There are no magic, length, checksum, or record-table gates.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
