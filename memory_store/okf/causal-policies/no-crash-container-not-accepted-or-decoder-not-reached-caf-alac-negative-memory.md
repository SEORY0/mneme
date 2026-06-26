---
type: causal-policy
title: "No Crash Container Not Accepted Or Decoder Not Reached Caf Alac Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal container_not_accepted_or_decoder_not_reached."
failure_class: "no_crash"
verifier_signal: "container_not_accepted_or_decoder_not_reached"
candidate_family: "construct"
input_format: "caf-alac"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "container-not-accepted-or-decoder-not-reached", "caf-alac", "negative-memory", "round-7"]
match_keys: ["no_crash", "container_not_accepted_or_decoder_not_reached", "caf-alac", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Container Not Accepted Or Decoder Not Reached Caf Alac Negative Memory

- key: `no_crash x container_not_accepted_or_decoder_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[caf-alac]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A hand-built CAF/ALAC envelope with description, cookie, and data chunks did not reach the
vulnerable ALAC decode path. The remaining missing gates are likely a valid packet table or a more
accurate ALAC frame bit layout that lets multiple channel elements decode successfully.

## Policy
Treat `no_crash x container_not_accepted_or_decoder_not_reached` on `caf-alac` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `container_not_accepted_or_decoder_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
CAF files use a file header followed by typed chunks. ALAC-in-CAF requires a stream description
declaring the ALAC format, a magic-cookie chunk containing the ALAC specific configuration including
channel count and frame parameters, and a data chunk containing compressed ALAC packets. The
described bug depends on the bitstream carrying more channel elements than the output channel count
can hold.

## Harness Contract
The harness opens the raw input via libsndfile virtual I/O, allocates a float buffer sized from the
parsed channel count, and repeatedly reads one frame at a time. The raw fuzzer bytes must therefore
be a recognizable sound-file container before ALAC decoding is reached.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
