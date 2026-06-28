---
type: negative-memory
title: "Generic Crash Local Wrapper Crash Not Reproduced Officially Mruby Source Construct Memory Safety Condition Order Negative Memory"
description: "Round 25 negative memory for generic_crash with verifier signal local_wrapper_crash_not_reproduced_officially."
failure_class: "generic_crash"
verifier_signal: "local_wrapper_crash_not_reproduced_officially"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer-raw-mruby-source"
vuln_class: "memory-safety-condition-order"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-wrapper-crash-not-reproduced-officially", "mruby-source", "libfuzzer-raw-mruby-source", "construct", "negative-memory", "round-25"]
match_keys: ["generic_crash", "local_wrapper_crash_not_reproduced_officially", "mruby-source", "libfuzzer-raw-mruby-source", "memory-safety-condition-order", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Generic Crash Local Wrapper Crash Not Reproduced Officially Mruby Source Construct Memory Safety Condition Order Negative Memory

- key: `generic_crash x local_wrapper_crash_not_reproduced_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer-raw-mruby-source]]

## Failure Shape
Large numeric precision and width variants were tried through raw mruby source. One local run crashed the wrapper, but official submission did not reproduce a vulnerable-build crash, so this was treated as local/off-target behavior rather than a solve.

## Policy
Treat `generic_crash x local_wrapper_crash_not_reproduced_officially` on `mruby-source` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `local_wrapper_crash_not_reproduced_officially` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_wrapper_crash_not_reproduced_officially`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is raw mruby source code. The relevant sink family is floating-point formatting via Ruby formatting calls, where format-string width or precision values flow into the C float formatting helper.

## Harness Contract
The fuzzer copies raw bytes into a NUL-terminated string, opens an mruby interpreter, loads the string as source code, closes the interpreter, and frees the copied source.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 3 attempts.
- Scope: generator repair and basin avoidance only.
