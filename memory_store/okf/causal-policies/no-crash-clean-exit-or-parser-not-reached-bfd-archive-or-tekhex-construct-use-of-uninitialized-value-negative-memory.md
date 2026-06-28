---
type: negative-memory
title: "No Crash Clean Exit Or Parser Not Reached Bfd Archive Or Tekhex Construct Use Of Uninitialized Value Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal clean_exit_or_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "clean_exit_or_parser_not_reached"
candidate_family: "construct"
input_format: "bfd-archive-or-tekhex"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-or-parser-not-reached", "bfd-archive-or-tekhex", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "clean_exit_or_parser_not_reached", "bfd-archive-or-tekhex", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Clean Exit Or Parser Not Reached Bfd Archive Or Tekhex Construct Use Of Uninitialized Value Negative Memory

- key: `no_crash x clean_exit_or_parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bfd-archive-or-tekhex]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Standalone TekHex-like text and an archive-wrapped TekHex member both executed cleanly. The likely missing relation is a complete BFD archive/object path that causes archive handling to instantiate a TekHex member and call the TekHex pass-over logic, rather than only accepting or rejecting the top-level file.

## Policy
Treat `no_crash x clean_exit_or_parser_not_reached` on `bfd-archive-or-tekhex` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_or_parser_not_reached` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_or_parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The fuzz target writes raw bytes to a temporary file and opens it through BFD with automatic target detection, then checks for archive format. TekHex records are percent-led text records carrying a length/type/integrity field prefix followed by line data. A complete BFD archive begins with the ar global marker and fixed-width member headers before member bytes.

## Harness Contract
The libFuzzer harness feeds the whole file bytes into BFD by way of a temporary file. There is no stdin protocol or FuzzedDataProvider carving; the bytes must form whatever BFD top-level format is needed to reach the inner object parser.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.
