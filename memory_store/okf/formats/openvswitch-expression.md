---
type: format-family
title: "Openvswitch Expression format"
description: "Structure and invariants for the openvswitch-expression input format."
tags: ["openvswitch-expression", "round-20"]
okf_support: 2
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- OVN expression input is raw textual syntax. Integer tokens can be decimal or hexadecimal, and field comparisons can wrap constants in equality or mask-style expressions. The vulnerable hexadecimal lexer walks hex digits from the end toward the beginning and stores nibbles into a fixed-width parsed value buffer.

### Harness Links
- [[afl-raw-stdin]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 28 Factual Contract

### Schema / Invariants
- OVN expression inputs are textual logical-match expressions. Address sets are referenced by name with the address-set sigil and port groups with the port-group sigil; referenced sets can be empty even though a literal empty value set is not accepted syntax. Equality and inequality with empty referenced sets normalize to boolean expressions, while ordered comparisons enter scalar comparison validation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- OVN expression inputs are raw text. Integer tokens may use a hexadecimal prefix. The hexadecimal parser scans digits from the end toward the start and packs nibbles into a fixed-width token value buffer; nonzero high digits trigger an overflow diagnostic, but zero high digits continue through the same packing loop.

### Harness Links
- [[afl-libfuzzer-compatible-raw-file]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
