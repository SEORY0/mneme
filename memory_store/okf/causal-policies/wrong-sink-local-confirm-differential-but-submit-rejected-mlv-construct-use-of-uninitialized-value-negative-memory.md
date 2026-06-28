---
type: negative-memory
title: "Wrong Sink Local Confirm Differential But Submit Rejected Mlv Construct Use Of Uninitialized Value Negative Memory"
description: "Round 25 negative memory for wrong_sink with verifier signal local_confirm_differential_but_submit_rejected."
failure_class: "wrong_sink"
verifier_signal: "local_confirm_differential_but_submit_rejected"
candidate_family: "construct"
input_format: "mlv"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "local-confirm-differential-but-submit-rejected", "mlv", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["wrong_sink", "local_confirm_differential_but_submit_rejected", "mlv", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Wrong Sink Local Confirm Differential But Submit Rejected Mlv Construct Use Of Uninitialized Value Negative Memory

- key: `wrong_sink x local_confirm_differential_but_submit_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mlv]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A valid MLV header plus a metadata block whose declared string payload exceeded the available bytes reached the read_string path and produced a MemorySanitizer uninitialized-value report locally. Local confirmation reported the patched image clean, but server submission twice returned fixed-side failure, so the official solve was not accepted.

## Policy
Treat `wrong_sink x local_confirm_differential_but_submit_rejected` on `mlv` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `local_confirm_differential_but_submit_rejected` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_confirm_differential_but_submit_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
MLV files are block streams. Each block has a tag, declared size, timestamp area, and payload. Several metadata tags contain fixed-width strings read into freshly allocated buffers; if the declared block payload is large enough for the parser branch but the actual file ends early, unchecked reads can leave string bytes uninitialized.

## Harness Contract
The FFmpeg demuxer fuzzer feeds the raw bytes to the MLV demuxer through libavformat. The target first validates the main MLV header, creates streams based on header class and frame counts, then scans primary and possible secondary block streams.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.
