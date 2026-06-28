---
type: causal-policy
title: "Wrong Sink Both Images Crash Off Target C Blosc2 Frame Negative Memory"
description: "Round 7 negative memory for wrong_sink with verifier signal both_images_crash_off_target."
failure_class: "wrong_sink"
verifier_signal: "both_images_crash_off_target"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "both-images-crash-off-target", "c-blosc2-frame", "negative-memory", "round-7"]
match_keys: ["wrong_sink", "both_images_crash_off_target", "c-blosc2-frame", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# Wrong Sink Both Images Crash Off Target C Blosc2 Frame Negative Memory

- key: `wrong_sink x both_images_crash_off_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A valid frame seed triggered a crash in both images outside the target trailer read, while an
appended trailer-length mutation moved backward to clean execution. The target requires preserving
the accepted frame while mutating the internal trailer extent relation, not appending broad trailing
data.

## Policy
Treat `wrong_sink x both_images_crash_off_target` on `c-blosc2-frame` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crash_off_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
A c-blosc2 frame has a recognizable frame header, declared frame size, compressed chunk metadata and
payloads, plus optional trailer metadata. The target usermeta read derives a trailer offset from
header and compressed-size fields, then reads a trailer usermeta length and copies that many bytes
from the in-memory frame.

## Harness Contract
The libFuzzer target passes raw bytes to blosc2_schunk_open_sframe, then decompresses chunks from
the returned super-chunk. Parser reachability depends on a coherent in-memory frame; the fuzzer does
not carve a mode byte.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
