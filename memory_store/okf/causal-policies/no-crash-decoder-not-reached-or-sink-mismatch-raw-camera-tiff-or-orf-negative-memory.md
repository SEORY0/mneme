---
type: causal-policy
title: "No Crash Decoder Not Reached Or Sink Mismatch Raw Camera Tiff Or Orf Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal decoder_not_reached_or_sink_mismatch."
failure_class: "no_crash"
verifier_signal: "decoder_not_reached_or_sink_mismatch"
candidate_family: "construct"
input_format: "raw-camera-tiff-or-orf"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-not-reached-or-sink-mismatch", "raw-camera-tiff-or-orf", "negative_memory", "round-8"]
match_keys: ["no_crash", "decoder_not_reached_or_sink_mismatch", "raw-camera-tiff-or-orf", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Decoder Not Reached Or Sink Mismatch Raw Camera Tiff Or Orf Negative Memory

## Policy
Treat `no_crash x decoder_not_reached_or_sink_mismatch` as a persistent failure basin for `raw-camera-tiff-or-orf` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- TIFF/ORF-like headers reached only shallow parser behavior or low-likelihood generic failure. The inputs did not satisfy enough Olympus RAW IFD structure to reach OrfDecoder strip offsets, strip byte counts, dimensions, and the compressed decode IOException path.

## Format and Harness Gates
- Format: The target decoder is selected from a RAW camera container with TIFF-style byte order, an IFD tree, compression metadata, strip offsets, strip byte counts, and even image dimensions. The vulnerable path requires compression accepted by the Olympus decoder and strip data that raises an IOException during raw decoding.
- Harness: The libFuzzer target gives the entire raw byte buffer to RawParser, obtains a decoder, disables crop/unknown-model failure, then calls decodeRaw and decodeMetaData. Rawspeed exceptions are caught by the harness, so non-target parser errors become clean exits.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
