---
type: causal-policy
title: "No Crash Parser Rejected Or Clean Without Clip Verts Sink Dxf Or Json Cad Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_rejected_or_clean_without_clip_verts_sink."
failure_class: "no_crash"
verifier_signal: "parser_rejected_or_clean_without_clip_verts_sink"
candidate_family: "construct"
input_format: "dxf-or-json-cad"
harness_convention: "libfuzzer"
vuln_class: "improper-dxf-clip-vertex-count-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-rejected-or-clean-without-clip-verts-sink", "dxf-or-json-cad", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-rejected-or-clean-without-clip-verts-sink", "dxf-or-json-cad", "libfuzzer", "improper-dxf-clip-vertex-count-handling"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Rejected Or Clean Without Clip Verts Sink Dxf Or Json Cad Negative Memory

- key: `no_crash x parser_rejected_or_clean_without_clip_verts_sink`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[dxf-or-json-cad]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Minimal DXF WIPEOUT and JSON drawing variants did not reach the unstable class import path or did not create the internal clip_verts/count relation needed before allocation.

## Policy
For `no_crash x parser_rejected_or_clean_without_clip_verts_sink` on `dxf-or-json-cad`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_rejected_or_clean_without_clip_verts_sink` appears for `dxf-or-json-cad`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
