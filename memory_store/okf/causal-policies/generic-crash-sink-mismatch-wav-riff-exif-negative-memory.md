---
type: causal-policy
title: "Generic Crash Sink Mismatch Wav Riff Exif Negative Memory"
description: "Round 12 negative memory for generic_crash with verifier signal sink_mismatch."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "wav-riff-exif"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "sink-mismatch", "wav-riff-exif", "negative-memory", "round-12"]
match_keys: ["generic_crash", "sink_mismatch", "wav-riff-exif", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# Generic Crash Sink Mismatch Wav Riff Exif Negative Memory

- key: `generic_crash x sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wav-riff-exif]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The candidates reached RIFF/WAV parsing and exercised LIST/EXIF subchunk shapes, including EXIF string records and oversized string records, but the server rejected the generic crashes as off-target. The likely missing piece is a more faithful EXIF audio subrecord sequence that reaches the uninitialized-value use rather than error cleanup or unrelated parser exits.

## Policy
Treat `generic_crash x sink_mismatch` on `wav-riff-exif` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
A RIFF/WAV file needs a RIFF container, WAVE form marker, a valid audio format chunk, and then metadata chunks. LIST/INFO-style metadata contains nested four-character markers; an EXIF nested marker dispatches to EXIF subrecords, several of which carry a length followed by string-like data.

## Harness Contract
The sndfile libFuzzer target feeds the raw buffer through virtual file I/O into libsndfile open/read paths. There is no harness prefix; all structure comes from the RIFF/WAV container.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `sink_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
