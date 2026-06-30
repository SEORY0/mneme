---
type: negative-memory
title: "No Crash Archive Reader Clean Exit Rar Seed Sweep And Header Stream Mutation Heap Use After Free Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal archive_reader_clean_exit."
failure_class: "no_crash"
verifier_signal: "archive_reader_clean_exit"
candidate_family: "seed_sweep-and-header_stream_mutation"
input_format: "rar"
harness_convention: "libfuzzer-libarchive-reader"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "archive-reader-clean-exit", "rar", "libfuzzer-libarchive-reader", "seed-sweep-and-header-stream-mutation", "negative-memory", "round-26"]
match_keys: ["no_crash", "archive_reader_clean_exit", "rar", "libfuzzer-libarchive-reader", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Archive Reader Clean Exit Rar Seed Sweep And Header Stream Mutation Heap Use After Free Negative Memory

- key: `no_crash x archive_reader_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar]]
- related harness facts: [[libfuzzer-libarchive-reader]]

## Failure Shape
Valid old-RAR compressed and PPMd seeds reached the libarchive reader but did not produce the run_filters failure. The dedicated in-repo old-RAR filter fixture also executed cleanly under official submit, and its size exceeded the verifier's normal single-input read limit, making it a poor direct carrier. Header-consistent size and dictionary mutations plus compressed-stream perturbations preserved archive recognition but did not create the required queued VM-filter stack relation.

## Policy
Treat `no_crash x archive_reader_clean_exit` on `rar` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `archive_reader_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `archive_reader_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Old RAR archives begin with the RAR marker, a main header, then file headers whose header CRC is checked before data decoding. File headers carry dictionary flags, compressed and uncompressed sizes, method, name length, and filename before the compressed stream. RAR VM filters are encoded inside compressed data; the reader decodes filter flags, block start, block length, optional registers, bytecode, and optional global data, queues filters, and later executes queued filters over the LZSS window.

## Harness Contract
The libarchive fuzzer consumes the whole raw archive byte stream from memory, enables all filters and formats, opens the archive, iterates headers, drains entry data, and frees the archive. There is no mode byte and no FuzzedDataProvider carving; the input must be a complete archive stream.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 27 attempts.
- Scope: generator repair and basin avoidance only.
