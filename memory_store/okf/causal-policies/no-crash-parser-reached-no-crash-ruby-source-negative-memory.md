---
type: causal-policy
title: "No Crash Parser Reached No Crash Ruby Source Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_no_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_crash"
candidate_family: "construct"
input_format: "ruby-source"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-crash", "ruby-source", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_no_crash", "ruby-source", "libfuzzer", "integer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached No Crash Ruby Source Negative Memory

- key: `no_crash x parser_reached_no_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ruby-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Ordinary Ruby source with many arguments, block calls, nested yields, dynamic methods, and very high local-register pressure did not make the VM store an overflowing accumulator in the call-info frame. The missing gate is likely a specific bytecode shape emitted by the compiler, not just large source-level arity or many locals.

## Policy
Treat `no_crash x parser_reached_no_crash` on `ruby-source` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The accepted input is Ruby source text compiled by mruby before execution. Calls, block calls, splats, and local variables compile into VM instructions whose register and accumulator fields control call-info state.

## Harness Contract
The mruby fuzzer copies the raw input into a NUL-terminated string and passes it to the mruby source loader. It does not accept precompiled bytecode in this harness path.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
