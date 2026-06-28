---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Elf Crx Object Construct Global Buffer Overflow Read Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "elf-crx-object"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "elf-crx-object", "negative-memory", "round-14"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "elf-crx-object", "libfuzzer", "global-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Parser Reached No Target Crash Elf Crx Object Construct Global Buffer Overflow Read Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-crx-object]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal CRX ELF objects reached the disassembly harness, including instruction words intended to match CRX entries whose operand descriptor arrays are fully populated, but no sanitizer-visible read past the descriptor array occurred. The remaining gap is likely an exact instruction encoding or disassembler mode needed to force operand counting on the vulnerable table entry.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `elf-crx-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
