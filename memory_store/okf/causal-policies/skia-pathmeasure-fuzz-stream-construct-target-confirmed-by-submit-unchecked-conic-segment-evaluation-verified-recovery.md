---
type: causal-policy
title: "SKIA Pathmeasure Fuzz Stream Construct Target Confirmed By Submit Unchecked Conic Segment Evaluation Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "target_confirmed_by_submit"
candidate_family: "construct"
input_format: "skia-pathmeasure-fuzz-stream"
harness_convention: "libfuzzer"
vuln_class: "unchecked-conic-segment-evaluation"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-confirmed-by-submit", "skia-pathmeasure-fuzz-stream", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "target_confirmed_by_submit", "skia-pathmeasure-fuzz-stream", "libfuzzer", "unchecked-conic-segment-evaluation", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# SKIA Pathmeasure Fuzz Stream Construct Target Confirmed By Submit Unchecked Conic Segment Evaluation Verified Recovery

- key: `generic_crash x target_confirmed_by_submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[skia-pathmeasure-fuzz-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the raw Skia path-measure stream contract: a small scalar/control prefix followed by path-building verbs. Build a path containing a move and a conic segment, then request an interior segment interval so the vulnerable path-measure code asks the conic chopping/evaluation routine for a subsegment whose evaluation fails. The vulnerable build uses the failed result without checking; the fixed build rejects or avoids that use.

## Policy
For `generic_crash x target_confirmed_by_submit` on `skia-pathmeasure-fuzz-stream`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `skia-pathmeasure-fuzz-stream` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `skia-pathmeasure-fuzz-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The fuzz input is a compact Skia path stream rather than a serialized image. The leading control byte selects path-measure options, several little-endian scalar fields configure distance and query behavior, and the remaining bytes are consumed as path verbs and coordinates. Conic path records include endpoints and a weight; segment extraction can later request only a subrange of that curve.

## Harness Contract
The harness feeds libFuzzer bytes directly to the Skia path-measure fuzzer. It consumes fields front-to-back through Skia's fuzz helper, with no file wrapper, checksum, mode selector outside the stream, or FuzzedDataProvider back-consumed fields.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 5 attempts.
- Scope: generator repair and retargeting only.
