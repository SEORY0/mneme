---
type: causal-policy
title: Generic Crash Sink Mismatch Negative Memory
description: Negative memory for generic_crash with verifier signal sink_mismatch.
failure_class: generic_crash
verifier_signal: sink_mismatch
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, sink-mismatch, negative_memory]
match_keys: [generic-crash, sink-mismatch, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Sink Mismatch Negative Memory

- key: `generic_crash x sink_mismatch`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: psd

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Quarantine the crashing basin. Shrink or discard the off-target crash and retarget the described sink; never submit a candidate that also fails on the fixed image.

## Diagnosed Dead Ends
- A trivial probe crashed in the PSD reader at a non-target sink and official comparison rejected it. A minimal grayscale PSD with an alpha-like extra channel caused local instability but the official server classified both builds the same, so the target likely requires a valid layered or merged grayscale PSD shape that reaches alpha merge correction without malformed-file rejection.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
