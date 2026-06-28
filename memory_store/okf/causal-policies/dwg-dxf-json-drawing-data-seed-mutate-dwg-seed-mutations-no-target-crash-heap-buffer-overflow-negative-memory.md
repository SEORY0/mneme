---
type: causal-policy
title: Dwg Dxf Json Drawing Data Dwg Seed Mutations No Target Crash Negative Memory
description: Negative memory for dwg/dxf/json drawing data candidates that ended in no_crash with verifier signal `dwg_seed_mutations_no_target_crash`.
failure_class: no_crash
verifier_signal: dwg_seed_mutations_no_target_crash
candidate_family: seed_mutate
input_format: dwg/dxf/json drawing data
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, dwg-seed-mutations-no-target-crash, dwg-dxf-json-drawing-data, libfuzzer, seed-mutate, heap-buffer-overflow, negative-memory]
match_keys: [no-crash, dwg-seed-mutations-no-target-crash, dwg-dxf-json-drawing-data, libfuzzer, seed-mutate, heap-buffer-overflow, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `dwg_seed_mutations_no_target_crash`` for `dwg/dxf/json drawing data` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `dwg_seed_mutations_no_target_crash`.
2. Stop repeating the dead-end basin: Real DWG seed files and coarse object-size mutations decoded or were rejected without reaching the vulnerable R13 object-size handling. The missing condition is a coherent R13 object table and object stream where a specific object advertises an invalid size that survives the section/table gates and is later used during decode/encode output.
3. Rebuild around `[[dwg-dxf-json-drawing-data]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.
