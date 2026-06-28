---
type: causal-policy
title: "No Crash Interpreter Error Or No Target Crash Postscript With Cff Data Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal interpreter_error_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "interpreter_error_or_no_target_crash"
candidate_family: "construct"
input_format: "postscript with cff data"
harness_convention: "libfuzzer"
vuln_class: "cff-parser-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "interpreter-error-or-no-target-crash", "postscript-with-cff-data", "negative-memory", "round-12"]
match_keys: ["no_crash", "interpreter_error_or_no_target_crash", "postscript-with-cff-data", "libfuzzer", "cff-parser-bounds", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Interpreter Error Or No Target Crash Postscript With Cff Data Negative Memory

- key: `no_crash x interpreter_error_or_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-with-cff-data]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The PostScript fuzzer accepted both normal PostScript and direct calls into the CFF parser operator. Minimal CFF and CID-keyed CFF structures with FDArray, FDSelect, sane and malformed FD private dictionaries all stayed in ordinary interpreter error handling and did not reach a sanitizer-detected target crash.

## Policy
Treat `no_crash x interpreter_error_or_no_target_crash` on `postscript-with-cff-data` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
CFF data starts with a header, then Name, Top DICT, String, and Global Subr indexes. CID-keyed CFF uses ROS fields in the top dictionary plus CharStrings, FDArray, and FDSelect offsets. FDArray entries are font dictionaries and may point to private dictionaries and local subroutine indexes.

## Harness Contract
The actual target is the Ghostscript ps2write device fuzzer. It runs raw input as PostScript. The internal .parsecff operator is callable from PostScript with a boolean and a string or block array, so CFF bytes can be supplied as a hex string without a full font wrapper.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `interpreter_error_or_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
