---
type: causal-policy
title: "No Crash Decoder Rejected Or Clean After Seed Sweep Av1 Ivf Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal decoder_rejected_or_clean_after_seed_sweep."
failure_class: "no_crash"
verifier_signal: "decoder_rejected_or_clean_after_seed_sweep"
candidate_family: "seed_sweep"
input_format: "av1-ivf"
harness_convention: "libfuzzer"
vuln_class: "incorrect-reference-frame-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-rejected-or-clean-after-seed-sweep", "av1-ivf", "libfuzzer", "seed-sweep", "negative-memory", "round-24"]
match_keys: ["no-crash", "decoder-rejected-or-clean-after-seed-sweep", "av1-ivf", "libfuzzer", "incorrect-reference-frame-state"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Decoder Rejected Or Clean After Seed Sweep Av1 Ivf Negative Memory

- key: `no_crash x decoder_rejected_or_clean_after_seed_sweep`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[av1-ivf]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Existing AV1 decoder corpus entries and minimized IVF-like seeds reached the fuzzer wrapper but did not drive the reference-frame map/state transition needed for a sanitizer-visible differential.

## Policy
For `no_crash x decoder_rejected_or_clean_after_seed_sweep` on `av1-ivf`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_sweep` only while this format and harness contract are present.

## Procedure
1. When `no_crash x decoder_rejected_or_clean_after_seed_sweep` appears for `av1-ivf`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
