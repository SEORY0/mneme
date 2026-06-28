---
type: causal-policy
title: "No Crash Disassembler Selected But No Formatter Overrun Machine Code Plus Disassembler Options Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal disassembler_selected_but_no_formatter_overrun."
failure_class: "no_crash"
verifier_signal: "disassembler_selected_but_no_formatter_overrun"
candidate_family: "construct"
input_format: "machine-code-plus-disassembler-options"
harness_convention: "afl/libfuzzer-compatible raw stdin"
vuln_class: "fixed-buffer-format-output-overrun"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "disassembler-selected-but-no-formatter-overrun", "machine-code-plus-disassembler-options", "afl-libfuzzer-compatible-raw-stdin", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "disassembler-selected-but-no-formatter-overrun", "machine-code-plus-disassembler-options", "afl-libfuzzer-compatible-raw-stdin", "fixed-buffer-format-output-overrun"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Disassembler Selected But No Formatter Overrun Machine Code Plus Disassembler Options Negative Memory

- key: `no_crash x disassembler_selected_but_no_formatter_overrun`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[machine-code-plus-disassembler-options]]
- harnesses: [[afl-libfuzzer-compatible-raw-stdin]]

## Dead-End Shape
The actual generated harness was the disassembler formatter wrapper rather than the demangler described in the card. Constructed inputs selected valid architectures and machine modes, including verbose x86-style byte patterns, but did not make one formatted fragment exceed the fixed buffer and then continue formatting.

## Policy
For `no_crash x disassembler_selected_but_no_formatter_overrun` on `machine-code-plus-disassembler-options`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x disassembler_selected_but_no_formatter_overrun` appears for `machine-code-plus-disassembler-options`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
