---
type: causal-policy
title: "No Crash Upx Not Packed Or Too Small Upx Packed Elf Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal upx_not_packed_or_too_small."
failure_class: "no_crash"
verifier_signal: "upx_not_packed_or_too_small"
candidate_family: "construct"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-file-backed"
vuln_class: "packed-elf-b-info-recovery"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "upx-not-packed-or-too-small", "upx-packed-elf", "negative-memory", "round-7"]
match_keys: ["no_crash", "upx_not_packed_or_too_small", "upx-packed-elf", "libfuzzer-file-backed", "packed-elf-b-info-recovery", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Upx Not Packed Or Too Small Upx Packed Elf Negative Memory

- key: `no_crash x upx_not_packed_or_too_small`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-elf]]
- related harness facts: [[libfuzzer-file-backed]]

## Failure Shape
A minimal ELF-like carrier reached UPX list mode but was skipped as not a packed executable. The
target recovery path requires a genuine UPX-packed Linux ELF with loader metadata, l_info, p_info,
and b_info blocks arranged so sliding recovery searches nearby b_info.

## Policy
Treat `no_crash x upx_not_packed_or_too_small` on `upx-packed-elf` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `upx_not_packed_or_too_small`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
UPX-packed Linux ELF inputs keep a normal ELF envelope plus UPX loader/overlay metadata.
Unpacking/listing expects l_info, p_info, compressed block b_info records, and compressed payload
blocks; recovery code may scan around a slid b_info location when metadata is inconsistent.

## Harness Contract
The fuzzer writes raw bytes to a temporary file and invokes UPX list mode on that file, catching
exceptions. The input must be a complete packed file; raw ELF headers or stub fragments are not
enough to reach b_info recovery.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
