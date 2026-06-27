---
type: causal-policy
title: "Ffmpeg Midivid Packet Construct Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 14 server-verified recovery for ffmpeg-midivid-packet keyed by wrong_sink x sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "ffmpeg-midivid-packet"
harness_convention: "afl/libfuzzer-compatible decoder fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "ffmpeg-midivid-packet", "afl-libfuzzer-compatible-decoder-fuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-14"]
match_keys: ["wrong_sink", "sink_mismatch", "ffmpeg-midivid-packet", "afl/libfuzzer-compatible decoder fuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Ffmpeg Midivid Packet Construct Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ffmpeg-midivid-packet]]
- related harness facts: [[afl-libfuzzer-compatible-decoder-fuzzer]]

## Policy
When `ffmpeg-midivid-packet` under `afl/libfuzzer-compatible decoder fuzzer` reaches `sink_mismatch` from `wrong_sink`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[afl-libfuzzer-compatible-decoder-fuzzer]]` and format contract `[[ffmpeg-midivid-packet]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Build a tiny intra-coded MidiVid packet with a valid vector table, then provide a block index greater than the available vector count. The FFmpeg target also needs the internal packet delimiter before the trailing codec configuration so the desired width and height are applied before decoding.
3. Keep mutations focused on the gate relation: declared size versus available data, selector versus subparser, structure count versus actual records, lifetime ownership, or sink-specific state.
4. If local labels report `wrong_sink` while the same parser branch is reached, submit once to check the official target match before discarding the candidate.
5. If the fixed image also fails, shrink back to the smallest boundary relation and avoid broad randomization.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not promote this as a byte recipe; it is a format-gate and sink-invariant relation.

## Evidence Shape
- Support: one server-verified Round 14 solve.
- Candidate family: construct.
