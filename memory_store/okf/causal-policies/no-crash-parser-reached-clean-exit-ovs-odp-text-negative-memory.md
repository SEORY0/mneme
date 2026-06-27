---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Ovs Odp Text Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "ovs-odp-text"
harness_convention: "libfuzzer"
vuln_class: "overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "parser_reached_clean_exit", "ovs-odp-text", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Parser Reached Clean Exit Ovs Odp Text Negative Memory

## Policy
For `no_crash x parser_reached_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. The ODP text parser accepted several nested key/action forms and formatted them cleanly.
2. When `no_crash x parser_reached_clean_exit` appears for `ovs-odp-text`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The selected target consumes a single NUL-terminated OVS datapath text string. It rejects very short inputs, embedded newlines, and inputs without a trailing terminator. The same string is tried as an ODP key, wildcard key, and action list; nested attributes are expressed textually with parenthesized encap-style clauses.
- Harness: Raw libFuzzer bytes are interpreted directly as a C string. There is no archive or file envelope despite the coarse card; parser reachability depends on a final terminator and no newline.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
