---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Raw Disassembler Buffer Construct Disassembler Invalid Register Pair Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "raw-disassembler-buffer"
harness_convention: "libfuzzer"
vuln_class: "disassembler-invalid-register-pair"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "raw-disassembler-buffer", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "raw-disassembler-buffer", "libfuzzer", "disassembler-invalid-register-pair", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached No Target Crash Raw Disassembler Buffer Construct Disassembler Invalid Register Pair Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-disassembler-buffer]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The corrected BFD trailer selected the ARC architecture and multiple ARC machine variants, but the hand-built instruction words did not decode to the specific instruction form with an illegal even-odd double-register pair. The missing piece is an ARC opcode encoding that the disassembler recognizes as the affected double-register instruction while carrying a register-pair combination the assembler would normally reject.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `raw-disassembler-buffer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is not an object file. It is a raw instruction byte buffer followed by a fixed-size control trailer. The trailer selects disassembler flavour, machine, and architecture; the remaining leading bytes are read as instruction memory.

## Harness Contract
The libFuzzer target rejects very small inputs, extracts the architecture controls from the end of the buffer, looks up a BFD architecture/machine pair, then repeatedly invokes the selected disassembler over the leading byte buffer.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 5 attempts.
- Scope: generator repair and basin avoidance only.
