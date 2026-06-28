---
type: causal-policy
title: "No Crash Parser Not Reached Raw Disassembler Buffer Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "raw-disassembler-buffer"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "raw-disassembler-buffer", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "raw-disassembler-buffer", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Raw Disassembler Buffer Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Trailer-selected KVX disassembler inputs with maximum continuation-bit bundles exercised the raw disassembler harness but did not produce an ASAN-visible fault. The likely issue is that the simple maximum-bundle probe reads into adjacent global state or exits through invalid-bundle handling without a sanitizer-detected access.
- When `no_crash x parser_not_reached` appears for `raw-disassembler-buffer`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The disassembler fuzzer treats most bytes as instruction data and reserves a small trailer for flavour, machine, and architecture selection. KVX bundles are made of fixed-width syllable words; a high continuation bit asks the decoder to keep collecting words up to the bundle maximum before reassembly.
- Harness: The active binary is the generic raw disassembler fuzzer, not the extended two-region disassembler harness. It uses little-endian display/endian settings, derives the architecture and machine from the trailing selector fields, then repeatedly calls the selected disassembler on the instruction buffer.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
