---
type: causal-policy
title: "No Crash Official Vulnerable Clean Cr2 Tiff Raw Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal official_vulnerable_clean."
failure_class: "no_crash"
verifier_signal: "official_vulnerable_clean"
candidate_family: "construct"
input_format: "cr2-tiff-raw"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-memory-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "official-vulnerable-clean", "cr2-tiff-raw", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "official-vulnerable-clean", "cr2-tiff-raw", "libfuzzer", "uninitialized-memory-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Official Vulnerable Clean Cr2 Tiff Raw Negative Memory

- key: `no_crash x official_vulnerable_clean`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[cr2-tiff-raw]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
A synthetic RawSpeed decompressor envelope produced a weak local wrapper crash but did not reproduce as an official vulnerable-image failure; the active harness was the CR2 TIFF decoder, not the direct decompressor envelope shape.

## Policy
For `no_crash x official_vulnerable_clean` on `cr2-tiff-raw`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x official_vulnerable_clean` appears for `cr2-tiff-raw`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
