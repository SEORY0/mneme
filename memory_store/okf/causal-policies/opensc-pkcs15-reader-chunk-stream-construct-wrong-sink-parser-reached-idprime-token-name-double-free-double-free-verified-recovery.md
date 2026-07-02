---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached Idprime Token Name Double Free Double Free Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_idprime_token_name_double_free."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_idprime_token_name_double_free"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-idprime-token-name-double-free", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "double-free", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_idprime_token_name_double_free", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "double-free", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached Idprime Token Name Double Free Double Free Verified Recovery

- key: `wrong_sink x parser_reached_idprime_token_name_double_free`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a virtual OpenSC reader transcript that first binds an IDPrime card, returns an index containing a token-info object but no certificate objects, and makes the normal PKCS#15 application probes fail so the synthetic IDPrime emulator is selected. In the token-name path, return a valid small header that causes allocation, then return a successful empty value read. The vulnerable function frees the output pointer but returns success, so the caller installs a dangling token label that is freed again during card cleanup.

## Policy
When `wrong_sink x parser_reached_idprime_token_name_double_free` appears for `opensc-pkcs15-reader-chunk-stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opensc-pkcs15-reader-chunk-stream]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
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
- Support: server-verified round 37 solve after 2 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
