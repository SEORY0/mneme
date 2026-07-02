---
type: negative-memory
title: "Opensc Pkcs15 Reader Chunk Stream Seed Mutate And Construct No Crash Official No Crash After Tcos Emulator Reachability Heap Buffer Overflow Read Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal official_no_crash_after_tcos_emulator_reachability."
failure_class: "no_crash"
verifier_signal: "official_no_crash_after_tcos_emulator_reachability"
candidate_family: "seed_mutate_and_construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "honggfuzz"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "official-no-crash-after-tcos-emulator-reachability", "opensc-pkcs15-reader-chunk-stream", "honggfuzz", "seed-mutate-and-construct", "heap-buffer-overflow-read", "negative-memory", "round-36"]
match_keys: ["no_crash", "official_no_crash_after_tcos_emulator_reachability", "opensc-pkcs15-reader-chunk-stream", "honggfuzz", "heap-buffer-overflow-read", "no-crash", "official-no-crash-after-tcos-emulator-reachability", "negative_memory", "seed_mutate_and_construct", "seed-mutate-and-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Opensc Pkcs15 Reader Chunk Stream Seed Mutate And Construct No Crash Official No Crash After Tcos Emulator Reachability Heap Buffer Overflow Read Negative Memory

- key: `no_crash x official_no_crash_after_tcos_emulator_reachability`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[honggfuzz]]

## Failure Shape
Seed mutations that switched a PKCS#15 transcript to a TCOS ATR did select the TCOS driver locally, and patched early SELECT responses could move into the TCOS PKCS#15 emulator. Official submissions still exited cleanly. Additional constructed attempts targeted TCOS PIN/key record parsers with short successful records, but did not produce a vulnerable-only crash.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x official_no_crash_after_tcos_emulator_reachability` on `opensc-pkcs15-reader-chunk-stream` under `honggfuzz` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `official_no_crash_after_tcos_emulator_reachability` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `official_no_crash_after_tcos_emulator_reachability`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 10 attempts.
- Scope: generator repair and basin avoidance only.
