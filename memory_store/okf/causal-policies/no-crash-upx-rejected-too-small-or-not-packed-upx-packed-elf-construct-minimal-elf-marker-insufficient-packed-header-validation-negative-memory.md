---
type: causal-policy
title: "No Crash Upx Rejected Too Small Or Not Packed Upx Packed Elf Construct Minimal Elf Marker Insufficient Packed Header Validation Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal upx_rejected_too_small_or_not_packed."
failure_class: "no_crash"
verifier_signal: "upx_rejected_too_small_or_not_packed"
candidate_family: "construct_minimal_elf_marker"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-file-command-wrapper"
vuln_class: "insufficient-packed-header-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "upx-rejected-too-small-or-not-packed", "upx-packed-elf", "negative-memory", "round-14"]
match_keys: ["no_crash", "upx_rejected_too_small_or_not_packed", "upx-packed-elf", "libfuzzer-file-command-wrapper", "insufficient-packed-header-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Upx Rejected Too Small Or Not Packed Upx Packed Elf Construct Minimal Elf Marker Insufficient Packed Header Validation Negative Memory

- key: `no_crash x upx_rejected_too_small_or_not_packed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-elf]]
- related harness facts: [[libfuzzer-file-command-wrapper]]

## Failure Shape
No in-repo packed corpus files were present in the extracted tree. A minimal ELF-like carrier with UPX markers was rejected as too small/not packed, so it never reached PackUnix p_info unpacking.

## Policy
Treat `no_crash x upx_rejected_too_small_or_not_packed` on `upx-packed-elf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
