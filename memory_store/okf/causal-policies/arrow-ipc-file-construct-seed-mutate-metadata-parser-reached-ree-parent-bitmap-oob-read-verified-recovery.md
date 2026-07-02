---
type: causal-policy
title: "Arrow Ipc File Construct Seed Mutate Metadata Parser Reached Ree Parent Bitmap Oob Read Verified Recovery"
description: "Server-verified recovery for arrow-ipc-file when generic_crash pairs with parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct_seed_mutate_metadata"
input_format: "arrow-ipc-file"
harness_convention: "libfuzzer-raw-arrow-ipc"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "arrow-ipc-file", "libfuzzer-raw-arrow-ipc", "construct-seed-mutate-metadata", "verified-recovery", "round-31"]
match_keys: ["generic-crash", "parser-reached", "arrow-ipc-file", "libfuzzer-raw-arrow-ipc", "construct-seed-mutate-metadata", "out-of-bounds-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 31
---
# Arrow Ipc File Construct Seed Mutate Metadata Parser Reached Ree Parent Bitmap Oob Read Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[arrow-ipc-file]]
- related harness facts: [[libfuzzer-raw-arrow-ipc]]

## Policy
When `generic_crash x parser_reached` appears for `arrow-ipc-file`, do not corrupt file framing; retarget pre-V5 REE parent validity metadata and the unknown-null-count recomputation invariant.

## Procedure
1. Start from a valid Arrow IPC file with readable schema, footer, record-batch block table, and run-end-encoded arrays.
2. Force older IPC metadata so REE parents can carry parent validity-buffer metadata.
3. Keep record-batch row counts and child array metadata consistent enough for full validation to recurse through children.
4. Mark the targeted REE parent null count as unknown while keeping its parent validity buffer invalidly small, so null-count recomputation reads past that bitmap.

## Format Contract
Use [[arrow-ipc-file]]; preserve IPC magic/footer framing, block table, schema, and child arrays while mutating parent validity metadata.

## Harness Contract
Use [[libfuzzer-raw-arrow-ipc]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 31 solve.
- Candidate family: construct_seed_mutate_metadata.
- Verifier key: `generic_crash x parser_reached`.
- Vulnerability class: `out-of-bounds-read`.
- Recovery summary: The verified split required ValidateFull to reach REE child validation before recomputing the parent null count from an undersized parent bitmap.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, clean parser reachability, or fixed-build crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
