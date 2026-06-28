---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailing Selectors Construct Parser Reached Print Insn Arm Undefined Behavior Out Of Bounds Read Verified Recovery"
description: "Round 19 verified recovery for wrong_sink with verifier signal parser_reached_print_insn_arm_undefined_behavior."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_print_insn_arm_undefined_behavior"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailing-selectors"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-print-insn-arm-undefined-behavior", "binutils-disassembler-buffer-with-trailing-selectors", "libfuzzer", "construct", "verified-recovery", "round-19"]
match_keys: ["wrong-sink", "parser-reached-print-insn-arm-undefined-behavior", "binutils-disassembler-buffer-with-trailing-selectors", "libfuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# Binutils Disassembler Buffer With Trailing Selectors Construct Parser Reached Print Insn Arm Undefined Behavior Out Of Bounds Read Verified Recovery

- key: `wrong_sink x parser_reached_print_insn_arm_undefined_behavior`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[binutils-disassembler-buffer-with-trailing-selectors]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the disassembler harness contract rather than an object-file format: put an ARM instruction encoding in the disassembly buffer and set the trailing selector fields so the harness dispatches to the ARM disassembler. The chosen instruction form drives the ARM printer into the vulnerable table/index path; the patched image rejects or avoids that out-of-bounds access.

## Policy
For `wrong_sink x parser_reached_print_insn_arm_undefined_behavior` on `binutils-disassembler-buffer-with-trailing-selectors`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `binutils-disassembler-buffer-with-trailing-selectors` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `binutils-disassembler-buffer-with-trailing-selectors` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
