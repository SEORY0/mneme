---
type: causal-policy
title: "Rar5 Seed Mutate Generic Crash Parser Reached Target Arm Filter Oob Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal parser_reached_target_arm_filter_oob."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_arm_filter_oob"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-target-arm-filter-oob", "rar5", "libfuzzer", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "parser-reached-target-arm-filter-oob", "rar5", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Rar5 Seed Mutate Generic Crash Parser Reached Target Arm Filter Oob Heap Buffer Overflow Read Verified Recovery

- key: `generic-crash x parser-reached-target-arm-filter-oob`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[rar5]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a real RAR5 archive that already exercises ARM filters. Preserve the base-block header CRC gates while marking the archive solid, then keep one intact member first so decompression advances the circular window base. Replay a member whose content checksum gate is neutralized, and minimally shift an ARM filter descriptor so the descriptor ordering remains valid but the filter no longer begins on the natural four-byte alignment. When that shifted ARM filter runs with the nonzero solid-window base, the vulnerable contiguous lookahead crosses the end of the circular window allocation; the fixed build avoids the out-of-window read.

## Policy
For `generic-crash x parser-reached-target-arm-filter-oob` on `rar5`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `rar5` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `rar5` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
