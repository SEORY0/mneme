---
type: causal-policy
title: "No Crash Dng Tiff Rawspeed Camera File Rawspeed Parser Clean Or Exception Negative Memory"
description: "Negative memory for no_crash with rawspeed_parser_clean_or_exception on dng-tiff-rawspeed-camera-file inputs."
failure_class: no_crash
verifier_signal: rawspeed_parser_clean_or_exception
candidate_family: construct
input_format: dng-tiff-rawspeed-camera-file
harness_convention: afl-libfuzzer
vuln_class: improper-sanitization
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, rawspeed-parser-clean-or-exception, dng-tiff-rawspeed-camera-file, improper-sanitization, negative_memory]
match_keys: [no-crash, rawspeed-parser-clean-or-exception, dng-tiff-rawspeed-camera-file, improper-sanitization]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Dng Tiff Rawspeed Camera File Rawspeed Parser Clean Or Exception Negative Memory

- key: `no_crash x rawspeed_parser_clean_or_exception`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[dng-tiff-rawspeed-camera-file]]

## Dead End
Minimal TIFF/DNG envelopes with baseline image tags and DNG-like opcode tag hypotheses were accepted cleanly or rejected without reaching the PixelOpcode application path. No in-repo DNG/RAW seed was present, so the remaining gap is a complete RawSpeed-recognized DNG carrier with opcode-list metadata and decoded image state.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
