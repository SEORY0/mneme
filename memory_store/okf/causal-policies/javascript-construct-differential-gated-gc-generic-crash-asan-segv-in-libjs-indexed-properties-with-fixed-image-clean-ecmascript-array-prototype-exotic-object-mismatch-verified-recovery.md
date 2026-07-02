---
type: causal-policy
title: "Javascript Construct Differential Gated Gc Generic Crash Asan Segv In Libjs Indexed Properties With Fixed Image Clean Ecmascript Array Prototype Exotic Object Mismatch Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal asan_segv_in_libjs_indexed_properties_with_fixed_image_clean."
failure_class: "generic_crash"
verifier_signal: "asan_segv_in_libjs_indexed_properties_with_fixed_image_clean"
candidate_family: "construct_differential_gated_gc"
input_format: "javascript"
harness_convention: "libfuzzer"
vuln_class: "ecmascript-array-prototype-exotic-object-mismatch"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "asan-segv-in-libjs-indexed-properties-with-fixed-image-clean", "javascript", "libfuzzer", "construct-differential-gated-gc", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "asan-segv-in-libjs-indexed-properties-with-fixed-image-clean", "javascript", "libfuzzer", "ecmascript-array-prototype-exotic-object-mismatch"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Javascript Construct Differential Gated Gc Generic Crash Asan Segv In Libjs Indexed Properties With Fixed Image Clean Ecmascript Array Prototype Exotic Object Mismatch Verified Recovery

- key: `generic-crash x asan-segv-in-libjs-indexed-properties-with-fixed-image-clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[javascript]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use plain JavaScript source that first tests whether the built-in Array prototype is recognized as an Array exotic object. In the vulnerable build, enter a nested allocation and explicit garbage-collection sequence that stresses array literal creation after temporary container churn, producing a native IndexedProperties crash. In the fixed build, the predicate is false for the vulnerable-only branch, so the stress path is skipped and execution exits cleanly.

## Policy
For `generic-crash x asan-segv-in-libjs-indexed-properties-with-fixed-image-clean` on `javascript`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct-differential-gated-gc` while this format and harness contract are present.

## Procedure
1. Preserve the `javascript` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `javascript` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
