---
type: causal-policy
title: "UPX Packed ELF Seed Mutate Sink Mismatch Heap Buffer Overflow Read In Overlay Scan Heap Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal sink_mismatch_heap_buffer_overflow_read_in_overlay_scan."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_heap_buffer_overflow_read_in_overlay_scan"
candidate_family: "seed_mutate"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-upx-test-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-heap-buffer-overflow-read-in-overlay-scan", "upx-packed-elf", "libfuzzer-upx-test-file", "seed-mutate", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "sink_mismatch_heap_buffer_overflow_read_in_overlay_scan", "upx-packed-elf", "libfuzzer-upx-test-file", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# UPX Packed ELF Seed Mutate Sink Mismatch Heap Buffer Overflow Read In Overlay Scan Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch_heap_buffer_overflow_read_in_overlay_scan`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[upx-packed-elf]]
- harnesses: [[libfuzzer-upx-test-file]]

## Failure Shape
Start from a genuine UPX-packed Linux ELF seed that the UPX test-mode harness accepts. Preserve the ELF envelope and the final valid UPX pack header, but shorten the file so only a partial overlay-offset word remains after that header, with the remaining trailing fragment nonzero so the suffix zero-trim scan still selects the header. The vulnerable overlay finder validates the header-relative length against the suffix buffer without accounting for the shifted scan base, then reads the overlay word past the available tail bytes; the fixed build rejects the incomplete overlay relation cleanly.

## Policy
For `wrong_sink x sink_mismatch_heap_buffer_overflow_read_in_overlay_scan` on `upx-packed-elf`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `upx-packed-elf` carrier and `libfuzzer-upx-test-file` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `upx-packed-elf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
UPX-packed Linux ELF inputs keep a normal ELF executable envelope plus UPX loader and overlay metadata. The tail contains a versioned UPX pack header followed by a little-endian overlay-offset word. Header fields include version, format, compression method, level, compressed and uncompressed sizes, original file size, filter metadata, and a header checksum; the checksum covers the pack header but not the following overlay-offset word.

## Harness Contract
The libFuzzer target writes the raw input bytes to a temporary file and invokes UPX test mode on that file through the normal command path. There is no fuzzer-side prefix, selector, length trailer, or FuzzedDataProvider layout; parser reachability requires a complete packed executable recognized by UPX.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 11 attempts.
- Scope: generator repair and retargeting only.
