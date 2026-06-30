---
type: negative-memory
title: "No Crash No Crash No Leak Signal DWG DXF JSON Construct Seed Mutate Improper Memory Management Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal no_crash_no_leak_signal."
failure_class: "no_crash"
verifier_signal: "no_crash_no_leak_signal"
candidate_family: "construct|seed_mutate"
input_format: "dwg-dxf-json"
harness_convention: "libfuzzer"
vuln_class: "improper-memory-management"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "no-crash-no-leak-signal", "dwg-dxf-json", "libfuzzer", "construct-seed-mutate", "negative-memory", "round-26"]
match_keys: ["no_crash", "no_crash_no_leak_signal", "dwg-dxf-json", "libfuzzer", "improper-memory-management", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash No Crash No Leak Signal DWG DXF JSON Construct Seed Mutate Improper Memory Management Negative Memory

- key: `no_crash x no_crash_no_leak_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwg-dxf-json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The described issue appears tied to a command-line error path for freeing partially initialized conversion state. The available local fuzzer harness dispatches raw input among DWG, JSON, and DXF importers, frees critical-error states internally, and has leak detection disabled. Minimal DXF scaffolds, JSON critical-error inputs, OBJECTS-section DXF scaffolds, real DWG/DXF seeds, and one official wrong-format seed submit all remained clean.

## Policy
Treat `no_crash x no_crash_no_leak_signal` on `dwg-dxf-json` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `no_crash_no_leak_signal` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `no_crash_no_leak_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
DWG inputs are binary drawings with a release marker at the beginning. DXF inputs are text group-code/value streams organized into sections such as HEADER and OBJECTS. JSON import starts from an object-shaped text stream. The fuzz target selects the parser family from the input prefix rather than from a file extension.

## Harness Contract
The libFuzzer harness consumes raw bytes. It routes drawing-marker inputs to the DWG decoder, object-prefix text to JSON import, and all other inputs to DXF import. It appends a terminator for text-oriented paths when needed, writes one randomly selected output format to a null sink after a successful import, then frees the drawing object.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 8 attempts.
- Scope: generator repair and basin avoidance only.
