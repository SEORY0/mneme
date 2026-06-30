---
type: negative-memory
title: "No Crash Clean Exit After Cryptofuzz Bignumcalc Cryptofuzz Binary Operation Stream Construct Leading Zero Hex Conversion Size Mismatch Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal clean_exit_after_cryptofuzz_bignumcalc."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_cryptofuzz_bignumcalc"
candidate_family: "construct"
input_format: "cryptofuzz-binary-operation-stream"
harness_convention: "libfuzzer"
vuln_class: "leading-zero hex conversion size mismatch"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-after-cryptofuzz-bignumcalc", "cryptofuzz-binary-operation-stream", "libfuzzer", "construct", "negative-memory", "round-26"]
match_keys: ["no_crash", "clean_exit_after_cryptofuzz_bignumcalc", "cryptofuzz-binary-operation-stream", "libfuzzer", "leading-zero hex conversion size mismatch", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Clean Exit After Cryptofuzz Bignumcalc Cryptofuzz Binary Operation Stream Construct Leading Zero Hex Conversion Size Mismatch Negative Memory

- key: `no_crash x clean_exit_after_cryptofuzz_bignumcalc`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cryptofuzz-binary-operation-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed cryptofuzz BignumCalc envelopes reached the wolfCrypt operation path for positive arithmetic results, but the reachable SP-math result conversion used a large temporary hex buffer and exited cleanly. Attempts to create sign-sensitive results were rejected before producing a comparable component result, so the leading-zero conversion mismatch did not become a crashing condition in this harness.

## Policy
Treat `no_crash x clean_exit_after_cryptofuzz_bignumcalc` on `cryptofuzz-binary-operation-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_cryptofuzz_bignumcalc` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_cryptofuzz_bignumcalc`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Cryptofuzz inputs use a binary datasource rather than JSON. Each consumed scalar or blob is length-prefixed in stream order. The top-level stream selects an operation, then carries an operation payload, a modifier blob, a module selector, and a continuation flag. BignumCalc payloads contain a calc operation followed by four length-prefixed decimal digit buffers; non-digit bytes are normalized to digits before module execution.

## Harness Contract
The libFuzzer target reads the raw file bytes as one cryptofuzz datasource. The build is constrained to wolfCrypt and selected bignum/DH/ECC operations. For BignumCalc, the parent datasource supplies the modifier stream and module selector after the nested operation payload; modifier booleans are also length-prefixed datasource fields.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 33 attempts.
- Scope: generator repair and basin avoidance only.
