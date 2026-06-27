---
type: causal-policy
title: "No Crash Rar5 Fixture Reached Clean Exit Rar5 Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal rar5_fixture_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "rar5_fixture_reached_clean_exit"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "rar5-fixture-reached-clean-exit", "rar5", "negative-memory", "round-13"]
match_keys: ["no_crash", "rar5_fixture_reached_clean_exit", "rar5", "libfuzzer", "heap-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Rar5 Fixture Reached Clean Exit Rar5 Negative Memory

- key: `no_crash x rar5_fixture_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The in-tree RAR5 different-window-size fixture parsed without a crash under the single-buffer libarchive fuzzer. The remaining gap is likely reproducing the multi-volume continuation state that the unit test exercises through archive sequencing rather than only replaying one raw archive buffer.

## Policy
Treat `no_crash x rar5_fixture_reached_clean_exit` on `rar5` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `rar5_fixture_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
RAR5 inputs start with the RAR5 marker, then CRC-protected variable-length base block headers. FILE base blocks carry split-before/split-after flags, data size, unpacked size, compression metadata, and a dictionary/window-size selector; header CRC validity is a hard parser gate.

## Harness Contract
The libarchive harness feeds the entire input as one archive byte stream through archive_read_support_format_all and drains each entry with archive_read_data. It does not provide separate filenames or external multi-volume files.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x rar5_fixture_reached_clean_exit`
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
The in-tree RAR5 different-window-size fixture parsed without a crash under the single-buffer libarchive fuzzer. The remaining gap is likely reproducing the multi-volume continuation state that the unit test exercises through archive sequencing rather than only replaying one raw archive buffer.

### Format Contract Delta
RAR5 inputs start with the RAR5 marker, then CRC-protected variable-length base block headers. FILE base blocks carry split-before/split-after flags, data size, unpacked size, compression metadata, and a dictionary/window-size selector; header CRC validity is a hard parser gate.

### Harness Contract Delta
The libarchive harness feeds the entire input as one archive byte stream through archive_read_support_format_all and drains each entry with archive_read_data. It does not provide separate filenames or external multi-volume files.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
