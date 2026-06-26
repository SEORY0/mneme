---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Postscript Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "postscript"
harness_convention: "libfuzzer"
vuln_class: "malformed-document-parse-crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "postscript", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "postscript", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Reached No Target Crash Postscript Negative Memory

## Policy
Treat `no_crash x parser_reached_no_target_crash` as a persistent failure basin for `postscript` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Minimal PostScript/EPS documents and DSC metadata variants parsed without reaching the malformed-document failure. The likely missing condition is a more specific DSC/resource edge case rather than ordinary PostScript syntax validity.

## Format and Harness Gates
- Format: The parser accepts raw PostScript/EPS streams with DSC comments such as document header, page count, bounding boxes, page records, and showpage content. DSC fields may use deferred or per-page forms, but well-formed minimal documents are handled cleanly.
- Harness: The libFuzzer target feeds the raw byte stream through a memory-backed FILE object into the libspectre document loader; there is no outer container, filename carving, or FuzzedDataProvider splitting.

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
