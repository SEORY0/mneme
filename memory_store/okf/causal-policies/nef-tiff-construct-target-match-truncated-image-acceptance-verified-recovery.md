---
type: causal-policy
title: "Nef Tiff Construct Target Match Truncated Image Acceptance Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal target_match."
failure_class: "generic_crash"
verifier_signal: "target_match"
candidate_family: "construct"
input_format: "nef-tiff"
harness_convention: "libfuzzer"
vuln_class: "truncated-image-acceptance"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match", "nef-tiff", "libfuzzer", "construct", "truncated-image-acceptance", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "target_match", "nef-tiff", "libfuzzer", "truncated-image-acceptance", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Nef Tiff Construct Target Match Truncated Image Acceptance Verified Recovery

## Policy
For `generic_crash x target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a structurally valid little-endian TIFF/NEF skeleton with Nikon identity metadata, sNEF-compatible image metadata, strip offset and strip byte-count fields that advertise a full RGB payload, and white-balance rational data.
2. Keep the TIFF/IFD structure parseable, but provide strip data that is truncated just past the decoder's minimum-line gate.
3. The vulnerable decoder accepts the truncated image path and reaches the target failure; the fixed build rejects or contains the truncation.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- RawSpeed reaches the NEF decoder through standard TIFF header and IFD parsing.
- The sNEF path depends on make/model identity, image dimensions, bit depth, compression, CFA-pattern presence, strip offset/count metadata, and white-balance rationals.
- The strip byte count is used to classify the expected image payload independently of the actual remaining bytes in the file.
- Harness [[libfuzzer]]:
  - The libFuzzer target passes the entire input as a raw camera-file byte stream to RawSpeed.
  - There is no front selector, chunk framing, checksum wrapper, or FuzzedDataProvider layout.
  - Parser exceptions are caught, so the input must remain a coherent TIFF/IFD container before the decoder-specific truncation invariant is exercised.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[nef-tiff]] and [[libfuzzer]].
