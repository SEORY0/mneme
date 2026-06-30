---
type: causal-policy
title: "Bmp Construct Generic Crash Parser Reached Reframe Img Wrapped Row Stride Heap Buffer Overflow Write Integer Overflow To Heap Buffer Overflow Write Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal parser_reached_reframe_img_wrapped_row_stride_heap_buffer_overflow_write."
failure_class: "generic_crash"
verifier_signal: "parser_reached_reframe_img_wrapped_row_stride_heap_buffer_overflow_write"
candidate_family: "construct"
input_format: "bmp"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-to-heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-reframe-img-wrapped-row-stride-heap-buffer-overflow-write", "bmp", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "parser-reached-reframe-img-wrapped-row-stride-heap-buffer-overflow-write", "bmp", "libfuzzer", "integer-overflow-to-heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Bmp Construct Generic Crash Parser Reached Reframe Img Wrapped Row Stride Heap Buffer Overflow Write Integer Overflow To Heap Buffer Overflow Write Verified Recovery

- key: `generic-crash x parser-reached-reframe-img-wrapped-row-stride-heap-buffer-overflow-write`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[bmp]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a minimal uncompressed BMP with valid file and DIB headers, select the 24-bit raw-image branch, and declare an image width whose bytes-per-row multiplication wraps in the vulnerable 32-bit arithmetic while keeping the physical payload tiny. The vulnerable reframer allocates using the wrapped size and then copies one decoded pixel row into that undersized output buffer; the fixed build rejects the unsafe dimension relation.

## Policy
For `generic-crash x parser-reached-reframe-img-wrapped-row-stride-heap-buffer-overflow-write` on `bmp`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `bmp` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `bmp` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
