---
type: negative-memory
title: "No Crash Disassembler Clean Exit Binutils Disassembler Selector Plus Instruction Bytes Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal disassembler_clean_exit."
failure_class: "no_crash"
verifier_signal: "disassembler_clean_exit"
candidate_family: "construct_x86_disassembler_suffix_and_opcode_sweep"
input_format: "binutils-disassembler-selector-plus-instruction-bytes"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "disassembler-clean-exit", "binutils-disassembler-selector-plus-instruction-bytes", "libfuzzer", "construct-x86-disassembler-suffix-and-opcode-sweep", "negative-memory", "round-19"]
match_keys: ["no-crash", "disassembler-clean-exit", "binutils-disassembler-selector-plus-instruction-bytes", "libfuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Disassembler Clean Exit Binutils Disassembler Selector Plus Instruction Bytes Negative Memory

- key: `no_crash x disassembler_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[binutils-disassembler-selector-plus-instruction-bytes]]
- harnesses: [[libfuzzer]]

## Failure Shape
The instruction-buffer plus selector-tail contract was recovered and many i386 machine/flavour combinations with prefetch-reserved opcode families were exercised, but no candidate reproduced the described print_insn boundary condition. The likely missing relation is the exact architecture variant or operand-size state that maps the reserved opcode form to the vulnerable decoder table entry.

## Policy
Treat `no_crash x disassembler_clean_exit` on `binutils-disassembler-selector-plus-instruction-bytes` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
