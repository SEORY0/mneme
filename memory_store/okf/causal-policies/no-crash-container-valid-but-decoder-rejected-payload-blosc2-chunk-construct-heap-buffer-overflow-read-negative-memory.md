---
type: causal-policy
title: "No Crash Container Valid But Decoder Rejected Payload Blosc2 Chunk Construct Heap Buffer Overflow Read Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal container_valid_but_decoder_rejected_payload."
failure_class: "no_crash"
verifier_signal: "container_valid_but_decoder_rejected_payload"
candidate_family: "construct"
input_format: "blosc2-chunk"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "container-valid-but-decoder-rejected-payload", "blosc2-chunk", "negative-memory", "round-14"]
match_keys: ["no_crash", "container_valid_but_decoder_rejected_payload", "blosc2-chunk", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Container Valid But Decoder Rejected Payload Blosc2 Chunk Construct Heap Buffer Overflow Read Negative Memory

- key: `no_crash x container_valid_but_decoder_rejected_payload`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[blosc2-chunk]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Self-consistent regular chunk headers reached the chunk decompression harness, but malformed BloscLZ, LZ4, Lizard, zlib, and Zstd-marked streams returned cleanly. The missing condition is a format-valid compressed stream that enters the variable literal-length decoder instead of being rejected by the codec front end.

## Policy
Treat `no_crash x container_valid_but_decoder_rejected_payload` on `blosc2-chunk` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
