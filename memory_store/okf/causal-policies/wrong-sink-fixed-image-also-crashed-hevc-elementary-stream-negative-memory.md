---
type: causal-policy
title: "Wrong Sink Fixed Image Also Crashed Hevc Elementary Stream Negative Memory"
description: "Round 24 negative memory for wrong_sink with verifier signal fixed_image_also_crashed."
failure_class: "wrong_sink"
verifier_signal: "fixed_image_also_crashed"
candidate_family: "seed_sweep"
input_format: "hevc-elementary-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "fixed-image-also-crashed", "hevc-elementary-stream", "libfuzzer", "seed-sweep", "negative-memory", "round-24"]
match_keys: ["wrong-sink", "fixed-image-also-crashed", "hevc-elementary-stream", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# Wrong Sink Fixed Image Also Crashed Hevc Elementary Stream Negative Memory

- key: `wrong_sink x fixed_image_also_crashed`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[hevc-elementary-stream]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Seed-corpus HEVC elementary streams reached decoder setup, and one reached an uninitialized-value decoder path, but the official fixed image also failed, so the candidate was overbroad or off-target for the SAO CTB shift issue.

## Policy
For `wrong_sink x fixed_image_also_crashed` on `hevc-elementary-stream`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_sweep` only while this format and harness contract are present.

## Procedure
1. When `wrong_sink x fixed_image_also_crashed` appears for `hevc-elementary-stream`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
