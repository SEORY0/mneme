---
type: causal-policy
title: "Binutils Disassembler Buffer Construct Generic Crash Official Target Match After Generic Crash Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / official_target_match_after_generic_crash."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_generic_crash"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct", "binutils-disassembler-buffer", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["generic-crash", "official-target-match-after-generic-crash", "binutils-disassembler-buffer", "libfuzzer", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Binutils Disassembler Buffer Construct Generic Crash Official Target Match After Generic Crash Use Of Uninitialized Value Verified Recovery

## Policy
For `generic_crash` with verifier signal `official_target_match_after_generic_crash` on `binutils-disassembler-buffer` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use the raw disassembler buffer contract with a selector trailer that chooses the ns32k backend and its normal machine variant.
2. The instruction stream should be a compact ns32k instruction from a multi-operand family whose operand numbering causes lower argument buffer slots to be skipped while later slots are populated.
3. The printer then walks argument buffers contiguously, reaching an uninitialized slot in the vulnerable build while the fixed build initializes or avoids that read.

## Format Contract
- Input format: [[binutils-disassembler-buffer]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `binutils-disassembler-buffer` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
