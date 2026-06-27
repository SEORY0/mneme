---
type: causal-policy
title: "No Crash Script Executed Clean Exit Mruby Script Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal script_executed_clean_exit."
failure_class: "no_crash"
verifier_signal: "script_executed_clean_exit"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read-or-unbounded-allocation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "script-executed-clean-exit", "mruby-script", "negative-memory", "round-12"]
match_keys: ["no_crash", "script_executed_clean_exit", "mruby-script", "libfuzzer", "out-of-bounds-read-or-unbounded-allocation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Script Executed Clean Exit Mruby Script Negative Memory

- key: `no_crash x script_executed_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Scripts using String#unpack with b/B directives and counts larger than the source bit length executed cleanly, including very large counts. The tested forms did not produce a sanitizer-visible overread or allocation failure in the built mruby fuzzer.

## Policy
Treat `no_crash x script_executed_clean_exit` on `mruby-script` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The payload is raw mruby source text. The relevant pack template directives are b and B, where an optional count controls how many bit characters are produced; a star count means use the available source bits.

## Harness Contract
The fuzzer copies the entire input to a NUL-terminated buffer, opens an mruby state, calls mrb_load_string on the buffer, closes the state, and frees the copy. There is no length prefix, selector, or file container.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `script_executed_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
