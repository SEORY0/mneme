---
type: causal-policy
title: "No Crash Ghostscript Device Clean Exit Postscript PDF Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal ghostscript_device_clean_exit."
failure_class: "no_crash"
verifier_signal: "ghostscript_device_clean_exit"
candidate_family: "construct_then_seed_sweep"
input_format: "postscript/pdf"
harness_convention: "libfuzzer Ghostscript ps2write device fuzzer"
vuln_class: "pdfwrite-font-copy-cleanup-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-device-clean-exit", "postscript-pdf", "negative-memory", "round-16"]
match_keys: ["no_crash", "ghostscript_device_clean_exit", "postscript/pdf", "libfuzzer Ghostscript ps2write device fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Ghostscript Device Clean Exit Postscript PDF Negative Memory

## Policy
For `no_crash x ghostscript_device_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- A simple font-using PostScript input and shipped PDF/PS example seeds exercised the ps2write device cleanly. None introduced the partially copied font plus early-error state required for unsafe cleanup.
- When `no_crash x ghostscript_device_clean_exit` appears for `postscript/pdf`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The Ghostscript device harness accepts complete PostScript or PDF programs. Reaching this bug likely requires a document that makes pdfwrite or ps2write copy a font and then triggers an error before the copied font is fully associated with its owning device object.
- Harness: The selected wrapper runs the ps2write device fuzzer. It feeds the raw file through Ghostscript stdin using fixed device arguments, discards normal output, and performs cleanup through gsapi_exit and instance deletion.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
