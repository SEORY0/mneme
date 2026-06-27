---
type: causal-policy
title: "No Crash Official Non Target Both Images Failed Ffmpeg Target Decoder Frame Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal official_non_target_both_images_failed."
failure_class: "no_crash"
verifier_signal: "official_non_target_both_images_failed"
candidate_family: "construct"
input_format: "ffmpeg-target-decoder-frame"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "official-non-target-both-images-failed", "ffmpeg-target-decoder-frame", "libfuzzer-ffmpeg-target-decoder", "negative-memory", "round-18"]
match_keys: ["no-crash", "official-non-target-both-images-failed", "ffmpeg-target-decoder-frame", "libfuzzer-ffmpeg-target-decoder", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Official Non Target Both Images Failed Ffmpeg Target Decoder Frame Negative Memory

- key: `no_crash x official_non_target_both_images_failed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-target-decoder-frame]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
- A minimal TGQ packet with dimensions and a DC-only macroblock mode reached decoder accounting locally but did not produce a target-matched crash.
- The official server reported nonzero exits for both vulnerable and fixed images, so the candidate was a non-target failure.

## Policy
Treat `no_crash x official_non_target_both_images_failed` on `ffmpeg-target-decoder-frame` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `official_non_target_both_images_failed`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ffmpeg-target-decoder-frame]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ffmpeg-target-decoder]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x official_non_target_both_images_failed`.
- Candidate family: `construct`.
- Basin summary: A minimal TGQ packet with dimensions and a DC-only macroblock mode reached decoder accounting locally but did not produce a target-matched crash.
