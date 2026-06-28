---
type: causal-policy
title: "No Crash Parser Not Reached Or Clean Exit Libxml2 Valid Fuzzer Entity Envelope Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_clean_exit"
candidate_family: "construct"
input_format: "libxml2 valid-fuzzer entity envelope"
harness_convention: "libfuzzer"
vuln_class: "libxml2 EBCDIC push-parser boundary"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-clean-exit", "libxml2-valid-fuzzer-entity-envelope", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached_or_clean_exit", "libxml2 valid-fuzzer entity envelope", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Or Clean Exit Libxml2 Valid Fuzzer Entity Envelope Negative Memory

## Policy
For `no_crash x parser_not_reached_or_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Initial raw XML/EBCDIC attempts missed the valid-fuzzer envelope. After correcting the envelope to include parser options, allocation limit, URL/entity separation, and document termination, EBCDIC-detection boundary lengths still exited cleanly under official submit. The likely missing condition is a precise push-buffer refill boundary that makes EBCDIC detection and encoding-handler setup disagree.
- When `no_crash x parser_not_reached_or_clean_exit` appears for `libxml2 valid-fuzzer entity envelope`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The valid fuzzer wraps XML-like data in an entity envelope rather than passing a standalone document. The beginning contains parser option and allocation-limit fields, followed by entity strings separated by a backslash-newline sentinel; the first entity acts as the main document. EBCDIC detection is driven by the initial document signature and by the amount of buffered input available to the push parser.
- Harness: The libxml2 valid fuzzer consumes fixed-size option fields first, configures validation-oriented parsing, then reads entity strings from the remaining bytes. Raw XML bytes without this envelope do not exercise the same parser path.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
