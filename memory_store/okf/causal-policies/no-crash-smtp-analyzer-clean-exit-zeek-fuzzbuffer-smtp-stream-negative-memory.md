---
type: causal-policy
title: "No Crash Smtp Analyzer Clean Exit Zeek Fuzzbuffer Smtp Stream Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal smtp_analyzer_clean_exit."
failure_class: "no_crash"
verifier_signal: "smtp_analyzer_clean_exit"
candidate_family: "construct"
input_format: "zeek-fuzzbuffer-smtp-stream"
harness_convention: "libfuzzer"
vuln_class: "smtp-bdat-state-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "smtp-analyzer-clean-exit", "zeek-fuzzbuffer-smtp-stream", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "smtp-analyzer-clean-exit", "zeek-fuzzbuffer-smtp-stream", "libfuzzer", "smtp-bdat-state-confusion"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Smtp Analyzer Clean Exit Zeek Fuzzbuffer Smtp Stream Negative Memory

- key: `no_crash x smtp_analyzer_clean_exit`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[zeek-fuzzbuffer-smtp-stream]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Constructed SMTP FuzzBuffer streams reached the analyzer harness but did not turn BDAT/DATA state confusion into a sanitizer-visible failure. Server replies during in-flight BDAT chunks and LAST/non-LAST variants exited cleanly.

## Policy
For `no_crash x smtp_analyzer_clean_exit` on `zeek-fuzzbuffer-smtp-stream`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x smtp_analyzer_clean_exit` appears for `zeek-fuzzbuffer-smtp-stream`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
