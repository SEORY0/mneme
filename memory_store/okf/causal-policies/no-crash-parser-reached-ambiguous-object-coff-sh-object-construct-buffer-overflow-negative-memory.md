---
type: negative-memory
title: "No Crash Parser Reached Ambiguous Object Coff Sh Object Construct Buffer Overflow Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_ambiguous_object."
failure_class: "no_crash"
verifier_signal: "parser_reached_ambiguous_object"
candidate_family: "construct"
input_format: "coff-sh-object"
harness_convention: "libfuzzer-file-command-wrapper"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-ambiguous-object", "coff-sh-object", "libfuzzer-file-command-wrapper", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_ambiguous_object", "coff-sh-object", "libfuzzer-file-command-wrapper", "buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached Ambiguous Object Coff Sh Object Construct Buffer Overflow Negative Memory

- key: `no_crash x parser_reached_ambiguous_object`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[coff-sh-object]]
- related harness facts: [[libfuzzer-file-command-wrapper]]

## Failure Shape
A minimal SH COFF object with one text section, one symbol, and a boundary relocation was recognized only as an ambiguous SH/PE-SH object and did not reach relocation application.

## Policy
Treat `no_crash x parser_reached_ambiguous_object` on `coff-sh-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_ambiguous_object` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_ambiguous_object`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
SH COFF objects contain a file header, section header table, raw section data, relocation records, and symbol table. SH relocation records include an address, symbol index, addend-like offset field, relocation type, and trailer bytes.

## Harness Contract
The binutils objdump-style wrapper writes raw input to a temporary file and lets BFD identify the object format. Ambiguous SH COFF recognition can stop before the target relocation handler is applied.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 1 attempt.
- Scope: generator repair and basin avoidance only.
