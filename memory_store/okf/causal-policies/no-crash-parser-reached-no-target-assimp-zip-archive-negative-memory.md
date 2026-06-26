---
type: causal-policy
title: "No Crash Parser Reached No Target Assimp Zip Archive Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_reached_no_target."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target"
candidate_family: "construct"
input_format: "assimp-zip-archive"
harness_convention: "libfuzzer"
vuln_class: "integer-underflow-loop"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target", "assimp-zip-archive", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_reached_no_target", "assimp-zip-archive", "libfuzzer", "integer-underflow-loop", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Reached No Target Assimp Zip Archive Negative Memory

- key: `no_crash x parser_reached_no_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[assimp-zip-archive]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal split-ZIP and patched ZIP archive variants reached Assimp ZIP handling but did not cause
minizip to request another disk through the vulnerable callback.

## Policy
Treat `no_crash x parser_reached_no_target` on `assimp-zip-archive` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
Assimp can treat ZIP archives as container inputs for model formats. The vulnerable path is in the
ZIP disk-open callback, which derives a sibling disk filename by scanning backward for a dot in the
current archive filename.

## Harness Contract
The Assimp fuzzer feeds raw bytes to Importer::ReadFileFromMemory with no explicit extension. The
in-memory loader assigns a synthetic filename and then performs signature-based format detection.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
