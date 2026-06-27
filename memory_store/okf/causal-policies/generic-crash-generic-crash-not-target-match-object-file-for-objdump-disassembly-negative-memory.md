---
type: causal-policy
title: "Generic Crash Generic Crash Not Target Match Object File For Objdump Disassembly Negative Memory"
description: "Round 9 negative memory for generic_crash with verifier signal generic_crash_not_target_match."
failure_class: "generic_crash"
verifier_signal: "generic_crash_not_target_match"
candidate_family: "construct"
input_format: "object-file-for-objdump-disassembly"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "generic-crash-not-target-match", "object-file-for-objdump-disassembly", "negative-memory", "round-9"]
match_keys: ["generic_crash", "generic_crash_not_target_match", "object-file-for-objdump-disassembly", "libfuzzer", "uninitialized-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# Generic Crash Generic Crash Not Target Match Object File For Objdump Disassembly Negative Memory

- key: `generic_crash x generic_crash_not_target_match`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[object-file-for-objdump-disassembly]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- One compact object-like candidate crashed locally in fuzz_objdump, so it was submitted.
- The official server did not reproduce a target match, and the other variants were rejected as
  unrecognized object files or exited cleanly.
- The candidates did not reliably reach C-SKY floating-constant operand printing after a read-memory
  failure.

## Policy
Treat `generic_crash x generic_crash_not_target_match` on `object-file-for-objdump-disassembly` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The desired path requires an object accepted by BFD as a C-SKY-disassembled input, with an
  instruction operand classified as a floating constant and placed near a boundary where the
  disassembler read callback fails before all operand bytes are initialized.

## Harness Contract
- The fuzzer writes raw input to a temporary file and invokes objdump-style BFD/disassembler logic
  on it.
- Local verification can show generic wrapper crashes that are not sufficient for official target
  matching.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `generic_crash_not_target_match`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
