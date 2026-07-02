---
type: causal-policy
title: "Rar And Rar5 Archive Seed Mutate No Crash Clean Exit Without Target Crash Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for rar-and-rar5-archive candidates that ended in no_crash with verifier signal clean_exit_without_target_crash."
failure_class: "no_crash"
verifier_signal: "clean_exit_without_target_crash"
candidate_family: "seed_mutate"
input_format: "rar-and-rar5-archive"
harness_convention: "libfuzzer-libarchive-reader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-without-target-crash", "rar-and-rar5-archive", "libfuzzer-libarchive-reader", "seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit-without-target-crash", "rar-and-rar5-archive", "libfuzzer-libarchive-reader", "seed-mutate", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Rar And Rar5 Archive Seed Mutate No Crash Clean Exit Without Target Crash Heap Buffer Overflow Read Negative Memory

- key: `no_crash x clean_exit_without_target_crash`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[rar-and-rar5-archive]]
- related harness facts: [[libfuzzer-libarchive-reader]]

## Policy
Treat `no_crash x clean_exit_without_target_crash` for `[[rar-and-rar5-archive]]` under `[[libfuzzer-libarchive-reader]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Distinct seed mutations reached valid archive envelopes but did not produce the target directory-window crash. The strongest hypothesis used a solid multi-member RAR5 fixture so an earlier member initialized decompression state before a later member was marked as a directory; the archive still drained cleanly. Old RAR directory-dictionary mutations, larger LZSS seeds, zero-sized later-member variants, service-block routing, and RAR5 single-member directory mutations all stayed in the same clean-exit basin.
3. Rebuild around `[[rar-and-rar5-archive]]` and `[[libfuzzer-libarchive-reader]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- Old RAR archives use a signature, main header, CRC-checked file headers, dictionary-size bits in file flags, packed and unpacked sizes, method, name, attributes, and compressed data. RAR5 archives use a fixed signature followed by CRC-protected variable-length base blocks; MAIN blocks carry archive flags such as solid mode, and FILE blocks carry optional data size, file flags, unpacked size, attributes, optional content checksum, compression metadata, host, name, and packed data. RAR5 solid archives can reuse decompression state across members, while service blocks are parsed like file blocks but route through an internal skip path.

## Harness Contract
- The libarchive fuzz target consumes the raw input as a single archive byte stream from memory, enables all filters and formats, then repeatedly reads headers and drains entry data through archive_read_data. There is no leading selector byte, no pcap-style wrapper, and no FuzzedDataProvider front/back carving.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 11.
