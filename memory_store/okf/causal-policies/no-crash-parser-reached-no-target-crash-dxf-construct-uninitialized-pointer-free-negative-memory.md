---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Dxf Construct Uninitialized Pointer Free Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "dxf"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-pointer-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "dxf", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "dxf", "libfuzzer", "uninitialized-pointer-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached No Target Crash Dxf Construct Uninitialized Pointer Free Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
DXF candidates that allocated a summary custom-property tag without a matching value did not trigger the cleanup crash; malformed follow-on sections were either non-critical or cleaned without dereferencing the uninitialized property value.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `dxf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

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
DXF is parsed as group-code/value records. Header variables live in a HEADER section; summary metadata can include custom property tags and values, where a tag allocates a property slot and a later value initializes the paired value field.

## Harness Contract
The libredwg LLVM fuzzer autodetects raw bytes as DWG, JSON, or DXF. Non-DWG/non-JSON data is passed to the DXF reader, then the harness may encode/write/free the parsed Dwg_Data object.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 3 attempts.
- Scope: generator repair and basin avoidance only.
