---
type: causal-policy
title: "Generic Crash Local Crash Rejected By Official Submission Blosc Compressed Chunk Negative Memory"
description: "Round 12 negative memory for generic_crash with verifier signal local_crash_rejected_by_official_submission."
failure_class: "generic_crash"
verifier_signal: "local_crash_rejected_by_official_submission"
candidate_family: "construct"
input_format: "blosc compressed chunk"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-or-invalid-memory"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-crash-rejected-by-official-submission", "blosc-compressed-chunk", "negative-memory", "round-12"]
match_keys: ["generic_crash", "local_crash_rejected_by_official_submission", "blosc-compressed-chunk", "libfuzzer", "use-of-uninitialized-or-invalid-memory", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# Generic Crash Local Crash Rejected By Official Submission Blosc Compressed Chunk Negative Memory

- key: `generic_crash x local_crash_rejected_by_official_submission`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[blosc-compressed-chunk]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A syntactically valid one-block Blosc chunk using the zlib/miniz codec was accepted by the chunk harness. Mutating the embedded fixed-Huffman deflate stream to use an invalid distance symbol produced a local segmentation fault, but confirmation showed the fixed build was not clean and the official server rejected the candidate.

## Policy
Treat `generic_crash x local_crash_rejected_by_official_submission` on `blosc-compressed-chunk` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
A raw Blosc chunk has a compact header containing version, codec flags, element size, uncompressed size, block size, and compressed size. Non-memcpy chunks include a block-start table followed by one or more block payloads; each compressed stream stores its compressed byte count before codec data. The chunk fuzzer validates that the header compressed size equals the whole input size and allocates the output buffer from that compressed size.

## Harness Contract
The c-blosc2 harness consumes raw bytes as a single compressed chunk, not a frame. It rejects inputs smaller than the minimum header, rejects inconsistent header sizes, validates the chunk, then calls blosc2_decompress into a buffer sized from the compressed chunk length.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_crash_rejected_by_official_submission`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
