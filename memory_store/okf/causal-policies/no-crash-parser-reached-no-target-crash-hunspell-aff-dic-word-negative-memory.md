---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Hunspell Aff Dic Word Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "hunspell-aff-dic-word"
harness_convention: "libfuzzer"
vuln_class: "state-restoration-length-bug"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "hunspell-aff-dic-word", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["no-crash", "parser-reached-no-target-crash", "hunspell-aff-dic-word", "libfuzzer", "state-restoration-length-bug", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Parser Reached No Target Crash Hunspell Aff Dic Word Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[hunspell-aff-dic-word]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Seed-mutated compound-pattern dictionaries and words executed cleanly.
- The attempted inputs reached Hunspell but did not create the exact simplified compound-pattern backtracking state where the restored word/index and length diverge.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `hunspell-aff-dic-word` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[hunspell-aff-dic-word]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
