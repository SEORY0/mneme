---
type: causal-policy
title: "No Crash Postscript Pdf Font Parser Reached No Target Crash Negative Memory"
description: "Negative memory for no_crash with parser_reached_no_target_crash on postscript-pdf-font inputs."
failure_class: no_crash
verifier_signal: parser_reached_no_target_crash
candidate_family: construct
input_format: postscript-pdf-font
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-target-crash, postscript-pdf-font, heap-buffer-overflow-read, negative_memory]
match_keys: [no-crash, parser-reached-no-target-crash, postscript-pdf-font, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Postscript Pdf Font Parser Reached No Target Crash Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[postscript-pdf-font]]

## Dead End
Minimal PostScript, Type 3 font, malformed Type 42 font, simple PDF font, and malformed TrueType-stream hypotheses did not trigger the FreeType fallback path. The missing condition is likely a valid enough TrueType glyph program that enters the extremis fallback while leaving a partial glyph bitmap state.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
