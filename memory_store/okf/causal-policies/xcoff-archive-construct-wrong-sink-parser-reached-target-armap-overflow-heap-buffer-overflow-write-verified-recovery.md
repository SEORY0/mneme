---
type: causal-policy
title: "Xcoff Archive Construct Wrong Sink Parser Reached Target Armap Overflow Heap Buffer Overflow Write Verified Recovery"
description: "Round 34 verified recovery for xcoff-archive when wrong_sink pairs with parser_reached_target_armap_overflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_armap_overflow"
candidate_family: "construct"
input_format: "xcoff-archive"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-armap-overflow", "xcoff-archive", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-target-armap-overflow", "xcoff-archive", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Xcoff Archive Construct Wrong Sink Parser Reached Target Armap Overflow Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_target_armap_overflow`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[xcoff-archive]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_target_armap_overflow`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-write`
- related format facts: [[xcoff-archive]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_target_armap_overflow` appears for `xcoff-archive`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[xcoff-archive]] format contract before changing sink fields.
2. Recreate the verified causal relation: Build a recognized big XCOFF archive with a coherent outer archive header and a global symbol-table pointer that lands on a parseable archive-map member. Keep the member envelope small and syntactically valid, then place an oversized symbol count in the armap body so the count-to-byte bounds check wraps below the member size while the later armap population loop still trusts the original count.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The big XCOFF archive path starts with a big-archive magic string, then fixed-width decimal archive-header fields for member-table and symbol-table offsets. The symbol-table offset names an archive member header, not the map body. That member header carries decimal size and linkage fields, a decimal name length, optional padded name bytes, an archive-member trailer, and then the armap contents. The armap body begins with a target-endian symbol count followed by per-symbol file offsets and trailing symbol-name strings.

### Harness Contract
The BFD fuzz harness writes the raw input bytes to a temporary file and calls BFD archive-format detection on that file. There is no mode byte, checksum wrapper, FuzzedDataProvider layout, or length prefix outside the archive format itself.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_target_armap_overflow`.
- Vulnerability class: `heap-buffer-overflow-write`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
