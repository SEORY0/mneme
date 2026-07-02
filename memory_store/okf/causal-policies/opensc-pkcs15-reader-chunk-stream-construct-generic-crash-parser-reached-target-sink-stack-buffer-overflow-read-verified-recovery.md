---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct Generic Crash Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached_target_sink", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "stack-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Opensc Pkcs15 Reader Chunk Stream Construct Generic Crash Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use the OpenSC virtual reader transcript format with an IAS/ECC-matching ATR. Feed repeated successful file-selection responses so one lands on the IAS/ECC FCI parser. The FCI must remain ISO-parseable while placing an empty contact ACL TLV at the response-buffer boundary; the vulnerable parser reads the first ACL byte without checking that the ACL value is nonempty, while the fixed build rejects the empty ACL cleanly.

## Policy
When `generic_crash x parser_reached_target_sink` appears for `opensc-pkcs15-reader-chunk-stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

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
