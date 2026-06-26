---
type: causal-policy
title: "No Crash Mapfile Parser Clean Mapserver Mapfile Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal mapfile_parser_clean."
failure_class: "no_crash"
verifier_signal: "mapfile_parser_clean"
candidate_family: "construct"
input_format: "mapserver-mapfile"
harness_convention: "libfuzzer-file-backed"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mapfile-parser-clean", "mapserver-mapfile", "negative-memory", "round-7"]
match_keys: ["no_crash", "mapfile_parser_clean", "mapserver-mapfile", "libfuzzer-file-backed", "heap-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Mapfile Parser Clean Mapserver Mapfile Negative Memory

- key: `no_crash x mapfile_parser_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mapserver-mapfile]]
- related harness facts: [[libfuzzer-file-backed]]

## Failure Shape
Five NUL-placement hypotheses across quoted strings, bare tokens, expression text, validation
metadata, and longer quoted strings all parsed cleanly or were rejected without a crash. The target
likely requires a lexer state where NUL participates in flex token length differently from C-string
length, but these mapfile carriers did not hit it.

## Policy
Treat `no_crash x mapfile_parser_clean` on `mapserver-mapfile` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `mapfile_parser_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
MapServer mapfiles are keyword-oriented text files with MAP/END block structure, quoted strings,
layer/web/validation subblocks, expressions, numeric fields, and comments. The lexer has separate
INITIAL, expression, and string states and accumulates quoted string contents into a reusable
buffer.

## Harness Contract
The fuzzer writes raw input bytes to a temporary file with a .map suffix, then calls msLoadMap on
that file and frees the result. Inputs outside a fixed size range are skipped; there is no mode
selector or FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
