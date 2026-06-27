---
type: format-family
title: Raw disassembler buffer
description: Abstract format contract for Raw disassembler buffer verifier-causal recoveries.
resource: cybergym://format/raw-disassembler-buffer
tags: [raw-disassembler-buffer, format_contract, "round-16"]
okf_support: 2
---
# Raw disassembler buffer

## Identification
This harness selects an architecture through a suffix or selector outside the instruction bytes.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Preserve the selector that reaches the target disassembler, then use an instruction family that exercises the specific operand printer rather than random opcode bytes.

## Linked Policies
[[tic30-disassembler-branch-operand-overflow]]

## Round 6 Factual Contract

### Schema / Invariants
- The Capstone fuzz target consumes raw instruction bytes and disassembles them under a configured architecture/mode. Relevant ARM memory operands encode base/index registers plus optional shift type/value metadata.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The disassembler fuzzer treats most bytes as instruction data and reserves a small trailer for flavour, machine, and architecture selection. KVX bundles are made of fixed-width syllable words; a high continuation bit asks the decoder to keep collecting words up to the bundle maximum before reassembly.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
