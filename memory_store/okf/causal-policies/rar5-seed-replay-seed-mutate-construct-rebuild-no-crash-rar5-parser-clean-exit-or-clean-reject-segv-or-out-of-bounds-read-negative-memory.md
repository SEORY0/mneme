---
type: negative-memory
title: "Rar5 Seed Replay Seed Mutate Construct Rebuild No Crash Rar5 Parser Clean Exit Or Clean Reject Segv Or Out Of Bounds Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal rar5_parser_clean_exit_or_clean_reject."
failure_class: "no_crash"
verifier_signal: "rar5_parser_clean_exit_or_clean_reject"
candidate_family: "seed_replay|seed_mutate|construct_rebuild"
input_format: "rar5"
harness_convention: "libfuzzer-libarchive"
vuln_class: "segv-or-out-of-bounds-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "rar5-parser-clean-exit-or-clean-reject", "rar5", "libfuzzer-libarchive", "seed-replay-seed-mutate-construct-rebuild", "segv-or-out-of-bounds-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "rar5_parser_clean_exit_or_clean_reject", "rar5", "libfuzzer-libarchive", "seed-replay-seed-mutate-construct-rebuild", "segv-or-out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Rar5 Seed Replay Seed Mutate Construct Rebuild No Crash Rar5 Parser Clean Exit Or Clean Reject Segv Or Out Of Bounds Read Negative Memory

- key: `no_crash x rar5_parser_clean_exit_or_clean_reject`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

## Failure Shape
The likely invariant is a state mismatch where a solid or split RAR5 path updates the declared window size after the decompression window and mask have already been initialized. Mutations tried preserving real RAR5 headers while changing dictionary selectors across solid members and multivolume continuations, including rebuilt CRC-valid headers and service-block warm-up to avoid content checksum gates. All variants exited cleanly or were rejected before a sanitizer-visible stale-mask access, so the remaining missing piece is a compressed-data sequence that both preserves decompressor progress and makes the next pushed output cross the stale mask boundary.

## Policy
Treat `no_crash x rar5_parser_clean_exit_or_clean_reject` on `rar5` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `rar5_parser_clean_exit_or_clean_reject`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `rar5_parser_clean_exit_or_clean_reject`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[rar5]]. RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base headers. Main headers carry archive flags such as volume and solid state. File and service headers can carry extra-data and data-size fields, file flags, unpacked size, attributes, optional content CRC, compression info, host OS, filename, and extra records before compressed data. Compression info encodes method/version, a solid bit, and a dictionary/window selector. Base-header CRC must be recomputed after metadata mutations. Service blocks are parsed through the file path and their data is skipped through the decompressor.

## Harness Contract
Use [[libfuzzer-libarchive]]. The libarchive libFuzzer harness provides the whole PoC as one in-memory archive stream, enables all filters and formats, calls archive_read_next_header repeatedly, and drains each normal entry with archive_read_data. There is no leading selector byte and no FuzzedDataProvider split. A candidate must be a complete archive stream; concatenated RAR5 volumes can be presented in one PoC buffer if their signatures and volume headers remain valid.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 12 attempts.
- Scope: generator repair and basin avoidance only.
