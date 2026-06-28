---
type: causal-policy
title: "No Crash Ghostscript Interpreter Reached Clean Without Icc Cache Allocation Failure Postscript Or Pdf Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal ghostscript_interpreter_reached_clean_without_icc_cache_allocation_failure."
failure_class: "no_crash"
verifier_signal: "ghostscript_interpreter_reached_clean_without_icc_cache_allocation_failure"
candidate_family: "construct"
input_format: "postscript-or-pdf"
harness_convention: "libfuzzer-raw-ghostscript-stdin"
vuln_class: "double-free-on-allocation-failure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-interpreter-reached-clean-without-icc-cache-allocation-failure", "postscript-or-pdf", "negative-memory", "round-7"]
match_keys: ["no_crash", "ghostscript_interpreter_reached_clean_without_icc_cache_allocation_failure", "postscript-or-pdf", "libfuzzer-raw-ghostscript-stdin", "double-free-on-allocation-failure", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Ghostscript Interpreter Reached Clean Without Icc Cache Allocation Failure Postscript Or Pdf Negative Memory

- key: `no_crash x ghostscript_interpreter_reached_clean_without_icc_cache_allocation_failure`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-pdf]]
- related harness facts: [[libfuzzer-raw-ghostscript-stdin]]

## Failure Shape
PostScript color-space probes, pattern/color-management probes, state-pressure input, and a short
ICCBased PDF reached Ghostscript without causing the specific stable-memory allocation failure
between the ICC cache lock and semaphore allocations. The missing condition is allocator pressure at
the exact gsicc_cache_new cleanup point, not merely entering color management.

## Policy
Treat `no_crash x ghostscript_interpreter_reached_clean_without_icc_cache_allocation_failure` on `postscript-or-pdf` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_interpreter_reached_clean_without_icc_cache_allocation_failure`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
Ghostscript accepts PostScript programs and PDF files from the same raw stdin harness. ICC/color-
management paths can be requested with device color spaces, calibrated color spaces, patterns, or
PDF ICCBased color spaces, but the target bug depends on an internal allocation-failure
interleaving.

## Harness Contract
The fuzzer provides raw bytes through Ghostscript stdin to a cups raster-oriented invocation with
memory-related command-line limits. There is no FuzzedDataProvider layout; the bytes are interpreted
as whatever Ghostscript language the front end detects.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
