---
type: causal-policy
title: "PDF Construct Parser Reached Target Stack Local Mismatch Stack Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_target_stack_local_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_local_mismatch"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-qpdf"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-local-mismatch", "pdf", "libfuzzer-qpdf", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_target_stack_local_mismatch", "pdf", "libfuzzer-qpdf", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# PDF Construct Parser Reached Target Stack Local Mismatch Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_stack_local_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer-qpdf]]

## Failure Shape
Build a minimal PDF that reaches classic xref-table parsing: recognizable header, xref section, trailer, and a coherent startxref pointer. Keep the active xref entry on the fixed-size table-entry fast path, but make a zero-only numeric field overlong enough that the parser's post-field newline probe advances outside the stack buffer.

## Policy
For `wrong_sink x parser_reached_target_stack_local_mismatch` on `pdf`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `pdf` carrier and `libfuzzer-qpdf` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
Classic PDF xref tables consist of a header, subsections, fixed-width numeric entry fields with an in-use/free marker, a trailer dictionary, and a startxref pointer back to the xref section. Early xref processing can be reached with a very small document when those structural gates are coherent.

## Harness Contract
The qpdf fuzz target consumes raw PDF bytes through a buffer-backed input source. There is no leading selector or FuzzedDataProvider layout; object creation parses startxref and xref data before later page or outline checks.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
