---
type: causal-policy
title: "No Crash Dpx Parser Processed Cleanly Dpx Image Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal dpx_parser_processed_cleanly."
failure_class: "no_crash"
verifier_signal: "dpx_parser_processed_cleanly"
candidate_family: "seed_mutate"
input_format: "dpx-image"
harness_convention: "afl-libfuzzer"
vuln_class: "incorrect-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dpx-parser-processed-cleanly", "dpx-image", "negative-memory", "round-13"]
match_keys: ["no_crash", "dpx_parser_processed_cleanly", "dpx-image", "afl-libfuzzer", "incorrect-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Dpx Parser Processed Cleanly Dpx Image Negative Memory

- key: `no_crash x dpx_parser_processed_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dpx-image]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
Repository DPX seeds with odd image widths and descriptor mutations to the CbCr family still processed cleanly. The missing trigger may require a DPX sample whose element packing, transfer characteristics, and pixel data are internally consistent for ColorDifferenceCbCr rather than simply changing the descriptor byte in RGB seeds.

## Policy
Treat `no_crash x dpx_parser_processed_cleanly` on `dpx-image` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `dpx_parser_processed_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
DPX files begin with a DPX magic and fixed-size headers describing pixel-data offset, image dimensions, element count, and per-element descriptors. ColorDifferenceCbCr elements are handled by a subsampled chroma path; the relevant validation relation is odd image width versus descriptor family.

## Harness Contract
The GraphicsMagick DPX AFL-compatible wrapper consumes the entire PoC as a DPX image file through the coder_DPX_fuzzer target. There is no front selector; parser reachability depends on a valid DPX header and element metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
