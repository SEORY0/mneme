---
type: causal-policy
title: "C Blosc2 Frame Seed Mutate Official Target Match Heap Use After Free Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal official_target_match."
failure_class: "generic_crash"
verifier_signal: "official_target_match"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match", "c-blosc2-frame", "libfuzzer", "seed-mutate", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "official_target_match", "c-blosc2-frame", "libfuzzer", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# C Blosc2 Frame Seed Mutate Official Target Match Heap Use After Free Verified Recovery

- key: `generic_crash x official_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[c-blosc2-frame]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a valid contiguous c-blosc2 frame so the msgpack frame header, frame lengths, chunk index, trailer, and embedded chunk sizes remain self-consistent. Mutate one embedded chunk's block-start entry so decompression enters a split-block stream with too little remaining input to read the next cbytes token. Leave the surrounding frame and chunk extent declarations intact; the vulnerable build trusts the malformed stream boundary, while the fixed build rejects it as a decompression error.

## Policy
For `generic_crash x official_target_match` on `c-blosc2-frame`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `c-blosc2-frame` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `c-blosc2-frame` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
A c-blosc2 frame has a msgpack header with magic, frame length, total uncompressed/compressed sizes, type size, chunk size, codec flags, filter pipeline, and metalayer index, followed by sequential Blosc chunks, an offsets/index chunk, and a msgpack trailer. Embedded Blosc chunks may use the extended chunk header when both shuffle flags are present; in that form, the block-start table follows the filter metadata. Each block then contains one or more compressed streams, each introduced by a signed cbytes token; negative token values encode run-filled streams.

## Harness Contract
The task image's wrapper invokes a libFuzzer frame target over a corpus directory. The fuzzer target receives raw frame bytes, opens an in-memory super-chunk from the frame, allocates an output buffer from the frame metadata, and decompresses chunks in order. The repository's model-free local verify wrapper copies the candidate to a file path where this image expects a directory, so direct single-input libFuzzer execution was used for local differential evidence and runner submit was used for the official verdict.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 8 attempts.
- Scope: generator repair and retargeting only.
