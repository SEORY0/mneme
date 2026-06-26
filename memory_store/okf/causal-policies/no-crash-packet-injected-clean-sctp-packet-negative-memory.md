---
type: causal-policy
title: "No Crash Packet Injected Clean Sctp Packet Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal packet_injected_clean."
failure_class: "no_crash"
verifier_signal: "packet_injected_clean"
candidate_family: "construct"
input_format: "sctp-packet"
harness_convention: "afl-file"
vuln_class: "length-validation-order"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packet-injected-clean", "sctp-packet", "negative-memory", "round-7"]
match_keys: ["no_crash", "packet_injected_clean", "sctp-packet", "afl-file", "length-validation-order", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Packet Injected Clean Sctp Packet Negative Memory

- key: `no_crash x packet_injected_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sctp-packet]]
- related harness facts: [[afl-file]]

## Failure Shape
A minimal SCTP common-header packet with an inconsistent chunk length was accepted or ignored
without reaching a crashing length-before-validation path. More stateful association setup or a
specific chunk type/parameter relation is likely required.

## Policy
Treat `no_crash x packet_injected_clean` on `sctp-packet` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `packet_injected_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The SCTP harness expects packets with a common header followed by SCTP chunks. Chunk headers carry a
type, flags, and length; many parser paths require a valid association verification tag and stage-
specific handshake state before later chunks are interpreted deeply.

## Harness Contract
The connect fuzzer uses the first input byte as a stage selector, synthesizes the SCTP common header
itself, injects built-in handshake packets according to the stage, then injects the remaining input
as chunk bytes. The listen fuzzer accepts a complete packet directly but still requires a plausible
SCTP envelope.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
