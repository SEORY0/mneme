---
type: causal-policy
title: "No Crash Clean Exit Some Probe Reachability Mpeg Video Elementary Or Program Stream Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal clean_exit_some_probe_reachability."
failure_class: "no_crash"
verifier_signal: "clean_exit_some_probe_reachability"
candidate_family: "construct"
input_format: "mpeg-video-elementary-or-program-stream"
harness_convention: "libfuzzer-gpac-probe-analyze"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-some-probe-reachability", "mpeg-video-elementary-or-program-stream", "negative-memory", "round-7"]
match_keys: ["no_crash", "clean_exit_some_probe_reachability", "mpeg-video-elementary-or-program-stream", "libfuzzer-gpac-probe-analyze", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Clean Exit Some Probe Reachability Mpeg Video Elementary Or Program Stream Negative Memory

- key: `no_crash x clean_exit_some_probe_reachability`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mpeg-video-elementary-or-program-stream]]
- related harness facts: [[libfuzzer-gpac-probe-analyze]]

## Failure Shape
MP4 seed mutation and simple MPEG elementary streams stayed clean. MPEG sequence headers, MPEG-2
extension headers, program-stream/PES wrapping, and MPEG-4 Visual VOS/VOL headers with short or long
user-data tails also stayed clean. One MPEG-4 Visual variant reached the rfmpgvid filter family, but
not the vulnerable string-read condition, suggesting the remaining gap is a valid decoder-config
aggregation that places a start-code-delimited user-data string at the exact end of collected header
bytes.

## Policy
Treat `no_crash x clean_exit_some_probe_reachability` on `mpeg-video-elementary-or-program-stream` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_some_probe_reachability`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
GPAC's MPEG video reframer recognizes MPEG-1/2 and MPEG-4 Visual start-code streams. The decoder-
config cleanup path scans collected header bytes for start-code prefixes and checks user-data-like
payloads for packed-bitstream markers.

## Harness Contract
The harness writes the raw input to a temporary file and runs GPAC probe/analyze parsing. There is
no mode byte; format detection is by container signatures, file-extension-like probing, and
elementary-stream start codes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
