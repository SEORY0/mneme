---
type: causal-policy
title: Object Alpha ECOFF Relocation Bounds Recovery
description: Verified recovery for generic_crash with server_target_match on object-file inputs.
failure_class: generic_crash
verifier_signal: server_target_match
candidate_family: seed_mutate
input_format: object-file
harness_convention: libfuzzer
vuln_class: buffer-overflow-read-write
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, server-target-match, seed-mutate, object-file, buffer-overflow-read-write, verified-recovery]
match_keys: [generic-crash, server-target-match, object-file, buffer-overflow-read-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Object Alpha ECOFF Relocation Bounds Recovery

- key: `generic_crash x server_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[object-file]]

## Failure Shape
Use a compact BFD extension seed that selects an Alpha ECOFF-style relocation path in
objdump-safe. The malformed relocation metadata violates the invariant that relocation
offsets must be range-checked against section contents before relocation-specific reads and
writes are applied.

## Policy
For `generic_crash x server_target_match` on `object-file`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `seed_mutate`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Start from a compact object-file seed that selects the Alpha ECOFF-style relocation path.
2. Keep object recognition and section ownership valid enough for objdump-safe traversal.
3. Mutate relocation metadata so relocation offsets are applied without the required range
check against section contents.
4. When a generic crash follows a clean parse, submit if the official server can distinguish
vulnerable and fixed relocation handling.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not switch object families after backend recognition is proven.
- Do not use a generic malformed object envelope that fails before relocation-specific reads
and writes.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
