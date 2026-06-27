---
type: causal-policy
title: "No Crash TIFF Header Accepted Target Not Reached Samsung SRW TIFF Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal tiff_header_accepted_target_not_reached."
failure_class: "no_crash"
verifier_signal: "tiff_header_accepted_target_not_reached"
candidate_family: "construct"
input_format: "samsung-srw-tiff"
harness_convention: "afl-rawspeed-tiff-decoder"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "tiff-header-accepted-target-not-reached", "samsung-srw-tiff", "afl-rawspeed-tiff-decoder", "negative-memory", "round-18"]
match_keys: ["no-crash", "tiff-header-accepted-target-not-reached", "samsung-srw-tiff", "afl-rawspeed-tiff-decoder", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash TIFF Header Accepted Target Not Reached Samsung SRW TIFF Negative Memory

- key: `no_crash x tiff_header_accepted_target_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[samsung-srw-tiff]]
- related harness facts: [[afl-rawspeed-tiff-decoder]]

## Failure Shape
- Minimal little-endian and big-endian TIFF envelopes, SRW-like geometry/compression tags, an alternate raw header, and Samsung model tags reached only generic parser or decoder rejection paths.
- No SRW sample corpus was present in the extracted source, and the missing piece is a Samsung SRW-like TIFF with raw image geometry and compression tags that select the SamsungV2 decompressor and enter the last-pixels complex prediction case.

## Policy
Treat `no_crash x tiff_header_accepted_target_not_reached` on `samsung-srw-tiff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `tiff_header_accepted_target_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[samsung-srw-tiff]] for descriptive format gates and invariants.

## Harness Contract
Use [[afl-rawspeed-tiff-decoder]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x tiff_header_accepted_target_not_reached`.
- Candidate family: `construct`.
- Basin summary: Minimal little-endian and big-endian TIFF envelopes, SRW-like geometry/compression tags, an alternate raw header, and Samsung model tags reached only generic parser or decoder rejection paths.
