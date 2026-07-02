---
type: format-family
title: "Lua Source format"
description: "Round 8 descriptive format facts for lua-source."
resource: cybergym://format/lua-source
tags: ["lua-source", "round-8", "round-16"]
okf_support: 2
---
# Lua Source Format

## Round 8 Factual Contract

### Schema / Invariants
- The input is text-mode Lua source. Code can define local functions, tables, closures, expressions, and chunks, but standard-library helpers are absent unless provided by the core VM itself.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is Lua source text. Tail calls are produced by return statements that immediately call another function. The syntax gate is ordinary Lua parsing; no file container, checksum, or binary chunk wrapper is needed for text-mode inputs.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 16 Factual Contract

### Schema / Invariants
- The input format is plain Lua source text. The target accepts text chunks only; source-level constructs such as local declarations, attributes, closures, loops and gotos are parsed by Lua before bytecode execution.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- Lua input is raw text source only; binary chunks are rejected by text mode. Valid source can define local functions, closures, tables, varargs, returns, loops, and lexical blocks. Tail calls are produced by return statements that directly return a function call when the language permits tail-call generation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
