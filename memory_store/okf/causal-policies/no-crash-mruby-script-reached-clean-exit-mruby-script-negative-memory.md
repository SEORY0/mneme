---
type: causal-policy
title: "No Crash Mruby Script Reached Clean Exit Mruby Script Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal mruby_script_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "mruby_script_reached_clean_exit"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer-mruby-load-string"
vuln_class: "semantic-method-placement"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mruby-script-reached-clean-exit", "mruby-script", "negative-memory", "round-13"]
match_keys: ["no_crash", "mruby_script_reached_clean_exit", "mruby-script", "libfuzzer-mruby-load-string", "semantic-method-placement", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Mruby Script Reached Clean Exit Mruby Script Negative Memory

- key: `no_crash x mruby_script_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer-mruby-load-string]]

## Failure Shape
A direct script invoking Kernel#p executed successfully and printed output, but did not crash. The described issue appears semantic/debugger-related rather than a memory-safety path reachable by simply calling the method under the load-string fuzzer.

## Policy
Treat `no_crash x mruby_script_reached_clean_exit` on `mruby-script` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `mruby_script_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is plain mruby source text. Valid scripts execute through mrb_load_string; method calls such as p, print, method lookup, and Kernel introspection are ordinary Ruby-level operations in this harness.

## Harness Contract
The OSS-Fuzz mruby harness copies the raw bytes into a NUL-terminated code buffer, opens a new mruby state, evaluates the code string, and closes the state. There is no byte-level carving or external file contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
