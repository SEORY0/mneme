---
type: causal-policy
title: "No Crash Parser Reached No Crash Iamf Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_no_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_crash"
candidate_family: "seed_mutate"
input_format: "iamf"
harness_convention: "file-parser"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-crash", "iamf", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_no_crash", "iamf", "file-parser", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached No Crash Iamf Negative Memory

- key: `no_crash x parser_reached_no_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[iamf]]
- related harness facts: [[file-parser]]

## Failure Shape
IAMF seed mutations involving appended padding, truncation, alternate seed files, synthetic leading OBU-like bytes, and interior zero padding did not trigger the uninitialized padding use. The likely missing gate is a precise OBU whose declared size and bit-level padding leave parser-owned padding uncleared while still passing IAMF descriptor validation.

## Policy
Treat `no_crash x parser_reached_no_crash` on `iamf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
IAMF streams are composed of OBU-style records with header fields, size coding, descriptor OBUs, audio element metadata, mix presentation metadata, and padding or reserved bit regions. Parser reachability depends on coherent descriptor order and declared sizes.

## Harness Contract
The FFmpeg harness writes or feeds the raw input as an IAMF demuxer sample through the local run_poc wrapper. There is no model-side generation or fuzzer prefix; demuxer probing and IAMF OBU parsing decide whether the parser reaches descriptor handling.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
