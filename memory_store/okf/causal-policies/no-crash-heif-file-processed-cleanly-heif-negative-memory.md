---
type: causal-policy
title: "No Crash Heif File Processed Cleanly Heif Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal heif_file_processed_cleanly."
failure_class: "no_crash"
verifier_signal: "heif_file_processed_cleanly"
candidate_family: "seed_mutate"
input_format: "heif"
harness_convention: "libfuzzer"
vuln_class: "invalid-reference-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "heif-file-processed-cleanly", "heif", "negative-memory", "round-12"]
match_keys: ["no_crash", "heif_file_processed_cleanly", "heif", "libfuzzer", "invalid-reference-handling", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Heif File Processed Cleanly Heif Negative Memory

- key: `no_crash x heif_file_processed_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[heif]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid HEIF seeds and a simple appended mask-reference-looking mutation reached the file fuzzer cleanly but did not create a parsed region annotation with a referenced-mask geometry whose mask reference points at an invalid image item.

## Policy
Treat `no_crash x heif_file_processed_cleanly` on `heif` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The target format is an ISO BMFF HEIF file. Region annotations are stored as region items and assigned to images through item references. Referenced mask regions require region data plus a mask item reference, and the vulnerable relation is whether that referenced item is a valid image.

## Harness Contract
The file fuzzer checks file type, reads the full raw input into a heif_context, obtains primary and top-level image handles, decodes images, and queries thumbnails and metadata. There is no fuzzer-specific selector; the HEIF box graph must be structurally valid enough for context loading.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `heif_file_processed_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
