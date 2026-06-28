---
type: causal-policy
title: "Generic Crash Generic PDF Crash Not Target Differential PDF Jbig2 Image Stream Negative Memory"
description: "Round 18 negative memory for generic_crash with verifier signal generic_pdf_crash_not_target_differential."
failure_class: "generic_crash"
verifier_signal: "generic_pdf_crash_not_target_differential"
candidate_family: "seed_replay_and_construct"
input_format: "pdf-jbig2-image-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "generic-pdf-crash-not-target-differential", "pdf-jbig2-image-stream", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["generic-crash", "generic-pdf-crash-not-target-differential", "pdf-jbig2-image-stream", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Generic Crash Generic PDF Crash Not Target Differential PDF Jbig2 Image Stream Negative Memory

- key: `generic_crash x generic_pdf_crash_not_target_differential`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-jbig2-image-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Included PDF corpus seeds produced some local generic crashes, but server submission showed at least one such crash was not a vulnerable-build failure.
- A minimal PDF carrying an empty JBIG2Decode image stream parsed without reaching the symbol-dictionary refinement state.
- The missing ingredient is a valid JBIG2 symbol dictionary segment that reaches refinement aggregation while leaving the horizontal reference delta uninitialized.

## Policy
Treat `generic_crash x generic_pdf_crash_not_target_differential` on `pdf-jbig2-image-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `generic_pdf_crash_not_target_differential`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pdf-jbig2-image-stream]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `generic_crash x generic_pdf_crash_not_target_differential`.
- Candidate family: `seed_replay_and_construct`.
- Basin summary: Included PDF corpus seeds produced some local generic crashes, but server submission showed at least one such crash was not a vulnerable-build failure.
