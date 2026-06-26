---
type: causal-policy
title: "No Crash Parser Not Reached Mat Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate"
input_format: "mat"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "mat", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_not_reached", "mat", "libfuzzer", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Not Reached Mat Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mat]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Mutating real MATLAB image seeds by truncating payloads and varying declared object sizes did not
pass the MAT object consistency gates deeply enough to reach the scanline exception path.

## Policy
Treat `no_crash x parser_not_reached` on `mat` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
MAT level-5 files use a fixed descriptive header followed by typed array records. Each array record
has a typed tag, byte count, array flags, dimensions, name, and typed data payload; readers cross-
check declared object sizes against dimensions and element size before scanline import.

## Harness Contract
The GraphicsMagick MAT fuzzer feeds the raw file bytes to the MAT coder. There is no mode selector
or FuzzedDataProvider layout; the input must be a complete MAT-like byte stream.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
