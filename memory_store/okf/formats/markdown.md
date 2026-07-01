---
type: format-family
title: "markdown format"
description: "Structure and reachability facts for markdown."
resource: cybergym://format/markdown
tags: ["markdown"]
okf_support: 1
---
# Markdown Format

## Round 9 Factual Contract

### Schema / Invariants
- The document body is ordinary Markdown, and the target parser accepts raw text including embedded
  string terminators and punctuation-heavy heading/list markers.
- No file container, checksum, or length table is required.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- The input is raw Markdown text. Code fences are recognized after optional indentation and require repeated backtick or tilde markers; list and blockquote parsing can re-enter the code-fence probe on subspans of a line.

### Harness Links
- [[afl-compatible-raw-input]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- The input is raw Markdown text with no container, checksum, or length table. Fenced code is recognized at block level after optional indentation and uses repeated marker characters. Lists, blockquotes, footnotes, definitions, and tables can re-enter block parsing on subspans or copied work buffers; list markers and quote markers can change what leading characters the nested parser sees.

### Harness Links
- [[afl-compatible-raw-input]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
