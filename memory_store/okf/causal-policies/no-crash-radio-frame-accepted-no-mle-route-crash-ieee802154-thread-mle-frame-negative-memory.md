---
type: causal-policy
title: "No Crash Radio Frame Accepted No MLE Route Crash Ieee802154 Thread MLE Frame Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal radio_frame_accepted_no_mle_route_crash."
failure_class: "no_crash"
verifier_signal: "radio_frame_accepted_no_mle_route_crash"
candidate_family: "seed_mutate"
input_format: "ieee802154-thread-mle-frame"
harness_convention: "afl/libfuzzer-wrapper"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "radio-frame-accepted-no-mle-route-crash", "ieee802154-thread-mle-frame", "negative-memory", "round-9"]
match_keys: ["no_crash", "radio_frame_accepted_no_mle_route_crash", "ieee802154-thread-mle-frame", "afl/libfuzzer-wrapper", "buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Radio Frame Accepted No MLE Route Crash Ieee802154 Thread MLE Frame Negative Memory

- key: `no_crash x radio_frame_accepted_no_mle_route_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ieee802154-thread-mle-frame]]
- related harness facts: [[afl-libfuzzer-wrapper]]

## Failure Shape
- The real radio corpus frame and several Route-TLV-like length/data perturbations executed
  successfully without crashing.
- The likely blocker is maintaining a valid Thread/MLE secured message structure while delivering a
  Route TLV with more route data entries than the fixed-size route array expects.

## Policy
Treat `no_crash x radio_frame_accepted_no_mle_route_crash` on `ieee802154-thread-mle-frame` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The relevant payload is an IEEE 802.15.4 frame carrying Thread/MLE data.
- MLE TLVs have type and length fields; the Route TLV includes a router-id sequence, router-id mask,
  and per-router route data, and the vulnerable invariant concerns route data count exceeding the
  implementation buffer capacity.

## Harness Contract
- The AFL-style target treats the input as one raw radio PSDU, rejects frames above the radio
  maximum, initializes an OpenThread leader instance, then passes the frame to radio receive
  completion.
- There is no mode selector or back-consumed size field.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `radio_frame_accepted_no_mle_route_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
