---
type: format-family
title: "Gas Assembly Source Format"
description: "Round 27 descriptive format facts for gas-assembly-source."
resource: cybergym://format/gas-assembly-source
tags: ["gas-assembly-source", "round-27"]
okf_support: 1
---
# Gas Assembly Source Format

## Round 27 Factual Contract

- The input is plain assembler text as consumed by GNU as.
- A leading preprocessor line-control directive changes the input-file reader's path: the reader consumes the marker, expects a following source-name line, and scans that line for a newline terminator.
- EOF at that point is a semantic violation rather than a binary container failure.

### Harness Links
- [[libfuzzer-raw-file-to-gas]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
