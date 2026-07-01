---
type: causal-policy
title: "Sdts Tar Iso8211 Seed Mutate Wrong Sink Parser Reached Sdts Iref Extract String Negative Size Memcpy Negative Size Param Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_sdts_iref_extract_string_negative_size."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sdts_iref_extract_string_negative_size"
candidate_family: "seed_mutate"
input_format: "sdts-tar-iso8211"
harness_convention: "libfuzzer"
vuln_class: "memcpy-negative-size-param"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sdts-iref-extract-string-negative-size", "sdts-tar-iso8211", "libfuzzer", "seed-mutate", "memcpy-negative-size-param", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_sdts_iref_extract_string_negative_size", "sdts-tar-iso8211", "libfuzzer", "memcpy-negative-size-param", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Sdts Tar Iso8211 Seed Mutate Wrong Sink Parser Reached Sdts Iref Extract String Negative Size Memcpy Negative Size Param Verified Recovery

- key: `wrong_sink x parser_reached_sdts_iref_extract_string_negative_size`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[sdts-tar-iso8211]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use a real SDTS transfer as a tar archive so the specialized OGR SDTS fuzzer reaches the catalog and feature layers. Preserve the catalog and transfer modules, then move the spatial-reference metadata out of the optimized fixed-width coordinate path. In a point-feature spatial-address field definition, make the first coordinate a variable numeric subfield followed by a fixed textual numeric subfield, and make one field instance declare data that ends immediately after the first coordinate bytes without the usual terminator. The first extraction consumes one byte past the declared field payload, so the second extraction receives a negative remaining length and reaches the vulnerable memcpy in ISO8211 string extraction. All unrelated transfer structure remains valid so the fixed build rejects the malformed invariant cleanly.

## Policy
When `wrong_sink x parser_reached_sdts_iref_extract_string_negative_size` appears for `sdts-tar-iso8211` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[sdts-tar-iso8211]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `sdts-tar-iso8211` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 6 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
