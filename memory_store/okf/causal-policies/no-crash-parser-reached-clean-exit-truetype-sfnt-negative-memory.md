---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Truetype SFNT Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "truetype-sfnt"
harness_convention: "libfuzzer"
vuln_class: "unsigned-integer-overflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "truetype-sfnt", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "parser-reached-clean-exit", "truetype-sfnt", "libfuzzer", "unsigned-integer-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Parser Reached Clean Exit Truetype SFNT Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[truetype-sfnt]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Minimal sfnt directories could satisfy required-table gates and exercise the wrapped table-bound expression, but the resulting slices did not produce a sanitizer-visible access in the local or official target path.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `truetype-sfnt` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[truetype-sfnt]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x parser_reached_clean_exit`.
- Candidate family: `construct`.
- Basin summary: Minimal sfnt directories could satisfy required-table gates and exercise the wrapped table-bound expression, but the resulting slices did not produce a sanitizer-visible access in the local or official target path.
