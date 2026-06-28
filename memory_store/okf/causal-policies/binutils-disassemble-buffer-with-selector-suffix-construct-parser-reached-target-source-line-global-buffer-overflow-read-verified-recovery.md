---
type: causal-policy
title: "Binutils Disassemble Buffer With Selector Suffix Construct Parser Reached Target Source Line Global Buffer Overflow Read Verified Recovery"
description: "Round 21 verified recovery for wrong-sink with verifier signal parser-reached-target-source-line."
failure_class: "wrong-sink"
verifier_signal: "parser-reached-target-source-line"
candidate_family: "construct"
input_format: "binutils-disassemble-buffer-with-selector-suffix"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-source-line", "binutils-disassemble-buffer-with-selector-suffix", "libfuzzer", "construct", "verified-recovery", "round-21"]
match_keys: ["wrong-sink", "parser-reached-target-source-line", "binutils-disassemble-buffer-with-selector-suffix", "libfuzzer", "global-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Binutils Disassemble Buffer With Selector Suffix Construct Parser Reached Target Source Line Global Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-target-source-line`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[binutils-disassemble-buffer-with-selector-suffix]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the harness suffix to select the V850E3V5 disassembler, then provide a system-register instruction whose encoded selector expands the logical system-register index beyond the legacy name table. The vulnerable printer indexes the name table without bounding the combined selector/register value.

## Policy
For `wrong-sink x parser-reached-target-source-line` on `binutils-disassemble-buffer-with-selector-suffix`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `binutils-disassemble-buffer-with-selector-suffix` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `binutils-disassemble-buffer-with-selector-suffix` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 1 attempts.
- Scope: generator repair only.
