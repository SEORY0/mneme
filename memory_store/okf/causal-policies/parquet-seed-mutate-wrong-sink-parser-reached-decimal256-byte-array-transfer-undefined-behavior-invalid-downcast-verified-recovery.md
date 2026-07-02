---
type: causal-policy
title: "Parquet Seed Mutate Wrong Sink Parser Reached Decimal256 Byte Array Transfer Undefined Behavior Invalid Downcast Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_decimal256_byte_array_transfer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_decimal256_byte_array_transfer"
candidate_family: "seed_mutate"
input_format: "parquet"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-invalid-downcast"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-decimal256-byte-array-transfer", "parquet", "libfuzzer", "seed-mutate", "undefined-behavior-invalid-downcast", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_decimal256_byte_array_transfer", "parquet", "libfuzzer", "undefined-behavior-invalid-downcast", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Parquet Seed Mutate Wrong Sink Parser Reached Decimal256 Byte Array Transfer Undefined Behavior Invalid Downcast Verified Recovery

- key: `wrong_sink x parser_reached_decimal256_byte_array_transfer`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[parquet]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Start from an in-repository Parquet seed whose physical column is a variable-length byte array annotated as decimal and whose footer, row group, column chunk, and page metadata already read cleanly. Mutate only the decimal precision in the Compact Thrift schema metadata so the same byte-array page data maps to an Arrow Decimal256 logical type. Reading the table reaches the Decimal256 transfer path for byte-array decimal data and triggers the vulnerable Decimal128 downcast, while the fixed build handles or rejects that type relation.

## Policy
When `wrong_sink x parser_reached_decimal256_byte_array_transfer` appears for `parquet` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[parquet]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `parquet` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 1 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
