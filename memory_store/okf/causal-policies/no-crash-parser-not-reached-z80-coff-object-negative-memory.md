---
type: causal-policy
title: "No Crash Parser Not Reached Z80 Coff Object Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "z80-coff-object"
harness_convention: "honggfuzz-objdump-wrapper"
vuln_class: "relocation-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "z80-coff-object", "honggfuzz-objdump-wrapper", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-not-reached", "z80-coff-object", "honggfuzz-objdump-wrapper", "relocation-overflow"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Not Reached Z80 Coff Object Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[z80-coff-object]]
- harnesses: [[honggfuzz-objdump-wrapper]]

## Dead-End Shape
Minimal COFF headers with z80 magic, one text section, symbols, and relocation entries were not recognized by the objdump wrapper. Variants changed section name spelling, byte order, relocation type, relocation address, and section size, but did not reach the z80 relocation backend.

## Policy
For `no_crash x parser_not_reached` on `z80-coff-object`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_not_reached` appears for `z80-coff-object`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
