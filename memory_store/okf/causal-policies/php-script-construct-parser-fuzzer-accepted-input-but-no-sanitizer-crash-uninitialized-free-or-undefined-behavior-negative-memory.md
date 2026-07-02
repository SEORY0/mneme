---
type: negative-memory
title: "PHP Script Construct Parser Fuzzer Accepted Input But No Sanitizer Crash Uninitialized Free Or Undefined Behavior Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal parser_fuzzer_accepted_input_but_no_sanitizer_crash."
failure_class: "no_crash"
verifier_signal: "parser_fuzzer_accepted_input_but_no_sanitizer_crash"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "honggfuzz-libfuzzer-php-parser-raw-source"
vuln_class: "uninitialized-free-or-undefined-behavior"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-fuzzer-accepted-input-but-no-sanitizer-crash", "php-script", "honggfuzz-libfuzzer-php-parser-raw-source", "construct", "uninitialized-free-or-undefined-behavior", "negative-memory", "round-29"]
match_keys: ["no_crash", "parser_fuzzer_accepted_input_but_no_sanitizer_crash", "php-script", "honggfuzz-libfuzzer-php-parser-raw-source", "uninitialized-free-or-undefined-behavior", "no-crash", "parser-fuzzer-accepted-input-but-no-sanitizer-crash", "php-script", "honggfuzz-libfuzzer-php-parser-raw-source", "uninitialized-free-or-undefined-behavior", "negative_memory", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# PHP Script Construct Parser Fuzzer Accepted Input But No Sanitizer Crash Uninitialized Free Or Undefined Behavior Negative Memory

- key: `no_crash x parser_fuzzer_accepted_input_but_no_sanitizer_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-script]]
- related harness facts: [[honggfuzz-libfuzzer-php-parser-raw-source]]

## Failure Shape
Raw PHP source candidates reached the parser fuzzer but did not trigger the described attribute cleanup bug. Distinct attempts covered the built-in attribute marker on classes, methods, constants, properties, and parameters; inheritance-scoped constant expressions; compile-time constant-expression rejection; grouped declaration rejection; unpack and non-constant attribute arguments. The official differential also reported a clean vulnerable run for the strongest candidate, so the missing gate is likely a narrower attribute compilation state than these surfaces exposed.

## Policy
Treat `no_crash x parser_fuzzer_accepted_input_but_no_sanitizer_crash` on `php-script` for `uninitialized-free-or-undefined-behavior` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_fuzzer_accepted_input_but_no_sanitizer_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_fuzzer_accepted_input_but_no_sanitizer_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is plain PHP source text. This PHP tree uses the older double-angle attribute syntax before declarations. Attribute arguments are parsed as constant expressions and are stored on class, function, method, property, class-constant, or parameter metadata during compilation. The built-in marker for declaring attribute classes is an internal class named PhpAttribute.

## Harness Contract
The wrapper runs the PHP parser fuzzer on the raw file contents as a PHP file body. There is no leading mode byte, checksum, archive wrapper, or FuzzedDataProvider split. The fuzzer copies the raw bytes into a NUL-terminated buffer, compiles them, destroys any resulting op_array, and does not execute script code.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 16 attempts.
- Scope: generator repair and basin avoidance only.
