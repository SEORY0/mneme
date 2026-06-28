---
type: negative-memory
title: "No Crash Rar5 Parser Clean Exit Rar5 Archive Seed Mutate Excessive Memory Allocation Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal rar5_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "rar5_parser_clean_exit"
candidate_family: "seed_mutate"
input_format: "rar5-archive"
harness_convention: "libfuzzer-libarchive-reader"
vuln_class: "excessive-memory-allocation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "rar5-parser-clean-exit", "rar5-archive", "libfuzzer-libarchive-reader", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "rar5_parser_clean_exit", "rar5-archive", "libfuzzer-libarchive-reader", "excessive-memory-allocation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Rar5 Parser Clean Exit Rar5 Archive Seed Mutate Excessive Memory Allocation Negative Memory

- key: `no_crash x rar5_parser_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar5-archive]]
- related harness facts: [[libfuzzer-libarchive-reader]]

## Failure Shape
A real in-repo RAR5 seed was decoded and its file-name-size relation was mutated with recomputed header metadata. The parser still exited cleanly, indicating the mutation did not force the oversized-name allocation path in a sanitizer-visible way.

## Policy
Treat `no_crash x rar5_parser_clean_exit` on `rar5-archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `rar5_parser_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `rar5_parser_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
RAR5 archives start with a signature and then CRC-protected variable-length block headers. File blocks carry flags, optional extra/data size fields, host and compression metadata, and a variable-length filename field.

## Harness Contract
The libarchive fuzzer treats raw bytes as an archive stream, enables broad filter and format support, opens memory input, iterates archive headers, queries entry metadata, reads entry data, and then frees the archive reader.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.
