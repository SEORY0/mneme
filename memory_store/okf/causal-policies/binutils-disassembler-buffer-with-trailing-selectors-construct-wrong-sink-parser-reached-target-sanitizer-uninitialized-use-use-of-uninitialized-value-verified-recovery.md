---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailing Selectors Construct Wrong Sink Parser Reached Target Sanitizer Uninitialized Use Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_target_sanitizer_uninitialized_use."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sanitizer_uninitialized_use"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailing-selectors"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "binutils-disassembler-buffer-with-trailing-selectors", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-target-sanitizer-uninitialized-use", "binutils-disassembler-buffer-with-trailing-selectors", "libfuzzer", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Binutils Disassembler Buffer With Trailing Selectors Construct Wrong Sink Parser Reached Target Sanitizer Uninitialized Use Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_target_sanitizer_uninitialized_use` on `binutils-disassembler-buffer-with-trailing-selectors` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use the raw-disassembler harness envelope: select the ARC disassembler with a valid ARC subarchitecture trailer, and place a front instruction buffer that is decoded as a normal-width ARC instruction but does not match the opcode table.
2. This keeps the decoder in find_format, leaves the LIMM-needed flag unset by any successful opcode match, and then reaches the vulnerable read of that uninitialized flag.
3. Avoid very short or all-reserved encodings that either decode cleanly or produce unstable non-target crashes.

## Format Contract
- Input format: [[binutils-disassembler-buffer-with-trailing-selectors]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `binutils-disassembler-buffer-with-trailing-selectors` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
