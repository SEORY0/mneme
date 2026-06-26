---
type: format-family
title: "Lua Source format"
description: "Round 8 descriptive format facts for lua-source."
resource: cybergym://format/lua-source
tags: ["lua-source", "round-8"]
okf_support: 1
---
# Lua Source Format

## Round 8 Factual Contract

### Schema / Invariants
- The input is text-mode Lua source. Code can define local functions, tables, closures, expressions, and chunks, but standard-library helpers are absent unless provided by the core VM itself.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

