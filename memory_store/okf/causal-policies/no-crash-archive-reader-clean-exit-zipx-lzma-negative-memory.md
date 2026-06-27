---
type: causal-policy
title: "No Crash Archive Reader Clean Exit Zipx Lzma Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal archive_reader_clean_exit."
failure_class: "no_crash"
verifier_signal: "archive_reader_clean_exit"
candidate_family: "seed_mutate_and_construct"
input_format: "zipx lzma"
harness_convention: "libfuzzer libarchive reader"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "archive-reader-clean-exit", "zipx-lzma", "libfuzzer-libarchive-reader", "negative-memory", "round-17"]
match_keys: ["no-crash", "archive-reader-clean-exit", "zipx-lzma", "libfuzzer-libarchive-reader", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Archive Reader Clean Exit Zipx Lzma Negative Memory

- key: `no_crash x archive_reader_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zipx-lzma]]
- related harness facts: [[libfuzzer-libarchive-reader]]

## Failure Shape
- A bundled ZIPX LZMA seed and short compressed-entry local-header variants were accepted or rejected cleanly.
- The missing condition appears to be a precise relation where the LZMA prologue is logically shorter than required while archive lookahead still exposes following bytes.

## Policy
Treat `no_crash x archive_reader_clean_exit` on `zipx lzma` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `archive_reader_clean_exit`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[zipx-lzma]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-libarchive-reader]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
