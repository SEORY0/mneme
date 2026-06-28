---
type: format-family
title: "Shell Script format"
description: "Round 8 descriptive format facts for shell-script."
resource: cybergym://format/shell-script
tags: ["shell-script", "round-8"]
okf_support: 2
---
# Shell Script Format

## Round 8 Factual Contract

### Schema / Invariants
- The shell input is plain source text. Heredoc redirection syntax creates pending heredoc records, optional tab stripping changes how terminators are recognized, and interpolation inside the heredoc body can re-enter expression and command parsing before the parser finalizes those records.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Shell fuzzer input is plain script text. Bareword parsing can produce node types such as bareword literals, globs, tilde expressions, and juxtaposition forms. Glob parsing is recursive: a wildcard-bearing word can parse the remaining suffix as another glob or bareword-like node.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- Shell fuzzer input is plain script text. Heredoc redirection syntax records pending heredoc entries; the dash/tilde heredoc forms affect terminator handling, and interpolation in the body can re-enter nested expression parsing before heredoc finalization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
