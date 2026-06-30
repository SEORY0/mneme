---
type: causal-policy
title: "Libredwg JSON Construct Parser Reached Dynapi Tfv Copy Fix Clean Official Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_dynapi_tfv_copy_fix_clean_official_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_dynapi_tfv_copy_fix_clean_official_match"
candidate_family: "construct"
input_format: "libredwg-json"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-dynapi-tfv-copy-fix-clean-official-match", "libredwg-json", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_dynapi_tfv_copy_fix_clean_official_match", "libredwg-json", "libfuzzer", "heap-buffer-overflow-write", "wrong-sink", "parser-reached-dynapi-tfv-copy-fix-clean-official-match", "libredwg-json", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Libredwg JSON Construct Parser Reached Dynapi Tfv Copy Fix Clean Official Match Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_dynapi_tfv_copy_fix_clean_official_match`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[libredwg-json]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_dynapi_tfv_copy_fix_clean_official_match` on `libredwg-json`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Select the JSON parser and set the file metadata to a pre-R13 DWG version so header strings are treated as fixed TFv fields. Use a recognized header variable from the fixed block-name family and make its string just exceed the fixed allocation. This reaches the dynapi header setter, remaps the metadata to fixed TFv, and the vulnerable helper copies the string without a bound; the fixed build protects that family and exits cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[libredwg-json]]: libredwg's JSON input is a top-level object with section objects. FILEHEADER metadata controls the DWG version used by later sections, and HEADER keys are looked up through dynapi metadata. For pre-R13 versions, selected header string variables are handled as fixed TFv strings even though the JSON token is ordinary text.
- Harness [[libfuzzer]]: The libFuzzer harness feeds the raw file bytes. It chooses DWG when the input begins with the DWG signature, JSON when the first byte is an opening JSON object, and DXF otherwise. The JSON path copies and null-terminates the input before calling the libredwg JSON reader, then may serialize the parsed drawing to an output format after import.

## Negative Memory
- Do not corrupt the outer `libredwg-json` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[libredwg-json]] and [[libfuzzer]].
