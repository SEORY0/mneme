---
type: causal-policy
title: "CIL Policy Text Construct From Repo Examples Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal target_heap_use_after_free."
failure_class: "generic_crash"
verifier_signal: "target_heap_use_after_free"
candidate_family: "construct_from_repo_examples"
input_format: "CIL policy text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-heap-use-after-free", "cil-policy-text", "construct-from-repo-examples", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "target_heap_use_after_free", "CIL policy text", "libfuzzer", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# CIL Policy Text Construct From Repo Examples Verified Recovery

## Policy
For `generic_crash x target_heap_use_after_free`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal valid CIL policy with the required class, sid, user, role, type, category, sensitivity, and context declarations. Declare a classpermission outside an optional block, populate it via a classpermissionset inside an optional that is later disabled by an unresolved rule, then reference the classpermission after the reset. Reset keeps a stale classperms list and later classpermission verification reads freed storage.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- CIL policy text uses parenthesized declarations. A classpermission declaration can be populated by classpermissionset rules, and classpermissionset bodies name class/permission pairs. Optional blocks can be disabled during resolution when a contained declaration or rule fails to resolve.
- Harness: The libFuzzer harness treats the input as raw CIL source, adds it as a policy file, compiles it, builds and optimizes a policydb, and writes the result to a null output. Triggering this bug requires reaching compile-time resolution and verification, not policydb serialization alone.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
