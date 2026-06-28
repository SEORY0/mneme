---
type: causal-policy
title: "Generic Crash Sink Mismatch Low Likelihood Postscript Eps Negative Memory"
description: "Round 8 negative memory for generic_crash with verifier signal sink_mismatch_low_likelihood."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch_low_likelihood"
candidate_family: "seed_mutate_and_construct"
input_format: "postscript-eps"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "sink-mismatch-low-likelihood", "postscript-eps", "negative_memory", "round-8"]
match_keys: ["generic_crash", "sink_mismatch_low_likelihood", "postscript-eps", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# Generic Crash Sink Mismatch Low Likelihood Postscript Eps Negative Memory

## Policy
Treat `generic_crash x sink_mismatch_low_likelihood` as a persistent failure basin for `postscript-eps` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Valid PostScript/EPS samples loaded cleanly, while binary data after a PostScript header produced only a low-likelihood generic crash. The attempts did not isolate the specific failed-read path that leaves libspectre variables uninitialized while also staying differential against the fixed image.

## Format and Harness Gates
- Format: The input is a PostScript or EPS stream read from memory-backed FILE I/O. Ordinary PostScript headers and EPS examples reach document loading, but malformed binary tails can shift failure into generic interpreter handling rather than the target variable-initialization path.
- Harness: The fuzzer feeds raw bytes through fmemopen into spectre_document_load_from_stream, then checks document status and frees the document. There is no mode selector, sidecar file, or back-loaded FuzzedDataProvider field.

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
