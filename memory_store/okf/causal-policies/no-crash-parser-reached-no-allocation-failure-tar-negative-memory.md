---
type: causal-policy
title: "No Crash Parser Reached No Allocation Failure Tar Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_reached_no_allocation_failure."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_allocation_failure"
candidate_family: "seed_mutate"
input_format: "tar"
harness_convention: "libfuzzer"
vuln_class: "excessive-memory-allocation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-allocation-failure", "tar", "libfuzzer", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-reached-no-allocation-failure", "tar", "libfuzzer", "excessive-memory-allocation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Reached No Allocation Failure Tar Negative Memory

- key: `no_crash x parser_reached_no_allocation_failure`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[tar]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Tar inputs with a real small raster and multiple oversized output-shape option families were accepted but stayed under the fuzzer guard or were rejected by GDALTranslate option validation. The successful trigger likely needs an option path not covered by the prepended output-size limit or a source dataset whose metadata expands allocation after the source-size precheck.

## Policy
For `no_crash x parser_reached_no_allocation_failure` on `tar`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_reached_no_allocation_failure` appears for `tar`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
