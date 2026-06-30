---
type: causal-policy
title: "Blosc2 Frame Construct Sink Mismatch Allocation Size Too Big Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "allocation-size-too-big"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "blosc2-frame", "libfuzzer", "construct", "allocation-size-too-big", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "sink_mismatch", "blosc2-frame", "libfuzzer", "allocation-size-too-big", "wrong-sink", "sink-mismatch", "blosc2-frame", "libfuzzer", "allocation-size-too-big", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Blosc2 Frame Construct Sink Mismatch Allocation Size Too Big Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[blosc2-frame]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x sink_mismatch` on `blosc2-frame`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a structurally valid in-memory Blosc2 frame with no data chunks, self-consistent header and total lengths, and a valid metalayer index that points at one serialized metalayer value. Keep the value marker valid but make the signed content length negative, so the vulnerable parser accepts the metalayer envelope and then uses that negative length as an allocation/copy size. The fixed build rejects that length before the allocation path.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[blosc2-frame]]: A Blosc2 frame header is a msgpack-like fixed header containing a magic string, header length, total frame length, flags, data sizes, type size, chunk size, thread counts, optional usermeta flag, and filter pipeline. The metalayer section is appended to the header as a small array containing a size field, a map from short metalayer names to value-record locations, and an array of serialized value records. A frame with zero data sizes and zero chunk size can still reach metalayer parsing as long as the header, total length, and trailer are self-consistent.
- Harness [[libfuzzer]]: The target is the raw-byte libFuzzer decompress-frame harness: the input bytes are passed directly to LLVMFuzzerTestOneInput, which opens them as an in-memory frame. There is no FuzzedDataProvider splitting. The local arvo wrapper invokes the libFuzzer binary on a fixed path; for this 32-bit fuzzer, local single-file verification needed staging the copied file into a tmpfs-backed path before running the fuzzer once.

## Negative Memory
- Do not corrupt the outer `blosc2-frame` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[blosc2-frame]] and [[libfuzzer]].
