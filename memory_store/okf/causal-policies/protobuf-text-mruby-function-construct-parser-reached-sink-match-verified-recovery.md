---
type: causal-policy
title: "Protobuf Text Mruby Function Construct Parser Reached Sink Match Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached_sink_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "protobuf-text-mruby-function"
harness_convention: "libfuzzer-libprotobuf-mutator"
vuln_class: "integer-overflow-or-buffer-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-sink-match", "construct", "protobuf-text-mruby-function", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached_sink_match", "protobuf-text-mruby-function", "libfuzzer-libprotobuf-mutator", "integer-overflow-or-buffer-overflow", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Protobuf Text Mruby Function Construct Parser Reached Sink Match Verified Recovery

- key: `generic_crash x parser_reached_sink_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[protobuf-text-mruby-function]]
- harnesses: [[libfuzzer-libprotobuf-mutator]]

## Failure Shape
The verifier-confirmed candidate preserved the `protobuf-text-mruby-function` parser envelope under `libfuzzer-libprotobuf-mutator` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached_sink_match` on `protobuf-text-mruby-function` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use the protobuf text format expected by the mruby proto fuzzer, not raw Ruby source. Build a
function AST that converts to assignments and arithmetic; repeated multiplication on small constants
creates a bigint receiver, then a generated right-shift expression with a boundary-width shift
drives the bigint internal length calculation into the vulnerable path.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The fuzzer input is protobuf text describing a Ruby function AST. The converter supports a limited
expression language; assignments preserve intermediate values and arithmetic operations are emitted
as Ruby code by the harness.

## Harness Contract
The active binary parses protobuf text and converts it to Ruby before executing mruby. Raw Ruby text
is treated as bad input for this harness, so the PoC must satisfy the proto schema first.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
