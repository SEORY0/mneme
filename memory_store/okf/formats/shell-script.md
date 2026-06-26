---
type: format-family
title: "Shell Script format"
description: "Round 8 descriptive format facts for shell-script."
resource: cybergym://format/shell-script
tags: ["shell-script", "round-8"]
okf_support: 1
---
# Shell Script Format

## Round 8 Factual Contract

### Schema / Invariants
- The shell input is plain source text. Heredoc redirection syntax creates pending heredoc records, optional tab stripping changes how terminators are recognized, and interpolation inside the heredoc body can re-enter expression and command parsing before the parser finalizes those records.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

