---
type: causal-policy
title: "No Crash Archive Parser Reached No Target Crash Alpha ECOFF Archive Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal archive_parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "archive_parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "alpha-ecoff-archive"
harness_convention: "libfuzzer-bfd-archive"
vuln_class: "uninitialized-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "archive-parser-reached-no-target-crash", "alpha-ecoff-archive", "libfuzzer-bfd-archive", "negative-memory", "round-18"]
match_keys: ["no-crash", "archive-parser-reached-no-target-crash", "alpha-ecoff-archive", "libfuzzer-bfd-archive", "uninitialized-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Archive Parser Reached No Target Crash Alpha ECOFF Archive Negative Memory

- key: `no_crash x archive_parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[alpha-ecoff-archive]]
- related harness facts: [[libfuzzer-bfd-archive]]

## Failure Shape
- A constructed archive member reached ordinary BFD archive handling but did not force the Alpha ECOFF compressed-member accessor to consume a short compressed-size/read sequence in a sanitizer-visible way.

## Policy
Treat `no_crash x archive_parser_reached_no_target_crash` on `alpha-ecoff-archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `archive_parser_reached_no_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[alpha-ecoff-archive]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-bfd-archive]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x archive_parser_reached_no_target_crash`.
- Candidate family: `construct`.
- Basin summary: A constructed archive member reached ordinary BFD archive handling but did not force the Alpha ECOFF compressed-member accessor to consume a short compressed-size/read sequence in a sanitizer-visible way.
