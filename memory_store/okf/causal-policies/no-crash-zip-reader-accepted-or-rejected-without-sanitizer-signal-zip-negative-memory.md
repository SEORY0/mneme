---
type: causal-policy
title: "No Crash ZIP Reader Accepted Or Rejected Without Sanitizer Signal ZIP Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal zip_reader_accepted_or_rejected_without_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "zip_reader_accepted_or_rejected_without_sanitizer_signal"
candidate_family: "construct"
input_format: "zip"
harness_convention: "libfuzzer"
vuln_class: "signed-offset-underflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "zip-reader-accepted-or-rejected-without-sanitizer-signal", "zip", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "zip-reader-accepted-or-rejected-without-sanitizer-signal", "zip", "libfuzzer", "signed-offset-underflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash ZIP Reader Accepted Or Rejected Without Sanitizer Signal ZIP Negative Memory

- key: `no_crash x zip_reader_accepted_or_rejected_without_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zip]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A constructed archive placed the end-of-central-directory record before the declared central directory while keeping declared central-directory bounds inside the total input size, aiming to make the archive-start calculation go negative.
- Local verification produced no crash, likely because later ZIP consistency checks or unsigned arithmetic behavior avoided an observable sanitizer signal for this minimal archive.

## Policy
Treat `no_crash x zip_reader_accepted_or_rejected_without_sanitizer_signal` on `zip` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `zip_reader_accepted_or_rejected_without_sanitizer_signal`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[zip]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x zip_reader_accepted_or_rejected_without_sanitizer_signal`.
- Candidate family: `construct`.
- Basin summary: A constructed archive placed the end-of-central-directory record before the declared central directory while keeping declared central-directory bounds inside the total input size, aiming to make the archive-start calculation go negative.
