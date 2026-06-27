---
type: format-family
title: file-magic-raw-buffer format
description: Structure and reachability facts for file-magic-raw-buffer inputs.
tags: [file-magic-raw-buffer]
okf_support: 0
---
# File Magic Raw Buffer Format

## Round 10 Factual Contract

### Schema / Invariants
- The input is passed as raw bytes to libmagic through magic_buffer. The format is not a normal file container; parser selection depends on matching compiled magic rules, including search and regex rule types.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
