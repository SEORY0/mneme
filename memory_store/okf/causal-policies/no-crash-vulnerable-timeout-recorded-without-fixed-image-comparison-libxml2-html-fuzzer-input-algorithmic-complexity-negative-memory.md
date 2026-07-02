---
type: causal-policy
title: "No Crash Vulnerable Timeout Recorded Without Fixed Image Comparison Libxml2 Html Fuzzer Input Algorithmic Complexity Negative Memory"
description: "Negative memory for persistent no_crash / vulnerable_timeout_recorded_without_fixed_image_comparison basin."
failure_class: "no_crash"
verifier_signal: "vulnerable_timeout_recorded_without_fixed_image_comparison"
candidate_family: "construct"
input_format: "libxml2-html-fuzzer-input"
harness_convention: "libfuzzer-libxml2-html-push-parser"
vuln_class: "algorithmic-complexity"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct", "libxml2-html-fuzzer-input", "algorithmic-complexity", "negative-memory"]
match_keys: ["no-crash", "vulnerable-timeout-recorded-without-fixed-image-comparison", "libxml2-html-fuzzer-input", "libfuzzer-libxml2-html-push-parser", "algorithmic-complexity", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Vulnerable Timeout Recorded Without Fixed Image Comparison Libxml2 Html Fuzzer Input Algorithmic Complexity Negative Memory

## Policy
For `no_crash` with verifier signal `vulnerable_timeout_recorded_without_fixed_image_comparison` on `libxml2-html-fuzzer-input` under `libfuzzer-libxml2-html-push-parser`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- Several targeted push-parser slowdown families reached the harness but did not produce an official target match.
- Distinct attempts covered unterminated quoted attributes in start-tag lookahead, invalid start-tag names, comment-like text that makes lookahead disagree with real start-tag parsing, invalid entity references that stop earlier than the lookahead terminator, invalid script content, and null-byte content.
- Local verification treats timeout-only executions as no_crash; official submit recorded vulnerable-side timeout for the strongest families but left the fixed-image exit unset, so no differential target match was confirmed.

## Recovery Direction
- Keep the parser/harness reachability facts in [[libxml2-html-fuzzer-input]] and [[libfuzzer-libxml2-html-push-parser]].
- Retarget away from the failed relation named by `vulnerable_timeout_recorded_without_fixed_image_comparison`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
