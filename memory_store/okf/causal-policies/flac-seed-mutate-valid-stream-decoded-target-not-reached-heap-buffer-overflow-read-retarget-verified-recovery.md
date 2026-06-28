---
type: causal-policy
title: "FLAC Seed Mutate Valid Stream Decoded Target Not Reached Heap Buffer Overflow Read Retarget Verified Recovery"
description: "Retarget-verified recovery for flac after no_crash with verifier signal valid_stream_decoded_target_not_reached."
failure_class: "no_crash"
verifier_signal: "valid_stream_decoded_target_not_reached"
candidate_family: "seed_mutate"
input_format: "flac"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "valid-stream-decoded-target-not-reached", "flac", "libfuzzer", "seed-mutate", "retarget-verified-recovery", "round-18"]
match_keys: ["no-crash", "valid-stream-decoded-target-not-reached", "flac", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# FLAC Seed Mutate Valid Stream Decoded Target Not Reached Heap Buffer Overflow Read Retarget Verified Recovery

- key: `no_crash x valid_stream_decoded_target_not_reached`
- outcome: retarget check flipped a prior round failure to a server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[flac]]
- related harness facts: [[libfuzzer]]

## Policy
When a FLAC candidate reaches clean decode but not the target, do not abandon the valid-stream carrier. Preserve STREAMINFO, frame, subframe, and CRC coherence, then retarget the residual bitreader relation: the vulnerable path needs an accepted audio frame whose partitioned Rice residual leaves the signed-block reader consuming beyond the accepted tail while the fixed image rejects or guards that relation.

## Procedure
1. Start from a valid FLAC stream that the decoder accepts through metadata and at least one audio frame.
2. Preserve the frame header and subframe gates while changing residual coding parameters, partition order, and residual payload length together.
3. Keep checks that make the frame decodable enough to enter the Rice signed-block reader; random corruption that causes early frame rejection returns to the `valid_stream_decoded_target_not_reached` basin.
4. Submit only candidates that separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not count valid metadata decode, clean frame rejection, or a clean end-of-stream as progress for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[flac]] for marker, metadata, frame, subframe, and residual-coding invariants.

## Harness Contract
Use [[libfuzzer]]; the harness consumes one raw FLAC byte stream with no selector or FuzzedDataProvider fields.

## Evidence Shape
- Support: 1 round 18 retarget check with official vulnerable/fixed split.
- Candidate family: seed_mutate.
