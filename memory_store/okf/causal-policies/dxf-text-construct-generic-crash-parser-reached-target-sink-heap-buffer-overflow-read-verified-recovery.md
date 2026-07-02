---
type: "causal-policy"
title: "DXF Text Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "dxf-text"
harness_convention: "libfuzzer-libredwg-llvmfuzz"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-target-sink", "dxf-text", "libfuzzer-libredwg-llvmfuzz", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_target_sink", "dxf-text", "libfuzzer-libredwg-llvmfuzz", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# DXF Text Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[dxf-text]]
- related harness facts: [[libfuzzer-libredwg-llvmfuzz]]

## Failure Shape
Drive the raw libredwg fuzzer into the DXF text path with a small line-oriented record whose value type causes a direct whitespace skip followed by a nested floating-point whitespace skip. Keep the logical input large enough for the DXF reader gate, end the skipped value at the logical buffer boundary, and use a terminator form that prevents the harness from allocating an extra byte. The second skip begins at the logical end and the vulnerable build reads past the input; the fixed build rejects or bounds-checks that state.

## Policy
When `generic_crash x parser_reached_target_sink` appears for `[[dxf-text]]` under `[[libfuzzer-libredwg-llvmfuzz]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[dxf-text]]` format contract and `[[libfuzzer-libredwg-llvmfuzz]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[dxf-text]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
