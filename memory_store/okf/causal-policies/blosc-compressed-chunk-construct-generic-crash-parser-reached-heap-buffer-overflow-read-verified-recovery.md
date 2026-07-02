---
type: causal-policy
title: "Blosc Compressed Chunk Construct Generic Crash Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "blosc-compressed-chunk"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "blosc-compressed-chunk", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached", "blosc-compressed-chunk", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Blosc Compressed Chunk Construct Generic Crash Parser Reached Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[blosc-compressed-chunk]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Satisfy the Blosc chunk header gates, keep the declared compressed size equal to the file size, use a single block in dont-split mode, and choose the Lizard codec path. Inside the codec payload, select the LIZv1 variable-literal decoder with raw substreams, then provide a token that asks for an extended literal length while the literal stream lacks the continuation data needed by that encoding. The vulnerable build reads past the tiny literal stream while decoding the variable length; the fixed build rejects the truncated extended-length form.

## Policy
When `generic_crash x parser_reached` appears for `blosc-compressed-chunk` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[blosc-compressed-chunk]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `blosc-compressed-chunk` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 14 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
