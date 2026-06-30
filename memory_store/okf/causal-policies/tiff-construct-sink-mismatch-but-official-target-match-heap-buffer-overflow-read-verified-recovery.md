---
type: causal-policy
title: "Tiff Construct Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "tiff"
harness_convention: "libfuzzer-gdal"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-but-official-target-match", "tiff", "libfuzzer-gdal", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "sink_mismatch_but_official_target_match", "tiff", "libfuzzer-gdal", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Tiff Construct Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal classic TIFF that is still acceptable to the LIBERTIFF metadata path, include a large out-of-line double-array metadata tag whose stored value offset is zero, and avoid the regular GTiff path consuming the file first.
2. The vulnerable reader treats the zero offset as inline storage and copies the declared element count from a single inline slot; the fixed build rejects that offline zero-offset case.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Classic TIFF uses an endian marker, a TIFF magic value, and an image-file-directory containing tag entries with type, count, and either inline value bytes or a value offset.
- Values whose byte count exceeds the inline field are out-of-line.
- GDAL may register both GTiff and LIBERTIFF for the same TIFF signature; keeping enough raster metadata for LIBERTIFF while omitting a raster data pointer can steer away from the regular GTiff open path.
- Harness [[libfuzzer-gdal]]:
  - The run_poc wrapper reads the submitted file as raw bytes.
  - The GDAL fuzzer places those bytes at a fixed in-memory filename, calls GDALAllRegister, opens that filename read-only, then probes raster bands and metadata.
  - There is no FuzzedDataProvider, mode byte, checksum gate, or archive wrapper.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[tiff]] and [[libfuzzer-gdal]].
