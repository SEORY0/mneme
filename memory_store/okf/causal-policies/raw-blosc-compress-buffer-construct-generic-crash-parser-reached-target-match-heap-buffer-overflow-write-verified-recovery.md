---
type: causal-policy
title: "Raw Blosc Compress Buffer Construct Generic Crash Parser Reached Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "raw-blosc-compress-buffer"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "raw-blosc-compress-buffer", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_match", "raw-blosc-compress-buffer", "libfuzzer", "heap-buffer-overflow-write", "generic-crash", "parser-reached-target-match", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Raw Blosc Compress Buffer Construct Generic Crash Parser Reached Target Match Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[raw-blosc-compress-buffer]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use the raw compression harness controls to select a real compression path with no transform filter, an available fast compressor, and the harness-controlled small block size. Make the first full block intentionally uncompressible enough that the compressor stores it as a raw copied block while still fitting exactly within the caller's destination budget after metadata. Then make the following short block a repeated run. The vulnerable run encoder writes that block's compressed-size token before checking that enough destination space remains; the fixed build rejects the boundary before the token write.

## Policy
When `generic_crash x parser_reached_target_match` appears for `raw-blosc-compress-buffer` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[raw-blosc-compress-buffer]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `raw-blosc-compress-buffer` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 2 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
