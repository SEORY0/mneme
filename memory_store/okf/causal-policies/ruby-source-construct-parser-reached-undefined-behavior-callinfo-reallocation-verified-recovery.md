---
type: causal-policy
title: "Ruby Source Construct Parser Reached Undefined Behavior Callinfo Reallocation Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "ruby-source"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-callinfo-reallocation"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "ruby-source", "libfuzzer", "construct", "undefined-behavior-callinfo-reallocation", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached", "ruby-source", "libfuzzer", "undefined-behavior-callinfo-reallocation", "wrong-sink", "parser-reached", "ruby-source", "libfuzzer", "undefined-behavior-callinfo-reallocation", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Ruby Source Construct Parser Reached Undefined Behavior Callinfo Reallocation Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[ruby-source]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached` on `ruby-source`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use plain Ruby source that compiles to string interpolation, so the VM executes OP_STRCAT with a string accumulator and a non-string object. Give that object a to_s method that performs enough nested Ruby calls to grow and reallocate the VM call-info stack, then returns a string. When control returns through mrb_str_concat to the active OP_STRCAT frame, the vulnerable VM continues with stale call-info or instruction state and trips undefined behavior; the fixed build preserves or refreshes the VM state.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[ruby-source]]: The input is raw Ruby source text, not bytecode or a serialized mruby irep. String interpolation is the source-level construct that emits the OP_STRCAT bytecode path. Interpolating an object that is not already a string, symbol, integer, class, or module causes mrb_str_concat to coerce it through to_s, which can execute arbitrary Ruby before concatenation finishes.
- Harness [[libfuzzer]]: The libFuzzer target copies the raw input bytes into a NUL-terminated buffer and passes them directly to mrb_load_string. There is no mode byte, checksum, length prefix, or FuzzedDataProvider layout. Inputs must be valid enough Ruby source to compile and execute under mrb_load_string; parser errors simply return without reaching the VM opcode path.

## Negative Memory
- Do not corrupt the outer `ruby-source` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[ruby-source]] and [[libfuzzer]].
