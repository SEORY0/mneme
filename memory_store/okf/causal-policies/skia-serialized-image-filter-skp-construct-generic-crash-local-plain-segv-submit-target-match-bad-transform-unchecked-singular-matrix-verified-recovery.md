---
type: causal-policy
title: "Skia Serialized Image Filter Skp Construct Generic Crash Local Plain Segv Submit Target Match Bad Transform Unchecked Singular Matrix Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal local_plain_segv_submit_target_match."
failure_class: "generic_crash"
verifier_signal: "local_plain_segv_submit_target_match"
candidate_family: "construct"
input_format: "skia-serialized-image-filter-skp"
harness_convention: "libfuzzer-skia-image-filter-deserialize"
vuln_class: "bad-transform-unchecked-singular-matrix"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "local-plain-segv-submit-target-match", "skia-serialized-image-filter-skp", "libfuzzer-skia-image-filter-deserialize", "construct", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "local-plain-segv-submit-target-match", "skia-serialized-image-filter-skp", "libfuzzer-skia-image-filter-deserialize", "bad-transform-unchecked-singular-matrix"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Skia Serialized Image Filter Skp Construct Generic Crash Local Plain Segv Submit Target Match Bad Transform Unchecked Singular Matrix Verified Recovery

- key: `generic-crash x local-plain-segv-submit-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[skia-serialized-image-filter-skp]]
- harnesses: [[libfuzzer-skia-image-filter-deserialize]]

## Failure Shape
Build a valid serialized Skia image-filter envelope whose top-level object is a picture image filter. The embedded picture must contain a reachable text-RSXform draw op and a paint table entry with a non-null shader, so playback enters the shader-local-matrix path. Trigger the bug by making the per-glyph transform invalid in the way that makes its inverse unavailable while the shader path still consumes that inverse.

## Policy
For `generic-crash x local-plain-segv-submit-target-match` on `skia-serialized-image-filter-skp`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `skia-serialized-image-filter-skp` carrier enough for the `libfuzzer-skia-image-filter-deserialize` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `skia-serialized-image-filter-skp` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
