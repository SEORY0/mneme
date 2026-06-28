---
type: causal-policy
title: "Generic Crash Sink Mismatch Zlib Deflate Construct Use Of Uninitialized Value Negative Memory"
description: "Round 14 negative memory for generic_crash with verifier signal sink_mismatch."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "zlib-deflate"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "sink-mismatch", "zlib-deflate", "negative-memory", "round-14"]
match_keys: ["generic_crash", "sink_mismatch", "zlib-deflate", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# Generic Crash Sink Mismatch Zlib Deflate Construct Use Of Uninitialized Value Negative Memory

- key: `generic_crash x sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zlib-deflate]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Several zlib envelopes and deflate back-reference attempts either returned cleanly or crashed outside the target oracle; official submission rejected the crashing variants, indicating they did not reproduce the intended uninitialized-copy path.

## Policy
Treat `generic_crash x sink_mismatch` on `zlib-deflate` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
