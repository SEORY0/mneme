---
type: causal-policy
title: "No Crash MNG Jng Parser Accepts Or Returns Null Without Crash Jng Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal mng_jng_parser_accepts_or_returns_null_without_crash."
failure_class: "no_crash"
verifier_signal: "mng_jng_parser_accepts_or_returns_null_without_crash"
candidate_family: "seed_mutate"
input_format: "jng"
harness_convention: "afl raw stdin/file bytes"
vuln_class: "missing-jng-color-image-error-reporting"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mng-jng-parser-accepts-or-returns-null-without-crash", "jng", "afl-raw-stdin-file-bytes", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "mng-jng-parser-accepts-or-returns-null-without-crash", "jng", "afl-raw-stdin-file-bytes", "missing-jng-color-image-error-reporting"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash MNG Jng Parser Accepts Or Returns Null Without Crash Jng Negative Memory

- key: `no_crash x mng_jng_parser_accepts_or_returns_null_without_crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[jng]]
- harnesses: [[afl-raw-stdin-file-bytes]]

## Dead-End Shape
Real JNG samples and mutations that removed or varied color/alpha image chunks remained no-crash. The parser either handled valid samples or returned without a sanitizer-visible failure when color image chunks were missing.

## Policy
For `no_crash x mng_jng_parser_accepts_or_returns_null_without_crash` on `jng`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x mng_jng_parser_accepts_or_returns_null_without_crash` appears for `jng`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
