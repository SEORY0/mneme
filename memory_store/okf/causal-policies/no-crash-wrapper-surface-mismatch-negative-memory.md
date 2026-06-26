---
type: causal-policy
title: Wrapper Surface Mismatch Negative Memory
description: Negative memory for failures where the local harness surface does not match the file shape being generated.
failure_class: no_crash
verifier_signal: wrapper_surface_mismatch
candidate_family: construct
input_format: any
harness_convention: libfuzzer
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, wrapper_surface_mismatch, wrong_harness_envelope, negative_memory]
match_keys: [no_crash, wrapper_surface_mismatch, wrong_harness_envelope, harness_input_shape_mismatch]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When the verifier or diagnosis says the wrapper surface mismatches the generated file shape, stop mutating the payload. First adapt to the harness contract: corpus directory, envelope prefix, length-delimited response stream, or embedded document carrier.

## Procedure
1. Classify whether the harness consumes a raw file, a path argument, a corpus directory, a packet body, or an embedded document.
2. Rebuild the candidate in that surface before changing vulnerability fields.
3. If the target format must be embedded, construct the outer carrier first and keep the inner object minimal.
4. Re-run local verification only after the wrapper shape is changed.
5. Quarantine the old payload-only family unless the wrapper contract becomes observable.

## Negative Memory
- Do not keep expanding a payload that the harness never feeds to the target parser.
- Do not mutate raw embedded assets when the harness requires a PDF, PostScript, APDU, or directory carrier.
- Do not submit wrapper-shape mismatches.

## Evidence Shape
- Support: diagnosed round failures with wrapper, envelope, and harness-shape mismatch signals.
- Scope: generator repair only.
