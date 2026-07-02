---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct Wrong Sink Parser Reached Target Match Use Of Uninitialized Value From Unchecked Disassembler Buffer Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value from unchecked disassembler buffer read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "binutils-disassembler-buffer-with-trailer-selector", "use-of-uninitialized-value-from-unchecked-disassembler-buffer-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-target-match", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "use-of-uninitialized-value-from-unchecked-disassembler-buffer-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Binutils Disassembler Buffer With Trailer Selector Construct Wrong Sink Parser Reached Target Match Use Of Uninitialized Value From Unchecked Disassembler Buffer Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_target_match` on `binutils-disassembler-buffer-with-trailer-selector` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Select the S12Z disassembler through the raw trailer selector and keep the instruction stream just long enough to pass the harness but too short for the page-two opcode fetch.
2. A page-two prefix makes the decoder use an unchecked follow-on byte from the disassembly buffer; the fixed build handles that short-buffer path cleanly.

## Format Contract
- Input format: [[binutils-disassembler-buffer-with-trailer-selector]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `binutils-disassembler-buffer-with-trailer-selector` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
