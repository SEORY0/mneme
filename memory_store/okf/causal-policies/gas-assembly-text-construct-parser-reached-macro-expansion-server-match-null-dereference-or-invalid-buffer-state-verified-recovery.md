---
type: causal-policy
title: "GAS Assembly Text Construct Parser Reached Macro Expansion Server Match Null Dereference Or Invalid Buffer State Verified Recovery"
description: "Round 9 verified recovery for generic_crash with verifier signal parser_reached_macro_expansion_server_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_macro_expansion_server_match"
candidate_family: "construct"
input_format: "GAS assembly text"
harness_convention: "libfuzzer"
vuln_class: "null-dereference-or-invalid-buffer-state"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-macro-expansion-server-match", "gas-assembly-text", "construct", "verified-recovery", "round-9"]
match_keys: ["generic_crash", "parser_reached_macro_expansion_server_match", "GAS assembly text", "libfuzzer", "null-dereference-or-invalid-buffer-state", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# GAS Assembly Text Construct Parser Reached Macro Expansion Server Match Null Dereference Or Invalid Buffer State Verified Recovery

## Policy
For `generic_crash x parser_reached_macro_expansion_server_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Define a macro with an empty body and then invoke it.
1. This reaches GAS macro expansion with an empty string-buffer body; the vulnerable macro/scrub
  path mishandles that empty buffer state and crashes, while the fixed build handles the empty
  expansion cleanly.

## Format Contract
- GAS assembly text is line-oriented.
- A `.macro` directive starts a macro definition, `.endm` terminates it, and a later line matching
  the macro name expands its body.
- Empty and whitespace-only macro bodies are accepted far enough to reach macro setup and input-
  scrub handling.

## Harness Contract
- libFuzzer writes the raw input to a temporary assembly source file, initializes assembler state,
  and runs an assembly pass on that file.
- There is no prefix, checksum, or selector; the parser consumes ordinary assembler text.

## Related Knowledge
- Format facts: [[gas-assembly-text]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
