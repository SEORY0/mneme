---
type: causal-policy
title: "Cram Construct Generic Crash Parser Reached Heap Buffer Overflow Write Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "cram"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "cram", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached", "cram", "libfuzzer", "heap-buffer-overflow-write", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Cram Construct Generic Crash Parser Reached Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[cram]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a syntactically valid CRAM stream that satisfies the file-definition, SAM-header-container, container-header, block-header, and CRC gates. Use CRAM v4-style varints so the compression header is parsed through the experimental codec table, then place an XPACK record-encoding descriptor on a normal integer data series. Keep the nested subcodec descriptor well-formed, but make the XPACK reverse-map cardinality exceed the decoder's fixed map storage while each listed map symbol remains individually valid. This triggers the overflow during compression-header codec initialization before slice/reference decoding is needed.

## Policy
When `generic_crash x parser_reached` appears for `cram` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[cram]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `cram` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 5 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
