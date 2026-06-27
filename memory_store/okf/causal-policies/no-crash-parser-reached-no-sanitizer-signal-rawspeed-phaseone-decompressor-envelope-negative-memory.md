---
type: causal-policy
title: "No Crash Parser Reached No Sanitizer Signal Rawspeed Phaseone Decompressor Envelope Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal parser_reached_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_sanitizer_signal"
candidate_family: "construct"
input_format: "rawspeed-phaseone-decompressor-envelope"
harness_convention: "libfuzzer"
vuln_class: "missing-row-order-validation"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-no-sanitizer-signal", "rawspeed-phaseone-decompressor-envelope", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "parser-reached-no-sanitizer-signal", "rawspeed-phaseone-decompressor-envelope", "libfuzzer", "missing-row-order-validation", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Parser Reached No Sanitizer Signal Rawspeed Phaseone Decompressor Envelope Negative Memory

- key: `no_crash x parser_reached_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-phaseone-decompressor-envelope]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A constructed PhaseOne strip envelope satisfied the basic image and strip-count gates and exercised duplicate or missing per-row strip numbering, but local verification did not report an initialized-memory or bounds violation.
- The likely gap is that the malformed row map alone did not force an observable poisoned read in this harness configuration.

## Policy
Treat `no_crash x parser_reached_no_sanitizer_signal` on `rawspeed-phaseone-decompressor-envelope` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_sanitizer_signal`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[rawspeed-phaseone-decompressor-envelope]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x parser_reached_no_sanitizer_signal`.
- Candidate family: `construct`.
- Basin summary: A constructed PhaseOne strip envelope satisfied the basic image and strip-count gates and exercised duplicate or missing per-row strip numbering, but local verification did not report an initialized-memory or bounds violation.
