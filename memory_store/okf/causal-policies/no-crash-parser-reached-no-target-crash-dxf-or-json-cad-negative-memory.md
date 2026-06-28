---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Dxf Or Json Cad Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "dxf-or-json-cad"
harness_convention: "libfuzzer-libredwg-llvmfuzz"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "dxf-or-json-cad", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "dxf-or-json-cad", "libfuzzer-libredwg-llvmfuzz", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached No Target Crash Dxf Or Json Cad Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf-or-json-cad]]
- related harness facts: [[libfuzzer-libredwg-llvmfuzz]]

## Failure Shape
Bundled DXF seeds and constructed inputs with custom class names, unknown entity names, dimension subclass rewrites, duplicate class/object names, and JSON dxfname fields all parsed and cleaned up without a sanitizer finding. The missing gate is likely a more precise DXF import state where ownership of the same dxfname allocation is transferred to an object or class and then also freed on an error or export cleanup path.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `dxf-or-json-cad` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The fuzzer sniffs DWG by an AC prefix, JSON by an opening brace, and otherwise treats input as DXF text. DXF is group-code text with SECTION records such as HEADER, CLASSES, ENTITIES, and OBJECTS; object type names and subclass markers are carried as string-valued group pairs and become dxfname-related fields during import.

## Harness Contract
The llvmfuzz target copies and null-terminates text-like inputs, imports DWG, JSON, or DXF into a Dwg_Data object, chooses one output path from the enabled encoders using the process PRNG, writes to a null sink, then frees the Dwg_Data. PoC reachability therefore includes both import cleanup and the selected export cleanup path.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
