---
type: causal-policy
title: "MNG Construct Parser Reached Target Chunk Reader Heap Buffer Overflow Read Verified Recovery"
description: "Round 24 verified recovery for wrong_sink with verifier signal parser_reached_target_chunk_reader."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_chunk_reader"
candidate_family: "construct"
input_format: "mng"
harness_convention: "afl-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-chunk-reader", "mng", "afl-file", "construct", "verified-recovery", "round-24"]
match_keys: ["wrong-sink", "parser-reached-target-chunk-reader", "mng", "afl-file", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# MNG Construct Parser Reached Target Chunk Reader Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_chunk_reader`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mng]]
- harnesses: [[afl-file]]

## Failure Shape
Build a minimal valid MNG envelope with a stream signature, image header chunk, a DISC control chunk whose body length violates the even-pair invariant by the smallest margin, and a terminal chunk. Keep PNG-style chunk framing coherent so the vulnerable reader allocates the DISC body and then reads a pair member past the end; the fixed reader rejects the odd DISC length cleanly.

## Policy
For `wrong_sink x parser_reached_target_chunk_reader` on `mng`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `mng` carrier and `afl-file` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `mng` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 1 attempts.
- Scope: generator repair and retargeting only.
