---
type: causal-policy
title: "No Crash Clean Exit No Sanitizer Signal Uri Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for persistent no_crash / clean_exit_no_sanitizer_signal basin."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_sanitizer_signal"
candidate_family: "construct"
input_format: "uri"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct", "uri", "heap-buffer-overflow-read", "negative-memory"]
match_keys: ["no-crash", "clean-exit-no-sanitizer-signal", "uri", "libfuzzer", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Clean Exit No Sanitizer Signal Uri Heap Buffer Overflow Read Negative Memory

## Policy
For `no_crash` with verifier signal `clean_exit_no_sanitizer_signal` on `uri` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- Malformed percent escapes in bracketed IPv6 scope ids, generic URI path/host/query/fragment escapes, encoded scope separators, missing closing brackets, and network-address-style scope examples all exited cleanly under the URI parser fuzzer.
- The likely missing condition is either a URI flag combination or a higher-level network-address resolver path that is not exercised by the selected harness.

## Recovery Direction
- Keep the parser/harness reachability facts in [[uri]] and [[libfuzzer]].
- Retarget away from the failed relation named by `clean_exit_no_sanitizer_signal`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
