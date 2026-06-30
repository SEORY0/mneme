---
type: causal-policy
title: "No Crash Decoder Accepted Seed Target SEI Path Not Violated H264 Annexb Mvc Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal decoder_accepted_seed_target_sei_path_not_violated."
failure_class: "no_crash"
verifier_signal: "decoder_accepted_seed_target_sei_path_not_violated"
candidate_family: "seed_mutate"
input_format: "h264-annexb-mvc"
harness_convention: "honggfuzz-libavc-mvc-decoder"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "decoder-accepted-seed-target-sei-path-not-violated", "h264-annexb-mvc", "honggfuzz-libavc-mvc-decoder", "negative-memory", "round-18"]
match_keys: ["no-crash", "decoder-accepted-seed-target-sei-path-not-violated", "h264-annexb-mvc", "honggfuzz-libavc-mvc-decoder", "heap-buffer-overflow-write", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Decoder Accepted Seed Target SEI Path Not Violated H264 Annexb Mvc Negative Memory

- key: `no_crash x decoder_accepted_seed_target_sei_path_not_violated`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annexb-mvc]]
- related harness facts: [[honggfuzz-libavc-mvc-decoder]]

## Failure Shape
- Three bundled H.264 corpus seeds plus single-SEI and double-large-SEI prefix mutations ran cleanly.
- The remaining gap is constructing an MVC elementary stream that preserves sequence/picture parameter gates and places multiple film-grain-characteristics SEI payloads inside one SEI NAL so the dynamic bitstream buffer is exceeded in the MVC decoder's SEI parsing path.

## Policy
Treat `no_crash x decoder_accepted_seed_target_sei_path_not_violated` on `h264-annexb-mvc` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_accepted_seed_target_sei_path_not_violated`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[h264-annexb-mvc]] for descriptive format gates and invariants.

## Harness Contract
Use [[honggfuzz-libavc-mvc-decoder]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x decoder_accepted_seed_target_sei_path_not_violated`.
- Candidate family: `seed_mutate`.
- Basin summary: Three bundled H.264 corpus seeds plus single-SEI and double-large-SEI prefix mutations ran cleanly.

## Round 27 Reinforcement
- key: `no_crash x decoder_accepted_seed_target_sei_path_not_violated`
- A real H.264 seed corpus reached the MVC decoder cleanly, but the target condition stayed untriggered.
- Distinct failed hypotheses included an unmodified accepted seed, a large skipped SEI payload followed by malformed Film Grain Characteristics syntax near the default bitstream-buffer boundary, repeated maximum-size Film Grain Characteristics payloads inside one SEI NAL, alternate placements before and after the seed's existing SEI/parameter-set sequence, and a larger carrier seed to cover access-unit-size interactions.
- The remaining missing gate is likely a stricter MVC-compatible state relation or a more exact FGC payload relation than plain AVC corpus seeds provide.
