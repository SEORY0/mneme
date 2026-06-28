---
type: causal-policy
title: "No Crash Proto Target Reached No Target Crash Protobuf Text To Mruby Source Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal proto_target_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "proto_target_reached_no_target_crash"
candidate_family: "construct"
input_format: "protobuf-text-to-mruby-source"
harness_convention: "libfuzzer-libprotobuf-mutator"
vuln_class: "stack-use-after-realloc"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "proto-target-reached-no-target-crash", "protobuf-text-to-mruby-source", "negative-memory", "round-13"]
match_keys: ["no_crash", "proto_target_reached_no_target_crash", "protobuf-text-to-mruby-source", "libfuzzer-libprotobuf-mutator", "stack-use-after-realloc", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Proto Target Reached No Target Crash Protobuf Text To Mruby Source Negative Memory

- key: `no_crash x proto_target_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[protobuf-text-to-mruby-source]]
- related harness facts: [[libfuzzer-libprotobuf-mutator]]

## Failure Shape
Raw Ruby source snippets were rejected by the selected protobuf target before conversion. Text-format Function messages that generated high local pressure, nested begin blocks, branch-heavy code, expression temporaries, and repeated builtin method calls either compiled and executed cleanly or hit ordinary compiler limits. The missing gate is likely a generated Ruby shape that causes a Proc or VM call frame to extend the stack while a register pointer remains live; the available converter grammar did not expose that shape in the tested families.

## Policy
Treat `no_crash x proto_target_reached_no_target_crash` on `protobuf-text-to-mruby-source` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `proto_target_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The accepted input for the selected target is a text-format protobuf Function. The converter emits a fixed no-argument Ruby method, initializes a first local, wraps statement sequences in begin expressions, and can generate assignments, if/else, ternary expressions, nested statement sequences, array builtin calls, math/time/object calls, constants, variable references, and binary expressions.

## Harness Contract
The build contains a raw mruby string harness and a libprotobuf-mutator harness. The verifier selected the protobuf harness, which parses the input as a Function message, converts it to Ruby source, then passes the generated source to mrb_load_string. Arbitrary Ruby source is not accepted on this target path.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x proto_target_reached_no_target_crash`
- related format facts: [[protobuf-text-to-mruby-source]]
- related harness facts: [[libfuzzer-libprotobuf-mutator]]

### Failure Shape Delta
Raw Ruby source snippets were rejected by the selected protobuf target before conversion. Text-format Function messages that generated high local pressure, nested begin blocks, branch-heavy code, expression temporaries, and repeated builtin method calls either compiled and executed cleanly or hit ordinary compiler limits. The missing gate is likely a generated Ruby shape that causes a Proc or VM call frame to extend the stack while a register pointer remains live; the available converter grammar did not expose that shape in the tested families.

### Format Contract Delta
The accepted input for the selected target is a text-format protobuf Function. The converter emits a fixed no-argument Ruby method, initializes a first local, wraps statement sequences in begin expressions, and can generate assignments, if/else, ternary expressions, nested statement sequences, array builtin calls, math/time/object calls, constants, variable references, and binary expressions.

### Harness Contract Delta
The build contains a raw mruby string harness and a libprotobuf-mutator harness. The verifier selected the protobuf harness, which parses the input as a Function message, converts it to Ruby source, then passes the generated source to mrb_load_string. Arbitrary Ruby source is not accepted on this target path.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
