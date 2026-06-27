---
type: causal-policy
title: "No Crash Samsung Srw Tiff Parser Rejected Or Clean Without Samsung V0 Target Negative Memory"
description: "Negative memory for no_crash with parser_rejected_or_clean_without_samsung_v0_target on samsung-srw-tiff inputs."
failure_class: no_crash
verifier_signal: parser_rejected_or_clean_without_samsung_v0_target
candidate_family: construct
input_format: samsung-srw-tiff
harness_convention: rawspeed-parser-decode-wrapper
vuln_class: out-of-bounds-read-or-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-rejected-or-clean-without-samsung-v0-target, samsung-srw-tiff, out-of-bounds-read-or-write, negative_memory]
match_keys: [no-crash, parser-rejected-or-clean-without-samsung-v0-target, samsung-srw-tiff, out-of-bounds-read-or-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Samsung Srw Tiff Parser Rejected Or Clean Without Samsung V0 Target Negative Memory

- key: `no_crash x parser_rejected_or_clean_without_samsung_v0_target`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[samsung-srw-tiff]]

## Dead End
The empty input produced an off-target wrapper crash and was discarded. Minimal TIFF, Samsung/SRW-like TIFF, line-offset-style TIFF, and raw TIFF-prefix candidates executed cleanly without reaching the Samsung V0 upward-prediction sanitizer condition. The missing gate is a more faithful SRW/TIFF file that selects SamsungV0Decompressor and provides valid compressed row stripes with upward-prediction flags on the first rows.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
