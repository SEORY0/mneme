---
type: causal-policy
title: "PDF Construct Parser Reached Target Clip Stack Heap Buffer Overflow Write Verified Recovery"
description: "Round 24 verified recovery for wrong_sink with verifier signal parser_reached_target_clip_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_clip_stack"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-clip-stack", "pdf", "libfuzzer", "construct", "verified-recovery", "round-24"]
match_keys: ["wrong-sink", "parser-reached-target-clip-stack", "pdf", "libfuzzer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# PDF Construct Parser Reached Target Clip Stack Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_target_clip_stack`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a minimal renderable PDF with catalog, pages, one page, and a content stream. Put repeated clipping path operations in the content stream so rendering pushes more clip marks than the vulnerable layer/clip stack tracks before checking depth; the fixed build enforces the nesting limit cleanly.

## Policy
For `wrong_sink x parser_reached_target_clip_stack` on `pdf`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `pdf` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 1 attempts.
- Scope: generator repair and retargeting only.
