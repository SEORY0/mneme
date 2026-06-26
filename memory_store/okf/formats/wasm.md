---
type: format-family
title: "Wasm format"
description: "Descriptive contract facts for Wasm."
resource: "cybergym://format/wasm"
tags: ["wasm", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- A minimal Wasm module needs the standard magic/version, a function type, a function section, an exported function matching the harness lookup, executable code for that function, and any memory/data sections referenced by active data segments. Init expressions are bytecode streams terminated by an end opcode.

### Harness Links
- [[libfuzzer-wasm3-module-loader]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
