---
type: causal-policy
title: "No Crash Named Arg Formatter Executed Clean Fmt Named Argument Fuzzer Buffer Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal named_arg_formatter_executed_clean."
failure_class: "no_crash"
verifier_signal: "named_arg_formatter_executed_clean"
candidate_family: "construct"
input_format: "fmt-named-argument-fuzzer-buffer"
harness_convention: "honggfuzz-raw-bytes"
vuln_class: "numeric-format-carry-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "named-arg-formatter-executed-clean", "fmt-named-argument-fuzzer-buffer", "negative-memory", "round-7"]
match_keys: ["no_crash", "named_arg_formatter_executed_clean", "fmt-named-argument-fuzzer-buffer", "honggfuzz-raw-bytes", "numeric-format-carry-error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Named Arg Formatter Executed Clean Fmt Named Argument Fuzzer Buffer Negative Memory

- key: `no_crash x named_arg_formatter_executed_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fmt-named-argument-fuzzer-buffer]]
- related harness facts: [[honggfuzz-raw-bytes]]

## Failure Shape
The named-argument harness layout was satisfied and the formatter executed, but tested boundary
floating-point values and precision/specifier combinations did not drive the fallback-format carry
path into a sanitizer-visible failure. The missing relation is likely a narrower decimal
representation or format spec that forces the vulnerable carry adjustment instead of the normal
formatting path.

## Policy
Treat `no_crash x named_arg_formatter_executed_clean` on `fmt-named-argument-fuzzer-buffer` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `named_arg_formatter_executed_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The named-argument fuzzer uses an initial control byte for argument type and argument-name length,
then a fixed-size value slot, then the argument name, with the remaining bytes interpreted as the
format string. The format string must reference the selected named argument to exercise formatting.

## Harness Contract
The honggfuzz wrapper invokes the named-argument fmt fuzzer on raw file bytes. Invalid format
strings and many formatting exceptions are handled by the harness as clean exits rather than
crashes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
