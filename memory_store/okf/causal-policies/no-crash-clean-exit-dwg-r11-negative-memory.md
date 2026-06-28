---
type: causal-policy
title: "No Crash Clean Exit Dwg R11 Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "seed_mutate"
input_format: "dwg-r11"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "dwg-r11", "negative-memory", "round-7"]
match_keys: ["no_crash", "clean_exit", "dwg-r11", "libfuzzer", "integer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Clean Exit Dwg R11 Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwg-r11]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A modern DWG seed, synthetic old-version stubs, real R11 samples, and R11 entity-boundary mutations
all exited cleanly. The real samples reached the old-version format family, but the targeted
overflow likely requires internally consistent section headers, header variables, CRC/sentinel
state, and entity boundaries rather than mutating the entity-end field alone.

## Policy
Treat `no_crash x clean_exit` on `dwg-r11` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
LibreDWG chooses binary DWG when the input begins with an AutoCAD version signature. Pre-R13/R11
files contain section boundary fields for entities and table sections, followed by header variables,
CRC/sentinel data, and entity/table payloads whose offsets must remain mutually consistent.

## Harness Contract
The harness passes raw bytes to LibreDWG. Inputs starting like DWG select binary decoding, inputs
starting with a JSON object select JSON import, and other text-like inputs can fall through to DXF
handling.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
