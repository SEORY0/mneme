---
type: causal-policy
title: "Wavefront Obj With Mtl Construct Generic Crash Parser Reached Target Getfloatvalue Null Dereference Write Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_getFloatValue."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_getFloatValue"
candidate_family: "construct"
input_format: "wavefront-obj-with-mtl"
harness_convention: "libfuzzer-assimp-fuzzer"
vuln_class: "null-dereference-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-getfloatvalue", "wavefront-obj-with-mtl", "libfuzzer-assimp-fuzzer", "construct", "null-dereference-write", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_getFloatValue", "wavefront-obj-with-mtl", "libfuzzer-assimp-fuzzer", "null-dereference-write", "generic-crash", "parser-reached-target-getfloatvalue", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Wavefront Obj With Mtl Construct Generic Crash Parser Reached Target Getfloatvalue Null Dereference Write Verified Recovery

- key: `generic_crash x parser_reached_target_getFloatValue`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[wavefront-obj-with-mtl]]
- related harness facts: [[libfuzzer-assimp-fuzzer]]

## Failure Shape
Make the raw in-memory model recognizable as Wavefront OBJ, then use an OBJ material-library declaration that resolves through Assimp's memory IO back to the same submitted buffer. In the material-library pass, place a scalar material field before any material record has established the current material. The vulnerable importer writes the parsed scalar through the missing current-material pointer, while the fixed build rejects or guards that ordering.

## Policy
When `generic_crash x parser_reached_target_getFloatValue` appears for `wavefront-obj-with-mtl` under `libfuzzer-assimp-fuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[wavefront-obj-with-mtl]]` format contract and `[[libfuzzer-assimp-fuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `wavefront-obj-with-mtl` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 1 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
