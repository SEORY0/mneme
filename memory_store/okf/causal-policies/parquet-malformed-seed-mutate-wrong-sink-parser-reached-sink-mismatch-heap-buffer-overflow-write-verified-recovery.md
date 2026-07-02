---
type: causal-policy
title: "Parquet Malformed Seed Mutate Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Write Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "malformed_seed_mutate"
input_format: "parquet"
harness_convention: "afl/libfuzzer-compatible-parquet-arrow-raw-file"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "parquet", "afl-libfuzzer-compatible-parquet-arrow-raw-file", "malformed-seed-mutate", "heap-buffer-overflow-write", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch", "parquet", "afl/libfuzzer-compatible-parquet-arrow-raw-file", "heap-buffer-overflow-write", "wrong-sink", "parser-reached-sink-mismatch", "afl-libfuzzer-compatible-parquet-arrow-raw-file", "verified_recovery", "malformed_seed_mutate", "malformed-seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Parquet Malformed Seed Mutate Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[parquet]]
- related harness facts: [[afl-libfuzzer-compatible-parquet-arrow-raw-file]]

## Failure Shape
Use a raw Parquet envelope that passes footer and page parsing, with a nested optional-struct/list schema. The triggering relation is between the declared row-bound used to size a struct validity bitmap and the repetition/definition level stream for a repeated child: the bitmap writer reaches the declared bound on a byte boundary while additional level entries remain, so finalization writes past the allocated validity buffer. Non-semantic padding can vary as long as the footer, nested schema, row-group metadata, and malformed level-stream relation are preserved.

## Policy
When `wrong_sink x parser_reached_sink_mismatch` appears for `parquet` under `afl/libfuzzer-compatible-parquet-arrow-raw-file`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[parquet]]` format contract and `[[afl-libfuzzer-compatible-parquet-arrow-raw-file]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `parquet` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 8 attempts.
- Candidate family: malformed_seed_mutate.
- Scope: generator repair and retargeting only.
