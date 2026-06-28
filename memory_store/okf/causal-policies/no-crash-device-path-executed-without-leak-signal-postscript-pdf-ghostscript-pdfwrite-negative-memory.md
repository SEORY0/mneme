---
type: causal-policy
title: "No Crash Device Path Executed Without Leak Signal Postscript PDF Ghostscript Pdfwrite Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal device_path_executed_without_leak_signal."
failure_class: "no_crash"
verifier_signal: "device_path_executed_without_leak_signal"
candidate_family: "construct"
input_format: "PostScript/PDF for Ghostscript pdfwrite"
harness_convention: "libfuzzer Ghostscript device wrapper"
vuln_class: "memory-leak-on-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "device-path-executed-without-leak-signal", "negative-memory", "round-10"]
match_keys: ["no_crash", "device_path_executed_without_leak_signal", "PostScript/PDF for Ghostscript pdfwrite", "libfuzzer Ghostscript device wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Device Path Executed Without Leak Signal Postscript PDF Ghostscript Pdfwrite Negative Memory

## Policy
For `no_crash x device_path_executed_without_leak_signal`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Basic PostScript rendering, invalid setpagedevice parameters, text clipping, pdfmark annotations, and malformed PDF input did not trigger the leak detector.
2. When `no_crash x device_path_executed_without_leak_signal` appears for `PostScript/PDF for Ghostscript pdfwrite`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The fuzzer input is interpreter content for Ghostscript. PostScript can set device parameters, draw pages, and use pdfmark/pdfwrite features; malformed PDF input may be accepted by the same wrapper but needs enough structure to reach pdfwrite device internals.
- Harness: The harness calls a Ghostscript device fuzzer with the pdfwrite device selected. Raw bytes become interpreter input; no front carving or FuzzedDataProvider layout is used.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
