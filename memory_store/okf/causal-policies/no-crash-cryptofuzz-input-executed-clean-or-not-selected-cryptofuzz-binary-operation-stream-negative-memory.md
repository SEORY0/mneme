---
type: causal-policy
title: "No Crash Cryptofuzz Input Executed Clean Or Not Selected Cryptofuzz Binary Operation Stream Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal cryptofuzz_input_executed_clean_or_not_selected."
failure_class: "no_crash"
verifier_signal: "cryptofuzz_input_executed_clean_or_not_selected"
candidate_family: "construct"
input_format: "cryptofuzz-binary-operation-stream"
harness_convention: "libfuzzer-msan"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "cryptofuzz-input-executed-clean-or-not-selected", "cryptofuzz-binary-operation-stream", "negative-memory", "round-9"]
match_keys: ["no_crash", "cryptofuzz_input_executed_clean_or_not_selected", "cryptofuzz-binary-operation-stream", "libfuzzer-msan", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Cryptofuzz Input Executed Clean Or Not Selected Cryptofuzz Binary Operation Stream Negative Memory

- key: `no_crash x cryptofuzz_input_executed_clean_or_not_selected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cryptofuzz-binary-operation-stream]]
- related harness facts: [[libfuzzer-msan]]

## Failure Shape
- Rough binary operation streams, JSON-like ECC descriptions, and long zero inputs did not select
  the libecc operation state that calls fp_uninit on an uninitialized field.
- The missing gate is the exact cryptofuzz binary operation encoding and module/curve combination
  for the libecc path.

## Policy
Treat `no_crash x cryptofuzz_input_executed_clean_or_not_selected` on `cryptofuzz-binary-operation-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- Cryptofuzz inputs are not plain JSON for this target; the executable uses cryptofuzzs binary
  datasource and custom mutator to select an operation, module, curve, and operation-specific
  parameters.
- ECC operations include private-to-public, validation, signing, verification, ECDH, and point
  arithmetic families.

## Harness Contract
- The libFuzzer target is built with MemorySanitizer and a custom mutator.
- The wrapper invokes cryptofuzz-libecc directly on the raw input; operation dispatch is internal to
  the cryptofuzz datasource rather than a simple leading text command.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `cryptofuzz_input_executed_clean_or_not_selected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
