---
type: causal-policy
title: "Yara Rule Text Construct Parser Reached Ubsan Callback Type Mismatch Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_ubsan_callback_type_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_ubsan_callback_type_mismatch"
candidate_family: "construct"
input_format: "yara-rule-text"
harness_convention: "libfuzzer-raw-bytes"
vuln_class: "undefined-behavior-function-type-mismatch"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-ubsan-callback-type-mismatch", "construct", "yara-rule-text", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_ubsan_callback_type_mismatch", "yara-rule-text", "libfuzzer-raw-bytes", "undefined-behavior-function-type-mismatch", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Yara Rule Text Construct Parser Reached Ubsan Callback Type Mismatch Verified Recovery

- key: `wrong_sink x parser_reached_ubsan_callback_type_mismatch`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[yara-rule-text]]
- harnesses: [[libfuzzer-raw-bytes]]

## Failure Shape
The verifier-confirmed candidate preserved the `yara-rule-text` parser envelope under `libfuzzer-raw-bytes` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_ubsan_callback_type_mismatch` on `yara-rule-text` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Any syntactically acceptable, nonempty YARA rule text is enough. The crash is caused by the fuzzer
callback being declared with the wrong data-pointer type for libFuzzer, so reaching the callback
with valid rule text triggers the sanitizer before rule semantics matter.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The input is raw YARA rule source text compiled from a NUL-terminated copy of the fuzzer bytes. A
minimal rule with a true condition is sufficient to satisfy the parser gate.

## Harness Contract
LibFuzzer calls the entrypoint with raw file bytes and a size. The vulnerable entrypoint declaration
uses a character pointer where libFuzzer expects a byte pointer, producing a callback ABI/type
mismatch.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
