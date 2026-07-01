---
type: negative-memory
title: "Rar5 Seed Mutate No Crash Clean Exit Or Off Target Timeout Without Target Crash Logic Error Directory Entry Unpack Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal clean_exit_or_off_target_timeout_without_target_crash."
failure_class: "no_crash"
verifier_signal: "clean_exit_or_off_target_timeout_without_target_crash"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer-libarchive"
vuln_class: "logic-error-directory-entry-unpack"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "clean-exit-or-off-target-timeout-without-target-crash", "rar5", "libfuzzer-libarchive", "seed-mutate", "logic-error-directory-entry-unpack", "negative-memory", "round-33"]
match_keys: ["no_crash", "clean_exit_or_off_target_timeout_without_target_crash", "rar5", "libfuzzer-libarchive", "seed-mutate", "logic-error-directory-entry-unpack", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Rar5 Seed Mutate No Crash Clean Exit Or Off Target Timeout Without Target Crash Logic Error Directory Entry Unpack Negative Memory

- key: `no_crash x clean_exit_or_off_target_timeout_without_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

## Failure Shape
Real RAR5 seeds were mutated while preserving the archive marker, base-header framing, and recomputed header CRC gates. Directory-marked compressed members either stayed in a long/off-target unpack path or exited cleanly; stored-data, host-mode, ARM-filter, and solid-stream variants did not produce the target sanitizer fault. The likely missing relation is a narrower coherent file/service or skip-mode state that routes a directory-marked entry into the vulnerable unpack path without degenerating into timeout or normal EOF.

## Policy
Treat `no_crash x clean_exit_or_off_target_timeout_without_target_crash` on `rar5` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `clean_exit_or_off_target_timeout_without_target_crash`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_or_off_target_timeout_without_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[rar5]]. RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base blocks. Main blocks carry archive flags such as solid mode. File blocks can carry extra-data and packed-data sizes, then file flags such as directory and content checksum, unpacked size, attributes, compression information, host OS, filename, optional extras, and member data. Header metadata mutations must preserve varint widths or rebuild the block header CRC. Directory flags can force a zero decompression window, while host metadata controls how the archive entry mode is exposed.

## Harness Contract
Use [[libfuzzer-libarchive]]. The libarchive fuzz harness consumes the raw PoC bytes as one in-memory archive stream, enables all filters and formats, repeatedly reads archive headers, and drains entry data with archive_read_data. There is no leading selector byte, filename contract, stdin wrapper, checksum wrapper beyond the archive format itself, or FuzzedDataProvider front/back split.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 6 attempts.
- Scope: generator repair and basin avoidance only.
