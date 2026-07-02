---
type: causal-policy
title: "7z Archive Construct Wrong Sink Parser Reached Crc32 Sink Use Of Uninitialized Value Read Verified Recovery"
description: "Round 34 verified recovery for 7z-archive when wrong_sink pairs with parser_reached_crc32_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_crc32_sink"
candidate_family: "construct"
input_format: "7z-archive"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-crc32-sink", "7z-archive", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-crc32-sink", "7z-archive", "libfuzzer", "construct", "use-of-uninitialized-value-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# 7z Archive Construct Wrong Sink Parser Reached Crc32 Sink Use Of Uninitialized Value Read Verified Recovery

- key: `wrong_sink x parser_reached_crc32_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[7z-archive]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_crc32_sink`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `use-of-uninitialized-value-read`
- related format facts: [[7z-archive]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_crc32_sink` appears for `7z-archive`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[7z-archive]] format contract before changing sink fields.
2. Recreate the verified causal relation: Build a structurally coherent 7z encoded-header envelope so the K7Zip handler accepts the signature, start-header CRC, packed-stream metadata, folder coder metadata, unpack-size vector, and folder CRC. Use a packed stream that produces less data than the declared unpack size while keeping the folder CRC marked present, causing the vulnerable CRC calculation to scan the declared span rather than the actual inflated span.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
7z parsing reaches encoded packed-stream decode only after the signature, start header, next-header CRC, PackInfo, Folder coder metadata, CodersUnpackSize, and optional folder CRC records are self-consistent. The encoded header stores metadata separately from the packed stream; PackInfo points back to the packed bytes, and the folder unpack-size vector controls the span later used for CRC verification.

### Harness Contract
The libFuzzer harness passes the raw file bytes through several KArchive handlers with no selector byte and no FuzzedDataProvider layout. The same raw bytes must therefore be a complete archive-like buffer; K7Zip is reached by satisfying its signature and header gates.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_crc32_sink`.
- Vulnerability class: `use-of-uninitialized-value-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
