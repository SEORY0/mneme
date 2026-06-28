---
type: negative-memory
title: "No Crash Filesystem Probe Clean Exit Ntfs Filesystem Image Construct Heap Buffer Overflow Read Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal filesystem_probe_clean_exit."
failure_class: "no_crash"
verifier_signal: "filesystem_probe_clean_exit"
candidate_family: "construct"
input_format: "ntfs-filesystem-image"
harness_convention: "libfuzzer-memory-image"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "filesystem-probe-clean-exit", "ntfs-filesystem-image", "libfuzzer-memory-image", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "filesystem_probe_clean_exit", "ntfs-filesystem-image", "libfuzzer-memory-image", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Filesystem Probe Clean Exit Ntfs Filesystem Image Construct Heap Buffer Overflow Read Negative Memory

- key: `no_crash x filesystem_probe_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ntfs-filesystem-image]]
- related harness facts: [[libfuzzer-memory-image]]

## Failure Shape
A minimal NTFS boot-sector-style image was accepted by the wrapper without reaching a crashing attribute runlist parse. No in-repo NTFS disk image seed was present in the extracted source tree for seed mutation.

## Policy
Treat `no_crash x filesystem_probe_clean_exit` on `ntfs-filesystem-image` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `filesystem_probe_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `filesystem_probe_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The target format is an NTFS filesystem image. Reaching the data-run parser requires a coherent filesystem boot sector, MFT metadata, attributes, and a resident or non-resident runlist structure for file data.

## Harness Contract
The SleuthKit fuzzer opens raw bytes as an in-memory image, opens a filesystem of the configured type at image offset zero, recursively lists from the root inode if opening succeeds, then closes the filesystem and image.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 1 attempt.
- Scope: generator repair and basin avoidance only.
