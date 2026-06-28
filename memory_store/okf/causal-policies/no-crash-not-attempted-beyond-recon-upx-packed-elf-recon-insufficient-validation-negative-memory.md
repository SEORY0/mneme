---
type: negative-memory
title: "No Crash Not Attempted Beyond Recon Upx Packed Elf Recon Insufficient Validation Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal not_attempted_beyond_recon."
failure_class: "no_crash"
verifier_signal: "not_attempted_beyond_recon"
candidate_family: "recon"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-file-command-wrapper"
vuln_class: "insufficient-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "not-attempted-beyond-recon", "upx-packed-elf", "libfuzzer-file-command-wrapper", "recon", "negative-memory", "round-25"]
match_keys: ["no_crash", "not_attempted_beyond_recon", "upx-packed-elf", "libfuzzer-file-command-wrapper", "insufficient-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Not Attempted Beyond Recon Upx Packed Elf Recon Insufficient Validation Negative Memory

- key: `no_crash x not_attempted_beyond_recon`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-elf]]
- related harness facts: [[libfuzzer-file-command-wrapper]]

## Failure Shape
No in-repo packed ELF seed was present, and memory warned that minimal ELF/UPX marker synthesis is a known rejected basin. I did not submit a low-quality marker-only candidate.

## Policy
Treat `no_crash x not_attempted_beyond_recon` on `upx-packed-elf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `not_attempted_beyond_recon` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `not_attempted_beyond_recon`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The target UPX path requires an ELF file that is accepted as a UPX-packed Linux ELF. The described invariant is in unpacking: the ELF program header count must be sufficient for code that assumes multiple program headers.

## Harness Contract
The UPX fuzzers write raw bytes to a temporary file and invoke UPX test/list/decompress command paths. Plain ELF-like carriers without a valid packed UPX structure are typically rejected before the unpacking code.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 0 attempts.
- Scope: generator repair and basin avoidance only.
