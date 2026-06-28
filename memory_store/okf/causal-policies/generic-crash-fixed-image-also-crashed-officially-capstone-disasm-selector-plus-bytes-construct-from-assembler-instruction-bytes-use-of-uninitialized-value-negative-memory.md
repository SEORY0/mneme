---
type: causal-policy
title: "Generic Crash Fixed Image Also Crashed Officially Capstone Disasm Selector Plus Bytes Construct From Assembler Instruction Bytes Use Of Uninitialized Value Negative Memory"
description: "Round 14 negative memory for generic_crash with verifier signal fixed_image_also_crashed_officially."
failure_class: "generic_crash"
verifier_signal: "fixed_image_also_crashed_officially"
candidate_family: "construct_from_assembler_instruction_bytes"
input_format: "capstone-disasm-selector-plus-bytes"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "fixed-image-also-crashed-officially", "capstone-disasm-selector-plus-bytes", "negative-memory", "round-14"]
match_keys: ["generic_crash", "fixed_image_also_crashed_officially", "capstone-disasm-selector-plus-bytes", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# Generic Crash Fixed Image Also Crashed Officially Capstone Disasm Selector Plus Bytes Construct From Assembler Instruction Bytes Use Of Uninitialized Value Negative Memory

- key: `generic_crash x fixed_image_also_crashed_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[capstone-disasm-selector-plus-bytes]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A real BND instruction sequence reached the X86 disassembler and produced an uninitialized-value crash, but official submission showed the fixed image still crashed. Isolating register-only forms did not find a differential variant within the budget.

## Policy
Treat `generic_crash x fixed_image_also_crashed_officially` on `capstone-disasm-selector-plus-bytes` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
