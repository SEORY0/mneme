---
type: causal-policy
title: "No Crash File Format Not Recognized Before Vms Descriptor Printing Vms Alpha Object Or Library Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal file-format-not-recognized before VMS descriptor printing."
failure_class: "no_crash"
verifier_signal: "file-format-not-recognized before VMS descriptor printing"
candidate_family: "construct"
input_format: "vms-alpha-object-or-library"
harness_convention: "honggfuzz/libfuzzer binutils objdump wrapper"
vuln_class: "stack-buffer-overflow-in-vms-descriptor-printing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "file-format-not-recognized-before-vms-descriptor-printing", "vms-alpha-object-or-library", "honggfuzz-libfuzzer-binutils-objdump-wrapper", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "file-format-not-recognized-before-vms-descriptor-printing", "vms-alpha-object-or-library", "honggfuzz-libfuzzer-binutils-objdump-wrapper", "stack-buffer-overflow-in-vms-descriptor-printing"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash File Format Not Recognized Before Vms Descriptor Printing Vms Alpha Object Or Library Negative Memory

- key: `no_crash x file-format-not-recognized before VMS descriptor printing`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[vms-alpha-object-or-library]]
- harnesses: [[honggfuzz-libfuzzer-binutils-objdump-wrapper]]

## Dead-End Shape
Hand-built EVAX/VMS-looking records and repeated descriptor text did not pass BFD object recognition, so the vulnerable descriptor printers were not reached. The missing gate is a valid VMS object or library record envelope with correct record classes and lengths.

## Policy
For `no_crash x file-format-not-recognized before VMS descriptor printing` on `vms-alpha-object-or-library`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x file-format-not-recognized before VMS descriptor printing` appears for `vms-alpha-object-or-library`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
