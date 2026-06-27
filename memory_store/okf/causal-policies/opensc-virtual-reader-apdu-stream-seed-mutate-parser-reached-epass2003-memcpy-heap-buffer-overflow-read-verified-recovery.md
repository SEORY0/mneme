---
type: causal-policy
title: "Opensc Virtual Reader APDU Stream Seed Mutate Parser Reached Epass2003 Memcpy Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for opensc-virtual-reader-apdu-stream when generic_crash pairs with parser_reached_epass2003_memcpy."
failure_class: "generic_crash"
verifier_signal: "parser_reached_epass2003_memcpy"
candidate_family: "seed_mutate"
input_format: "opensc-virtual-reader-apdu-stream"
harness_convention: "opensc-card-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-epass2003-memcpy", "opensc-virtual-reader-apdu-stream", "opensc-card-fuzzer", "seed-mutate", "verified-recovery", "round-18"]
match_keys: ["generic-crash", "parser-reached-epass2003-memcpy", "opensc-virtual-reader-apdu-stream", "opensc-card-fuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Opensc Virtual Reader APDU Stream Seed Mutate Parser Reached Epass2003 Memcpy Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_epass2003_memcpy`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opensc-virtual-reader-apdu-stream]]
- related harness facts: [[opensc-card-fuzzer]]

## Policy
When `generic_crash x parser_reached_epass2003_memcpy` appears for `opensc-virtual-reader-apdu-stream`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Drive the OpenSC virtual reader through card initialization into the epass2003 PKCS#15 key-generation path.
2. Return an APDU response whose advertised or expected key-buffer size is larger than the allocated response buffer, so the vulnerable code copies from the undersized allocation.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[opensc-virtual-reader-apdu-stream]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[opensc-card-fuzzer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: seed_mutate.

## Round 18 Verified Evidence
- Verifier key: `generic_crash x parser_reached_epass2003_memcpy`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Drive the OpenSC virtual reader through card initialization into the epass2003 PKCS#15 key-generation path.
