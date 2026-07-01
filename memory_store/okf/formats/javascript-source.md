---
type: format-family
title: "Javascript Source"
description: "Round 12 factual format contract for javascript-source."
resource: cybergym://format/javascript-source
tags: ["javascript-source", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Javascript Source

## Round 12 Factual Contract

### Schema / Invariants
- The input is plain JavaScript source text. It must parse successfully and run far enough to allocate many objects or arrays so the runtime enters garbage collection.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- Input is raw JavaScript source text. The relevant syntax family combines switch statements, case/default labels, function declarations, and intentionally unclosed block/function scopes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 34 Factual Contract

### Schema / Invariants
- The input is plain JavaScript source text with no container header, length field, checksum, or trailing selector. Punctuation-style operator tokens are consumed directly by the lexer, and some operator prefixes are resolved by a helper that checks whether a continuation character follows.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- JavaScript source inputs need no magic, length, checksum, or mode byte. The relevant grammar region is switch statement parsing: a switch block owns case/default clauses, each clause may parse a statement list, and function declarations, arrow functions, and block statements inside a clause push additional parser continuations. Case/default tokens are only valid as switch labels; when they appear while an inner function-like parse is still unfinished, parser recovery behavior decides whether the token is rejected or incorrectly treated as an outer switch continuation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
