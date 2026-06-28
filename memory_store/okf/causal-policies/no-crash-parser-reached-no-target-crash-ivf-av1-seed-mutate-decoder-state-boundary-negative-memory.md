---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Ivf Av1 Seed Mutate Decoder State Boundary Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "ivf-av1"
harness_convention: "libfuzzer"
vuln_class: "decoder-state-boundary"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "ivf-av1", "libfuzzer", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "ivf-av1", "libfuzzer", "decoder-state-boundary", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached No Target Crash Ivf Av1 Seed Mutate Decoder State Boundary Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ivf-av1]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The harness accepted IVF-shaped decoder inputs and replayed multiple bundled minimized AV1 seeds, but none reached the horizontal loop-filter invariant described by the task. The remaining gap is selecting or mutating a decoded frame configuration that enables the vulnerable loop-filter path rather than merely passing container and frame-size gates.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `ivf-av1` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

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
The target expects an IVF-style AV1 decode stream: a container header is read first, then frame records are iterated and each frame payload is passed to the AV1 decoder. Historical decoder seeds in the corpus are useful for reaching the parser, but they do not necessarily enable loop filtering or the target frame geometry.

## Harness Contract
The libFuzzer target wraps the raw input with an in-memory file, requires the container header read to succeed, initializes the AV1 decoder, then repeatedly reads IVF frames and drains decoded images. There is no FuzzedDataProvider carving or mode selector.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 9 attempts.
- Scope: generator repair and basin avoidance only.
