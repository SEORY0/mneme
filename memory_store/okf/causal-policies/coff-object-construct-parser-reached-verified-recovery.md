---
type: causal-policy
title: "Coff Object Construct Parser Reached Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "coff-object"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "construct", "coff-object", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached", "coff-object", "libfuzzer", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Coff Object Construct Parser Reached Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[coff-object]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `coff-object` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached` on `coff-object` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Construct a minimal COFF object with a valid header and symbol table, then make a symbol declare
more auxiliary records than are present so normalized symbol-table loading enters the error cleanup
after COFF symbol swapping has allocated BFD-owned state.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
COFF objects have a fixed file header pointing to a symbol table. Each symbol table entry has a
short name or string-table reference, value, section index, type, storage class, and auxiliary-entry
count, followed by an optional string table.

## Harness Contract
The binutils wrapper writes the raw input to a temporary file and runs the safe objdump fuzzer path.
BFD determines the object format from the raw bytes and objdump requests headers, sections, symbols,
and related metadata.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
