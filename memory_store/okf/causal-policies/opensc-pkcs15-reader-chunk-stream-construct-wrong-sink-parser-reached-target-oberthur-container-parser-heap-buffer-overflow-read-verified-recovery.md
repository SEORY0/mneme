---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached Target Oberthur Container Parser Heap Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_target_oberthur_container_parser."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_oberthur_container_parser"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "honggfuzz"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-oberthur-container-parser", "opensc-pkcs15-reader-chunk-stream", "honggfuzz", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_target_oberthur_container_parser", "opensc-pkcs15-reader-chunk-stream", "honggfuzz", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached Target Oberthur Container Parser Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_oberthur_container_parser`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[honggfuzz]]

## Failure Shape
Use an Oberthur-recognized ATR, then a length-prefixed APDU response stream. Let early card-manager, serial, application-select, and root-directory gates succeed, but answer the normal PKCS#15 discovery probes with clean not-found status so the synthetic Oberthur emulator starts on the intended chunk. In the Oberthur init path, return valid PIN-directory metadata, acceptable PIN status responses, a transparent token-info file large enough for its parser, then a driver-specific variable-record Containers file whose one returned record is shorter than the fixed container ID/UUID fields the parser reads. End the record sequence with record-not-found so the short synthesized record is parsed.

## Policy
When `wrong_sink x parser_reached_target_oberthur_container_parser` appears for `opensc-pkcs15-reader-chunk-stream` under `honggfuzz`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opensc-pkcs15-reader-chunk-stream]]` format contract and `[[honggfuzz]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `opensc-pkcs15-reader-chunk-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 3 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
