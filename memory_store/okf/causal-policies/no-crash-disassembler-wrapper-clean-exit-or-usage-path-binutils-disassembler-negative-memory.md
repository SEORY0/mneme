---
type: causal-policy
title: "No Crash Disassembler Wrapper Clean Exit Or Usage Path Binutils Disassembler Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal disassembler_wrapper_clean_exit_or_usage_path."
failure_class: "no_crash"
verifier_signal: "disassembler_wrapper_clean_exit_or_usage_path"
candidate_family: "construct"
input_format: "binutils-disassembler-fuzzer-input"
harness_convention: "libfuzzer-compatible"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "disassembler-wrapper-clean-exit-or-usage-path", "negative-memory", "round-10"]
match_keys: ["no_crash", "disassembler_wrapper_clean_exit_or_usage_path", "binutils-disassembler-fuzzer-input", "libfuzzer-compatible", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Disassembler Wrapper Clean Exit Or Usage Path Binutils Disassembler Negative Memory

## Policy
For `no_crash x disassembler_wrapper_clean_exit_or_usage_path`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Multiple architecture and machine selector hypotheses did not reach an instruction family whose mask width overflows the small stack buffer in the CGEN disassembler hash helper.
2. When `no_crash x disassembler_wrapper_clean_exit_or_usage_path` appears for `binutils-disassembler-fuzzer-input`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The disassembler fuzzer input is a byte stream plus a fixed-size metadata trailer. The trailer selects disassembler flavour, architecture, and machine; the preceding bytes are the instruction stream that will be decoded under that architecture.
- Harness: The harness rejects very small or oversized inputs, reads architecture metadata from the end of the raw file, then repeatedly calls the selected binutils disassembler over the body bytes. Fuzzing the body without a matching CGEN architecture/machine selector stays off the target path.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
