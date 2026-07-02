---
type: negative-memory
title: "Rar Seed Mutate No Crash Archive Reader Clean Exit Heap Use After Free Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal archive_reader_clean_exit."
failure_class: "no_crash"
verifier_signal: "archive_reader_clean_exit"
candidate_family: "seed_mutate"
input_format: "rar"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "archive-reader-clean-exit", "rar", "libfuzzer", "seed-mutate", "heap-use-after-free", "negative-memory", "round-33"]
match_keys: ["no_crash", "archive_reader_clean_exit", "rar", "libfuzzer", "seed-mutate", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Rar Seed Mutate No Crash Archive Reader Clean Exit Heap Use After Free Negative Memory

- key: `no_crash x archive_reader_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid old-RAR and PPMd-oriented seeds reached the archive reader but did not create the precise recoverable compressed-data failure followed by reuse of stale PPMd state. Direct PPMd-table mutations failed too early or cleanly, and multivolume split-continuation carriers remained clean when compressed data was perturbed. The missing relation appears to be a recoverable unsupported-filter return after PPMd allocation, followed by subsequent continuation/header processing before normal header reset clears the state.

## Policy
Treat `no_crash x archive_reader_clean_exit` on `rar` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `archive_reader_clean_exit`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `archive_reader_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[rar]]. Old RAR archives begin with the marker and main header, then CRC-checked block headers. File headers carry split-before/split-after flags, packed and unpacked sizes, compression method, name length/name, and then the packed stream. PPMd compressed blocks are selected inside the packed bitstream; a PPMd table can be allocated by flags in a new-code table, and later blocks may reuse that state if the stream marks a PPMd block without a dictionary allocation flag.

## Harness Contract
Use [[libfuzzer]]. The libarchive libFuzzer harness treats the entire input as a raw archive stream from memory, enables all filters and formats, repeatedly reads headers, drains each entry with archive_read_data until a nonpositive return, breaks only on ARCHIVE_FATAL, and frees the archive reader. There is no mode byte or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 24 attempts.
- Scope: generator repair and basin avoidance only.
