---
type: causal-policy
title: "Cram Seed Mutate Generic Crash Parser Reached Md5 Heap Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for cram when generic_crash pairs with parser_reached_md5_heap_oob_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_md5_heap_oob_read"
candidate_family: "seed_mutate"
input_format: "cram"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-md5-heap-oob-read", "cram", "libfuzzer", "seed-mutate", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-md5-heap-oob-read", "cram", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Cram Seed Mutate Generic Crash Parser Reached Md5 Heap Oob Read Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_md5_heap_oob_read`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[cram]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_md5_heap_oob_read`
- outcome: server-verified vulnerable/fixed split
- candidate family: `seed_mutate`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[cram]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x parser_reached_md5_heap_oob_read` appears for `cram`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[cram]] format contract before changing sink fields.
2. Recreate the verified causal relation: Start from a valid CRAM v3 seed with a mapped raw slice header and nonzero slice MD5. Preserve the container and block CRC gates, retarget the slice from external reference lookup to an existing embedded reference block, set the slice start negative, and make the declared span just exceed the embedded reference buffer so the MD5 path reads past that buffer after the narrow sanity check accepts it.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
CRAM v3 uses a file definition followed by containers whose headers and blocks are CRC-protected. Mapped slice headers carry reference id/start/span, record count, content IDs, reference-base ID, and MD5. Raw slice-header blocks can be seed-mutated if size relationships and CRCs remain coherent.

### Harness Contract
The harness opens the raw bytes through hts_open on a memory-backed file. If the data is recognized as sequence data, it reads the SAM/CRAM header and iterates records with sam_read1/write. There is no mode byte or FuzzedDataProvider.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `seed_mutate`.
- Verifier key: `generic_crash x parser_reached_md5_heap_oob_read`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
