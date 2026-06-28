---
type: causal-policy
title: "No Crash Encoder Not Reaching Sbr Tonal Zero Path Libxaac Encoder Fuzzed Provider Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal encoder_not_reaching_sbr_tonal_zero_path."
failure_class: "no_crash"
verifier_signal: "encoder_not_reaching_sbr_tonal_zero_path"
candidate_family: "construct"
input_format: "libxaac-encoder-fuzzed-provider"
harness_convention: "libfuzzer-fuzzed-data-provider"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "encoder-not-reaching-sbr-tonal-zero-path", "libxaac-encoder-fuzzed-provider", "libfuzzer-fuzzed-data-provider", "negative-memory", "round-17"]
match_keys: ["no-crash", "encoder-not-reaching-sbr-tonal-zero-path", "libxaac-encoder-fuzzed-provider", "libfuzzer-fuzzed-data-provider", "global-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Encoder Not Reaching Sbr Tonal Zero Path Libxaac Encoder Fuzzed Provider Negative Memory

- key: `no_crash x encoder_not_reaching_sbr_tonal_zero_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxaac-encoder-fuzzed-provider]]
- related harness facts: [[libfuzzer-fuzzed-data-provider]]

## Failure Shape
- SBR/USAC-oriented encoder configuration tails plus silence, constant, alternating, and sine-like PCM bodies did not reach the target quantization path.
- Some candidates fell into harness invocation handling, and the clean candidates did not expose the tonal-difference-zero condition.

## Policy
Treat `no_crash x encoder_not_reaching_sbr_tonal_zero_path` on `libxaac-encoder-fuzzed-provider` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `encoder_not_reaching_sbr_tonal_zero_path`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[libxaac-encoder-fuzzed-provider]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-fuzzed-data-provider]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
