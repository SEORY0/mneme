---
type: causal-policy
title: "Bmp Construct Target Stack Reached Despite Local Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal target_stack_reached_despite_local_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "target_stack_reached_despite_local_sink_mismatch"
candidate_family: "construct"
input_format: "bmp"
harness_convention: "libfuzzer-mupdf-document-renderer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "target-stack-reached-despite-local-sink-mismatch", "bmp", "libfuzzer-mupdf-document-renderer", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "target-stack-reached-despite-local-sink-mismatch", "bmp", "libfuzzer-mupdf-document-renderer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Bmp Construct Target Stack Reached Despite Local Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x target_stack_reached_despite_local_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[bmp]]
- harnesses: [[libfuzzer-mupdf-document-renderer]]

## Failure Shape
Use a raw BMP accepted by MuPDF content sniffing. Choose a palette-bearing Windows BMP header with a valid small image shape, declare the bitmap-data position far beyond the actual buffer, and provide too little palette/pixel data. The vulnerable parser computes the palette span from the unchecked bitmap-data position before later clamping it.

## Policy
For `wrong_sink x target_stack_reached_despite_local_sink_mismatch` on `bmp`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `bmp` carrier enough for the `libfuzzer-mupdf-document-renderer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `bmp` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 10 attempts.
- Scope: generator repair only.
