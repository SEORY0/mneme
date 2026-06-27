---
type: causal-policy
title: "No Crash Decoder Executed No Target Crash Vc1 Elementary Stream Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal decoder_executed_no_target_crash."
failure_class: "no_crash"
verifier_signal: "decoder_executed_no_target_crash"
candidate_family: "seed_mutate"
input_format: "vc1-elementary-stream"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-executed-no-target-crash", "vc1-elementary-stream", "negative-memory", "round-15"]
match_keys: ["no_crash", "decoder_executed_no_target_crash", "vc1-elementary-stream", "libfuzzer", "uninitialized-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Decoder Executed No Target Crash Vc1 Elementary Stream Negative Memory

- key: `no_crash x decoder_executed_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[vc1-elementary-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Valid VC1 corpus inputs and distinct mutations of the decoder-fuzzer envelope did not trigger the
  missing-slice uninitialized-value condition. One variant separated decoder extradata from a frame
  payload and decoded a frame, confirming that the decoder path can be reached, but parser-enabled,
  split-packet, truncated-frame, corrupted-frame, RCV, and small-dimension variants all remained non-
  crashing.

## Policy
Treat `no_crash x decoder_executed_no_target_crash` on `vc1-elementary-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- VC1 elementary streams are start-code-prefixed units such as sequence, entrypoint, frame, field, or
  slice payloads. The FFmpeg target also accepts a fuzzer-specific trailing control block that can
  configure dimensions, parser use, error-recognition behavior, extradata length, keyframe flags,
  packet flushing, and related decoder context fields. Packet boundaries can be introduced with the
  target's fixed tag marker.

## Harness Contract
- The VC1 target_dec_fuzzer treats the raw prefix as one or more decoder packets split by a fixed tag
  marker. If the input is large enough, the final control block is consumed as little-endian fuzzer
  configuration; optional extradata is carved from the end of the remaining prefix before packet
  decoding. The video get_buffer hook allocates exact image planes without zero-initializing them,
  which is the relevant harness difference from production allocation.

## Negative Memory
- Do not resubmit variants that only reproduce `decoder_executed_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
