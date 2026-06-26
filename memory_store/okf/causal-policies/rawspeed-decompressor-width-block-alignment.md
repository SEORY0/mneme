---
type: causal-policy
title: RawSpeed Decompressor Width Block Alignment Recovery
description: Verified recovery for generic_crash with signal_crash on rawspeed-decompressor-envelope inputs.
failure_class: generic_crash
verifier_signal: signal_crash
candidate_family: construct
input_format: rawspeed-decompressor-envelope
harness_convention: libfuzzer
vuln_class: out-of-bounds-access
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, signal-crash, construct, rawspeed-decompressor-envelope, out-of-bounds-access, verified-recovery]
match_keys: [generic-crash, signal-crash, rawspeed-decompressor-envelope, out-of-bounds-access]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# RawSpeed Decompressor Width Block Alignment Recovery

- key: `generic_crash x signal_crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[rawspeed-decompressor-envelope]]

## Failure Shape
Build the RawSpeed direct decompressor envelope with valid scalar image metadata and a
single component, but choose an image width that violates the decoder block-alignment
assumption while still providing enough payload to enter decompression.

## Policy
For `generic_crash x signal_crash` on `rawspeed-decompressor-envelope`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Build the direct decompressor envelope with valid scalar image metadata and a single
component.
2. Choose a width or stride relation that violates the decoder's block-alignment assumption.
3. Provide enough payload for decompression to begin; bad-format truncation is not the target.
4. For generic signal crashes, preserve the envelope and vary only alignment-related
dimensions.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not mutate component count and dimensions together once decompression is reached.
- Do not treat a decoder setup failure as success; the target crash occurs after decompression
starts.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
