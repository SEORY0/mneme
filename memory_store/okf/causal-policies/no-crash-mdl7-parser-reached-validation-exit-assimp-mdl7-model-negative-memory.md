---
type: causal-policy
title: "No Crash Mdl7 Parser Reached Validation Exit Assimp Mdl7 Model Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal mdl7_parser_reached_validation_exit."
failure_class: "no_crash"
verifier_signal: "mdl7_parser_reached_validation_exit"
candidate_family: "seed_mutate"
input_format: "assimp-mdl7-model"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mdl7-parser-reached-validation-exit", "assimp-mdl7-model", "negative-memory", "round-9"]
match_keys: ["no_crash", "mdl7_parser_reached_validation_exit", "assimp-mdl7-model", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Mdl7 Parser Reached Validation Exit Assimp Mdl7 Model Negative Memory

- key: `no_crash x mdl7_parser_reached_validation_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[assimp-mdl7-model]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Real MDL7 samples reached the Assimp MDL importer and skin parsing, but mutations to external-skin
  and truncated skin payload shapes either failed validation or diverted into non-target allocation
  behavior.
- I did not isolate a ReadFirstSkin over-read that remained valid enough for the fixed/vulnerable
  differential.

## Policy
Treat `no_crash x mdl7_parser_reached_validation_exit` on `assimp-mdl7-model` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- MDL7 inputs begin with an MDL7 header carrying structure sizes and counts, followed by group
  records.
- Each group can contain skin records with a type, width, height, fixed-size texture name, and type-
  dependent payload such as embedded pixels or an external texture string.
- Header structure-size fields must match the importer constants or the loader rejects the file
  before skin parsing.

## Harness Contract
- The Assimp fuzzer passes the raw byte buffer directly to Importer::ReadFileFromMemory with the
  normal realtime postprocess preset.
- There is no prefix or mode byte; format selection is based on the model magic and importer
  probing.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `mdl7_parser_reached_validation_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
