---
type: causal-policy
title: "Rawspeed Ljpeg Fuzzer Struct Construct Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "rawspeed-ljpeg-fuzzer-struct"
harness_convention: "afl-libfuzzer-file"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "rawspeed-ljpeg-fuzzer-struct", "afl-libfuzzer-file", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "rawspeed-ljpeg-fuzzer-struct", "afl-libfuzzer-file", "heap-buffer-overflow-write", "verified_recovery", "construct", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Rawspeed Ljpeg Fuzzer Struct Construct Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct the direct RawSpeed LJpeg decompressor harness envelope, not a camera file. Keep the RawImage metadata valid as an unsigned 16-bit image with three components per pixel, then provide a big-endian lossless JPEG stream whose frame and scan advertise four components. Use a simple valid Huffman table and enough scan data for the slice decoder to write across a wide one-row slice; the vulnerable width clipping uses the wrong component ratio, while the fixed build clips the current slice cleanly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[rawspeed-ljpeg-fuzzer-struct]]: The fuzzer input begins with little-endian RawImage metadata: dimensions, image type, components per pixel, CFA flag, followed by little-endian tile X/Y offsets and a compatibility flag. The remaining bytes are parsed by the LJpeg decompressor after it switches the stream to big-endian. The LJpeg stream must start with SOI and include coherent DHT, SOF3, and SOS marker segments; SOF component descriptors and SOS table selectors must agree so decodeN selects the intended component count.
- Harness [[afl-libfuzzer-file]]: The harness reads the raw file bytes as one ByteStream. There is no prefix selector or FuzzedDataProvider split. It creates a RawImage from the front scalar fields, reads tile offset and flag fields, allocates image data, constructs LJpegDecompressor over the remaining bytes, and catches RawSpeed exceptions, so clean exits usually mean a parser gate or slice-write relation was not reached.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[rawspeed-ljpeg-fuzzer-struct]] and [[afl-libfuzzer-file]].
