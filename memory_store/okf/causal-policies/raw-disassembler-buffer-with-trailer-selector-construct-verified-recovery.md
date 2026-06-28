---
type: causal-policy
title: "Raw Disassembler Buffer With Trailer Selector Construct Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal plausible_target_crash."
failure_class: "generic_crash"
verifier_signal: "plausible_target_crash"
candidate_family: "construct"
input_format: "raw disassembler buffer with trailer selector"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-or-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "plausible-target-crash", "raw-disassembler-buffer-with-trailer-selector", "construct", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "plausible_target_crash", "raw disassembler buffer with trailer selector", "libfuzzer", "uninitialized-or-out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# Raw Disassembler Buffer With Trailer Selector Construct Verified Recovery

## Policy
For `generic_crash x plausible_target_crash`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the harness trailer to select the MetaG disassembler and machine variant, while keeping the instruction payload minimal and malformed enough that the disassembler consults memory through the path that ignores the supplied read callback. The fixed build returns cleanly, while the vulnerable build faults during disassembly.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The payload is mostly raw disassembly bytes, but the harness reserves a trailing selector region for flavour, machine, and architecture values. The architecture and machine selector, not a file magic, determine whether the MetaG printer is reached.
- Harness: The libFuzzer harness rejects very short and oversized inputs, treats the leading region as the disassembly buffer, reads the final selector fields from the end of the input, looks up a BFD architecture, then calls the selected disassembler repeatedly with an in-memory disassemble_info buffer.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
