---
type: causal-policy
title: "PDF Construct Parser Reached Out Of Bounds Write Verified Recovery"
description: "Round 24 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-ghostscript-gstoraster"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached", "pdf", "libfuzzer-ghostscript-gstoraster", "construct", "verified-recovery", "round-24"]
match_keys: ["generic-crash", "parser-reached", "pdf", "libfuzzer-ghostscript-gstoraster", "out-of-bounds-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# PDF Construct Parser Reached Out Of Bounds Write Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer-ghostscript-gstoraster]]

## Failure Shape
Construct a minimal PDF that causes repair mode to scan an object stream instead of relying on a normal cross-reference table. Keep the object stream syntactically valid, but make its compressed-object number exceed the allocated xref table range so repair writes metadata through an unchecked index. The fixed build rejects the out-of-range object number.

## Policy
For `generic_crash x parser_reached` on `pdf`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `pdf` carrier and `libfuzzer-ghostscript-gstoraster` harness contract until parser reachability is stable.
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
