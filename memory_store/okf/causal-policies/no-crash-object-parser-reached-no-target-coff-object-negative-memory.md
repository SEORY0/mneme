---
type: causal-policy
title: "No Crash Object Parser Reached No Target Coff Object Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal object_parser_reached_no_target."
failure_class: "no_crash"
verifier_signal: "object_parser_reached_no_target"
candidate_family: "construct"
input_format: "coff-object"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "object-parser-reached-no-target", "coff-object", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "object-parser-reached-no-target", "coff-object", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Object Parser Reached No Target Coff Object Negative Memory

- key: `no_crash x object_parser_reached_no_target`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[coff-object]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Constructed COFF objects reached symbol-table parsing and could make objdump-style diagnostics report an unrecognized storage class for a long symbol name, but the benchmark wrapper still exited cleanly. The missing condition appears to be the debug-section string-table layout used by the vulnerable diagnostic path rather than the ordinary COFF string table alone.

## Policy
For `no_crash x object_parser_reached_no_target` on `coff-object`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x object_parser_reached_no_target` appears for `coff-object`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
