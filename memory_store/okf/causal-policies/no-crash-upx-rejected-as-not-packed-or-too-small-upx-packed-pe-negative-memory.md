---
type: causal-policy
title: "No Crash UPX Rejected As Not Packed Or Too Small UPX Packed Pe Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal upx_rejected_as_not_packed_or_too_small."
failure_class: "no_crash"
verifier_signal: "upx_rejected_as_not_packed_or_too_small"
candidate_family: "construct"
input_format: "upx-packed-pe"
harness_convention: "afl/libfuzzer-wrapper"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "upx-rejected-as-not-packed-or-too-small", "upx-packed-pe", "negative-memory", "round-9"]
match_keys: ["no_crash", "upx_rejected_as_not_packed_or_too_small", "upx-packed-pe", "afl/libfuzzer-wrapper", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash UPX Rejected As Not Packed Or Too Small UPX Packed Pe Negative Memory

- key: `no_crash x upx_rejected_as_not_packed_or_too_small`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-pe]]
- related harness facts: [[afl-libfuzzer-wrapper]]

## Failure Shape
- Minimal PE-like files and a real executable stub were rejected as too small or not packed by UPX,
  so rebuildImports was not reached.
- A successful candidate likely needs a valid UPX-packed PE whose import metadata is near a logical
  block boundary and lacks an early terminator for a DLL or import name.

## Policy
Treat `no_crash x upx_rejected_as_not_packed_or_too_small` on `upx-packed-pe` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The target path is for UPX-packed PE files.
- The outer file must be recognized by UPX as packed, then decompression/rebuild metadata must
  describe PE imports including DLL names and imported symbol names.
- Ordinary PE stubs are insufficient because they do not reach UPX unpack/rebuild logic.

## Harness Contract
- The selected wrapper wrote raw bytes to a temporary file and invoked UPX test mode on it.
- There was no input carving.
- The output indicated the test_packed_file_fuzzer path, which reports NotPackedException or file-
  size rejection for invalid envelopes.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `upx_rejected_as_not_packed_or_too_small`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
