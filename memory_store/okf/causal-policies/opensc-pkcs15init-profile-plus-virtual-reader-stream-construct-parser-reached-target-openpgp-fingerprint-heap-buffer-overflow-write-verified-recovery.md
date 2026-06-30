---
type: causal-policy
title: "Opensc Pkcs15Init Profile Plus Virtual Reader Stream Construct Parser Reached Target Openpgp Fingerprint Heap Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for opensc-pkcs15init-profile-plus-virtual-reader-stream when generic_crash pairs with parser_reached_target_heap_buffer_overflow_write."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_heap_buffer_overflow_write"
candidate_family: "construct"
input_format: "opensc-pkcs15init-profile-plus-virtual-reader-stream"
harness_convention: "libfuzzer-opensc-pkcs15init"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-heap-buffer-overflow-write", "opensc-pkcs15init-profile-plus-virtual-reader-stream", "libfuzzer-opensc-pkcs15init", "construct", "verified-recovery", "round-31"]
match_keys: ["generic-crash", "parser-reached-target-heap-buffer-overflow-write", "opensc-pkcs15init-profile-plus-virtual-reader-stream", "libfuzzer-opensc-pkcs15init", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 31
---
# Opensc Pkcs15Init Profile Plus Virtual Reader Stream Construct Parser Reached Target Openpgp Fingerprint Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_heap_buffer_overflow_write`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opensc-pkcs15init-profile-plus-virtual-reader-stream]]
- related harness facts: [[libfuzzer-opensc-pkcs15init]]

## Policy
When `generic_crash x parser_reached_target_heap_buffer_overflow_write` appears for `opensc-pkcs15init-profile-plus-virtual-reader-stream`, preserve card-driver probe sequencing and PKCS#15 binding before retargeting OpenPGP data-object tree lookup order.

## Procedure
1. Split the input into pkcs15-init profile text and a virtual-reader transcript; keep the profile path concrete for the PKCS#15 application.
2. Prepend enough failing APDU status chunks for earlier default card drivers to decline before the OpenPGP driver accepts the first successful select response.
3. Provide a valid OpenPGP application table, capability/object metadata, PIN-status data, algorithm attributes, full binding fingerprint table, and RSA key-generation response.
4. Place a shorter fingerprint-sequence object in an earlier constructed branch so later global fingerprint update resolves it before the full table and writes past that allocation.

## Format Contract
Use [[opensc-pkcs15init-profile-plus-virtual-reader-stream]]; preserve profile/text split, reader chunk order, APDU statuses, and OpenPGP binding data.

## Harness Contract
Use [[libfuzzer-opensc-pkcs15init]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 31 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x parser_reached_target_heap_buffer_overflow_write`.
- Vulnerability class: `heap-buffer-overflow-write`.
- Recovery summary: The verified split depended on successful OpenPGP PKCS#15 binding followed by global fingerprint update resolving an earlier short constructed object.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, clean parser reachability, or fixed-build crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
