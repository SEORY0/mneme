---
type: causal-policy
title: "Wrong Sink Parser Reached Id3 Txxx Copy Both Builds Crash Mpeg Ts With Id3 Metadata Negative Memory"
description: "Round 7 negative memory for wrong_sink with verifier signal parser_reached_id3_txxx_copy_both_builds_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_id3_txxx_copy_both_builds_crash"
candidate_family: "construct_ts_id3"
input_format: "mpeg-ts-with-id3-metadata"
harness_convention: "afl-libfuzzer-file-through-gpac-probe-analyze"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-id3-txxx-copy-both-builds-crash", "mpeg-ts-with-id3-metadata", "negative-memory", "round-7"]
match_keys: ["wrong_sink", "parser_reached_id3_txxx_copy_both_builds_crash", "mpeg-ts-with-id3-metadata", "afl-libfuzzer-file-through-gpac-probe-analyze", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# Wrong Sink Parser Reached Id3 Txxx Copy Both Builds Crash Mpeg Ts With Id3 Metadata Negative Memory

- key: `wrong_sink x parser_reached_id3_txxx_copy_both_builds_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mpeg-ts-with-id3-metadata]]
- related harness facts: [[afl-libfuzzer-file-through-gpac-probe-analyze]]

## Failure Shape
Raw ID3 was not routed by the probe/analyze filter graph. A minimal MPEG-TS carrier with PAT/PMT
metadata signaling did reach the HLS ID3 PES reframer and triggered an ID3 frame-size overread, but
official comparison showed the fixed build crashed too. The accepted target likely requires the
cover-art-specific ID3 relation rather than the generic text-frame copy relation.

## Policy
Treat `wrong_sink x parser_reached_id3_txxx_copy_both_builds_crash` on `mpeg-ts-with-id3-metadata` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_id3_txxx_copy_both_builds_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The successful reachability carrier is MPEG-TS with a PAT, PMT, metadata PES stream signaling, and
an ID3v2 tag in the PES payload. ID3v2 frames use a frame identifier, a synchsafe length, flags, and
a frame body; an oversized claimed frame length can affect parser copy bounds.

## Harness Contract
The selected GPAC fuzzer writes raw input to a temporary file and runs the probe/analyze filter
graph. Direct raw ID3 is not enough; the bytes must be classified as a media container that routes
to the MPEG-TS demuxer and ID3 PES reframer.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
