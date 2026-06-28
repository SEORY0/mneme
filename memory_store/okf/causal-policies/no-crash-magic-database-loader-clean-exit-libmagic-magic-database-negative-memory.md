---
type: causal-policy
title: "No Crash Magic Database Loader Clean Exit Libmagic Magic Database Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal magic_database_loader_clean_exit."
failure_class: "no_crash"
verifier_signal: "magic_database_loader_clean_exit"
candidate_family: "construct"
input_format: "libmagic-magic-database"
harness_convention: "file-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "magic-database-loader-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "magic_database_loader_clean_exit", "libmagic-magic-database", "file-fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Magic Database Loader Clean Exit Libmagic Magic Database Negative Memory

## Policy
For `no_crash x magic_database_loader_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Valid and malformed strength annotations reached the magic database loader and dump/check path without tripping the raw string-value print or end-of-string increment bug.
2. When `no_crash x magic_database_loader_clean_exit` appears for `libmagic-magic-database`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The active input is a textual magic database, not arbitrary bytes to classify. Rules contain an offset expression, a type/test, a message, and optional annotation lines such as strength adjustments; the loader compiles these into magic entries before dumping or checking them.
- Harness: The verifier invokes the libmagic load-database fuzzer on the raw file as a magic rules file. It reports parser warnings for invalid rule syntax but accepts simple valid rules; there is no separate mode selector.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
