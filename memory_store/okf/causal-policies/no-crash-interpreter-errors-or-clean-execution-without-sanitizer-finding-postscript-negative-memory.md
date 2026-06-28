---
type: causal-policy
title: "No Crash Interpreter Errors Or Clean Execution Without Sanitizer Finding Postscript Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal interpreter errors or clean execution without sanitizer finding."
failure_class: "no_crash"
verifier_signal: "interpreter errors or clean execution without sanitizer finding"
candidate_family: "construct"
input_format: "postscript"
harness_convention: "libfuzzer gstoraster stdin"
vuln_class: "postscript-stack-state-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "interpreter-errors-or-clean-execution-without-sanitizer-finding", "postscript", "libfuzzer-gstoraster-stdin", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "interpreter-errors-or-clean-execution-without-sanitizer-finding", "postscript", "libfuzzer-gstoraster-stdin", "postscript-stack-state-confusion"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Interpreter Errors Or Clean Execution Without Sanitizer Finding Postscript Negative Memory

- key: `no_crash x interpreter errors or clean execution without sanitizer finding`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[postscript]]
- harnesses: [[libfuzzer-gstoraster-stdin]]

## Dead-End Shape
Bare unmatched array closes and stopped-procedure contexts reached Ghostscript but only produced normal PostScript error recovery. The missing trigger is a higher-level operator continuation whose operands must survive the array-close recovery path after array construction fails.

## Policy
For `no_crash x interpreter errors or clean execution without sanitizer finding` on `postscript`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x interpreter errors or clean execution without sanitizer finding` appears for `postscript`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
