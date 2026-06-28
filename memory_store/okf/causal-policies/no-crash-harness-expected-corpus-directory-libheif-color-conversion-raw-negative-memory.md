---
type: causal-policy
title: "No Crash Harness Expected Corpus Directory Libheif Color Conversion Raw Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal harness_expected_corpus_directory."
failure_class: "no_crash"
verifier_signal: "harness_expected_corpus_directory"
candidate_family: "construct_and_seed_mutate"
input_format: "libheif-color-conversion-raw"
harness_convention: "libfuzzer-wrapper-file-contract-mismatch"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "harness-expected-corpus-directory", "libheif-color-conversion-raw", "negative_memory", "round-8"]
match_keys: ["no_crash", "harness_expected_corpus_directory", "libheif-color-conversion-raw", "libfuzzer-wrapper-file-contract-mismatch", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Harness Expected Corpus Directory Libheif Color Conversion Raw Negative Memory

## Policy
Treat `no_crash x harness_expected_corpus_directory` as a persistent failure basin for `libheif-color-conversion-raw` under `libfuzzer-wrapper-file-contract-mismatch`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Every candidate, including structurally valid color-conversion buffers, stopped before the fuzzer body because the wrapped libFuzzer binary treated the file path as a corpus directory. This prevented reaching the color conversion overflow regardless of the byte layout.

## Format and Harness Gates
- Format: When reachable, the color-conversion input begins with fixed-width image parameters, followed by chroma/colorspace selectors and then raw plane bytes. Width and height must be nonzero even values, bit depth must be supported, chroma/colorspace enums must be valid, and plane sizes must match the selected layout.
- Harness: The intended fuzzer reads raw bytes front-to-back from a memory stream, but the benchmark wrapper invokes the libFuzzer binary with a regular file path in a way this target interprets as a required corpus directory. No candidate file reached LLVMFuzzerTestOneInput in local verification.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
