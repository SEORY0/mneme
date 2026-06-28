---
type: causal-policy
title: "No Crash Parser Accepted Or Rejected Inputs Without Target Crash Rar5 Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser accepted or rejected inputs without target crash."
failure_class: "no_crash"
verifier_signal: "parser accepted or rejected inputs without target crash"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "afl/libfuzzer libarchive archive reader"
vuln_class: "logic-error-directory-entry-unpack"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-accepted-or-rejected-inputs-without-target-crash", "rar5", "afl-libfuzzer-libarchive-archive-reader", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-accepted-or-rejected-inputs-without-target-crash", "rar5", "afl-libfuzzer-libarchive-archive-reader", "logic-error-directory-entry-unpack"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Accepted Or Rejected Inputs Without Target Crash Rar5 Negative Memory

- key: `no_crash x parser accepted or rejected inputs without target crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[rar5]]
- harnesses: [[afl-libfuzzer-libarchive-archive-reader]]

## Dead-End Shape
Real RAR5 seeds, a header mutation, truncation, and a minimal RAR5 envelope all exercised the archive reader but did not create an entry marked as a directory that was still routed into unpacking data. The likely missing ingredient is a coherent RAR5 file-service header combination rather than generic archive reachability.

## Policy
For `no_crash x parser accepted or rejected inputs without target crash` on `rar5`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser accepted or rejected inputs without target crash` appears for `rar5`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
