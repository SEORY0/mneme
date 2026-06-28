---
type: negative-memory
title: "No Crash Rpc Parser Reached No Target Crash P11 Kit Rpc Message Seed Mutate Attribute Array Recursion Memory Corruption Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal rpc_parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "rpc_parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "p11-kit-rpc-message"
harness_convention: "libfuzzer"
vuln_class: "attribute-array-recursion-memory-corruption"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "rpc-parser-reached-no-target-crash", "p11-kit-rpc-message", "libfuzzer", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "rpc_parser_reached_no_target_crash", "p11-kit-rpc-message", "libfuzzer", "attribute-array-recursion-memory-corruption", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Rpc Parser Reached No Target Crash P11 Kit Rpc Message Seed Mutate Attribute Array Recursion Memory Corruption Negative Memory

- key: `no_crash x rpc_parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[p11-kit-rpc-message]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Seed mutations successfully exercised RPC calls carrying array-valued attributes and nested array-valued attributes, but they either parsed cleanly or failed without a sanitizer split. The likely missing condition is a call or nested value shape that forces the second parsing pass to materialize recursively sized data into an allocation sized only for the immediate attribute count.

## Policy
Treat `no_crash x rpc_parser_reached_no_target_crash` on `p11-kit-rpc-message` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `rpc_parser_reached_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `rpc_parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
p11-kit RPC messages begin with a big-endian call identifier, a part count/signature, then typed fields. Attribute arrays encode an attribute count followed by attributes. Each attribute has a type, a validity marker, a declared value length, and a value encoded according to the attribute type. Template attributes are array-valued and can encode nested attributes.

## Harness Contract
The harness feeds raw bytes into a p11_buffer, initializes the mock module, and calls the RPC server handler directly. There is no outer transport framing beyond the RPC message itself; repository seeds under the fuzz corpus are valid starting points.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 18 attempts.
- Scope: generator repair and basin avoidance only.
