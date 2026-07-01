---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached Target Stack Unsigned Integer Underflow To Heap Buffer Verified Recovery"
description: "Round 34 verified recovery for opensc-pkcs15-reader-chunk-stream when wrong_sink pairs with parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "unsigned-integer-underflow-to-heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-target-stack", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "unsigned-integer-underflow-to-heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached Target Stack Unsigned Integer Underflow To Heap Buffer Verified Recovery

- key: `wrong_sink x parser_reached_target_stack`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_target_stack`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `unsigned-integer-underflow-to-heap-buffer-overflow-read`
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_target_stack` appears for `opensc-pkcs15-reader-chunk-stream`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[opensc-pkcs15-reader-chunk-stream]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use the virtual reader transcript contract rather than a normal file. Let earlier card-driver probes receive harmless failure statuses, then satisfy the SetCOS version probe so the SetCOS EID path is selected. Return a successful SELECT response with an FCI/FCP template whose normal EF metadata is valid but whose SetCOS security-attribute subfield declares a remaining subfield length that consumes the whole attribute; the parser then advances by the subfield plus its header and underflows the remaining-length counter.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is a sequence of native little-endian length-prefixed reader chunks. APDU response chunks place the status word at the end, with preceding bytes used as response data. A SetCOS SELECT response can carry an ISO7816 FCI/FCP template containing ordinary file size/type/id tags plus a security-attribute tag; SetCOS 4.4/EID processing parses that security-attribute payload as one or more PTL-coded access-control subfields.

### Harness Contract
The libFuzzer target feeds the raw file bytes to a virtual OpenSC reader. The reader consumes one length-prefixed chunk for connection/ATR handling, then consumes later chunks as APDU responses during card-driver matching, PKCS#15 binding, and file selection. In this build the ATR chunk does not provide a useful ATR gate, so reaching SetCOS depends on the APDU-based version probe rather than ATR matching.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_target_stack`.
- Vulnerability class: `unsigned-integer-underflow-to-heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
