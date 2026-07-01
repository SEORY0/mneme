---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "honggfuzz-libfuzzer-persistent"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "opensc-pkcs15-reader-chunk-stream", "honggfuzz-libfuzzer-persistent", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_sink", "opensc-pkcs15-reader-chunk-stream", "honggfuzz-libfuzzer-persistent", "heap-buffer-overflow-read", "generic-crash", "parser-reached-target-sink", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Opensc Pkcs15 Reader Chunk Stream Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[honggfuzz-libfuzzer-persistent]]

## Failure Shape
Reachability required a smart-card response transcript rather than a standalone ASN.1 blob: choose the target card via the initial connection data, answer the current-directory probe with a response the driver ignores, then answer the file-selection APDU with FCI/FCP data carrying security attributes. The triggering record satisfies the access-mode prefix and condition kind gates but gives the condition expression no payload, so the parser reads the condition reference past the end of the allocated security-attribute buffer.

## Policy
When `generic_crash x parser_reached_target_sink` appears for `opensc-pkcs15-reader-chunk-stream` under `honggfuzz-libfuzzer-persistent`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opensc-pkcs15-reader-chunk-stream]]` format contract and `[[honggfuzz-libfuzzer-persistent]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `opensc-pkcs15-reader-chunk-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 9 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
