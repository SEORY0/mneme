---
type: negative-memory
title: "No Crash Wrapper Expected Directory Opentype Font Corpus Seed Mutate Buffer Overflow Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal wrapper_expected_directory."
failure_class: "no_crash"
verifier_signal: "wrapper_expected_directory"
candidate_family: "seed_mutate"
input_format: "opentype-font-corpus"
harness_convention: "libfuzzer-corpus-wrapper"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-expected-directory", "opentype-font-corpus", "libfuzzer-corpus-wrapper", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "wrapper_expected_directory", "opentype-font-corpus", "libfuzzer-corpus-wrapper", "buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Wrapper Expected Directory Opentype Font Corpus Seed Mutate Buffer Overflow Negative Memory

- key: `no_crash x wrapper_expected_directory`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font-corpus]]
- related harness facts: [[libfuzzer-corpus-wrapper]]

## Failure Shape
Valid in-repo HarfBuzz fuzzing fonts and an archive-style corpus wrapper were rejected before the font parser because the runner invoked the target with a file path where this wrapper expects a corpus directory.

## Policy
Treat `no_crash x wrapper_expected_directory` on `opentype-font-corpus` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `wrapper_expected_directory` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_expected_directory`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The useful seeds are OpenType/TrueType font files from HarfBuzz fuzzing and subset corpora. The vulnerable area is subset serialization, so a successful candidate must keep a valid font table directory and mutate only the table relation consumed by the serializer.

## Harness Contract
The observed wrapper did not feed raw file bytes to LLVMFuzzerTestOneInput. It treated the submitted path as a corpus directory; raw fonts and a zipped corpus were rejected before parser entry.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 4 attempts.
- Scope: generator repair and basin avoidance only.
