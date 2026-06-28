---
type: causal-policy
title: "No Crash Wrapper Rejected File Path Blosc Compressed Buffer Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal wrapper_rejected_file_path."
failure_class: "no_crash"
verifier_signal: "wrapper_rejected_file_path"
candidate_family: "construct"
input_format: "blosc-compressed-buffer"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-rejected-file-path", "blosc-compressed-buffer", "negative-memory", "round-9"]
match_keys: ["no_crash", "wrapper_rejected_file_path", "blosc-compressed-buffer", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Wrapper Rejected File Path Blosc Compressed Buffer Negative Memory

- key: `no_crash x wrapper_rejected_file_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[blosc-compressed-buffer]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Header-shaped compressed-buffer candidates varied the advertised uncompressed size, compressed
  size, block size, and flags, but this image's wrapper rejected the mounted file path as a
  directory-style corpus path before the Blosc parser ran.

## Policy
Treat `no_crash x wrapper_rejected_file_path` on `blosc-compressed-buffer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The fuzzer expects a raw Blosc compressed buffer whose header reports nonzero uncompressed size, a
  compressed size equal to the total input length, and a buffer that passes blosc_cbuffer_validate
  before decompression into an output allocation sized from the compressed length.

## Harness Contract
- The entrypoint launches a libFuzzer target through a path that requires a corpus directory in this
  local/server setup, so a mounted raw file can be rejected before the decompression target consumes
  it.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_rejected_file_path`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
