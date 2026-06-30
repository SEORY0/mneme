---
type: causal-policy
title: "PNG Construct Sink Mismatch Use Of Uninitialized Value Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "png"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "png", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "sink_mismatch", "png", "libfuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# PNG Construct Sink Mismatch Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x sink_mismatch`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a structurally valid minimal PNG so the header probe accepts it, then put a zlib-wrapped DEFLATE stream in the image data chunk.
2. The triggering stream should start with a length/distance copy before any output history exists, using an invalid maximum distance symbol that the vulnerable decoder maps to a zero-base distance.
3. This leaves uninitialized bytes in the decoded scanline that are consumed by PNG filtering; the fixed decoder rejects the invalid DEFLATE symbol cleanly.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- PNG is a chunk stream with a fixed signature, an image header chunk before image data, and zlib-wrapped DEFLATE bytes in image-data chunks.
- Chunk framing is big-endian length, type, data, and checksum; the decoder reaches the DEFLATE path when the image header is coherent and image dimensions remain within the harness limit.
- Harness [[libfuzzer]]:
  - The stb_image libFuzzer harness feeds raw file bytes directly to the memory parser.
  - It first calls the info parser as a reachability gate, rejects very large decoded dimensions, and then decodes the same raw bytes requesting RGBA output.
  - There is no leading mode selector, datasource wrapper, filename, or FuzzedDataProvider layout.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[png]] and [[libfuzzer]].
