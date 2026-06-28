---
type: causal-policy
title: "No Crash Fuzzgen Clean Exit Or Rejected Input Libfuzzer Arbitrary Cranelift Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal fuzzgen_clean_exit_or_rejected_input."
failure_class: "no_crash"
verifier_signal: "fuzzgen_clean_exit_or_rejected_input"
candidate_family: "construct"
input_format: "libfuzzer-arbitrary-cranelift"
harness_convention: "libfuzzer"
vuln_class: "unsupported-codegen-operation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "fuzzgen-clean-exit-or-rejected-input", "libfuzzer-arbitrary-cranelift", "negative-memory", "round-15"]
match_keys: ["no_crash", "fuzzgen_clean_exit_or_rejected_input", "libfuzzer-arbitrary-cranelift", "libfuzzer", "unsupported-codegen-operation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Fuzzgen Clean Exit Or Rejected Input Libfuzzer Arbitrary Cranelift Negative Memory

- key: `no_crash x fuzzgen_clean_exit_or_rejected_input`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libfuzzer-arbitrary-cranelift]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- High-entropy, all-zero, all-one, incrementing, and textual arbitrary byte streams did not cause the
  Cranelift generator to emit the needed 128-bit atomic operation combination. The target is not a
  CLIF text parser; reaching the bug requires steering the Arbitrary-derived generator toward an ISA,
  memory flags, value types, and atomic opcode selection that together produce unsupported codegen.

## Policy
Treat `no_crash x fuzzgen_clean_exit_or_rejected_input` on `libfuzzer-arbitrary-cranelift` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The Cranelift fuzz targets deserialize structured generator choices from the raw libFuzzer byte
  stream using the Rust Arbitrary API. The cranelift-fuzzgen target builds functions, inputs, ISA
  options, and run/compare settings from those choices rather than reading textual CLIF or WebAssembly
  modules.

## Harness Contract
- The packaged run command selected the cranelift-fuzzgen libFuzzer binary. It passes the raw input to
  Arbitrary-derived test-case generation, then compiles/interprets generated Cranelift functions.
  There is no stable byte offset contract comparable to a file format header.

## Negative Memory
- Do not resubmit variants that only reproduce `fuzzgen_clean_exit_or_rejected_input`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
