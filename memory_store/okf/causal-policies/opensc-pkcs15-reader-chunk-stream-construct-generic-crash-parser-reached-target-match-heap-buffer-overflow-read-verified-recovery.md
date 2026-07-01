---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct Generic Crash Parser Reached Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_match", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "heap-buffer-overflow-read", "generic-crash", "parser-reached-target-match", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Opensc Pkcs15 Reader Chunk Stream Construct Generic Crash Parser Reached Target Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Drive the OpenSC PKCS#15 reader with a chunked synthetic smart-card transcript: first satisfy ITACNS card recognition, let unrelated probing fail cleanly until the built-in ITACNS emulator runs, then provide successful serial-file and personal-data-file responses. The personal-data file must have a coherent outer file-size response, but its own ASCII-hex TLV-size header should claim a larger inner region than the bytes actually returned after one complete small field. The vulnerable parser trusts that inner declared size and reads the next field length past the allocated data object; the fixed build rejects the declared-size mismatch.

## Policy
When `generic_crash x parser_reached_target_match` appears for `opensc-pkcs15-reader-chunk-stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opensc-pkcs15-reader-chunk-stream]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
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
- Support: 1 server-verified round 36 solve after 6 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
