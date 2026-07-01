---
type: causal-policy
title: "Opensc Coolkey Reader Chunks Construct Combined Object Wrong Sink Parser Reached Target Stack Path Stack Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for opensc-coolkey-reader-chunks when wrong_sink pairs with parser_reached_target_stack_path."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_path"
candidate_family: "construct-combined-object"
input_format: "opensc-coolkey-reader-chunks"
harness_convention: "libfuzzer-pkcs15-reader"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-path", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-combined-object", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-target-stack-path", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-combined-object", "stack-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Opensc Coolkey Reader Chunks Construct Combined Object Wrong Sink Parser Reached Target Stack Path Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_stack_path`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_target_stack_path`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct-combined-object`
- vulnerability class: `stack-buffer-overflow-read`
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

### Policy
When `wrong_sink x parser_reached_target_stack_path` appears for `opensc-coolkey-reader-chunks`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-pkcs15-reader]] harness contract and the [[opensc-coolkey-reader-chunks]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use the reader transcript contract to satisfy a syntactically valid ATR, the CoolKey APDU probe, lifecycle, object listing, and a combined-object read. Put an uncompressed V1 CoolKey object inside the combined object and encode it as a private key whose key type is EC, with enough ordinary object attributes for PKCS#15 emulation to accept it. The vulnerable emulator classifies that private EC object as a public EC PKCS#15 object while still passing private-key metadata, so object registration copies the wrong metadata shape and triggers the target stack read; the fixed build rejects or avoids that mismatched type transition.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is a synthetic OpenSC reader transcript made of little-endian length-prefixed chunks. The first chunk is ATR bytes. Later chunks are APDU responses whose final two bytes are status words and whose preceding bytes are response data. The CoolKey path can be reached with an applet probe, lifecycle response, LIST_OBJECTS response, and a combined-object read. A combined object has a CoolKey combined header, an uncompressed decompressed-object area with token-name metadata, and embedded V1 object records containing a fixed-attributes word plus typed attribute records.

### Harness Contract
The libFuzzer target feeds raw bytes to a virtual OpenSC reader. The harness consumes chunks from front to back: one ATR chunk during connect, APDU-response chunks during card matching and PKCS#15 binding, then two more chunks as operation input and parameters before it iterates PKCS#15 objects through crypto and PIN APIs. APDU chunks shorter than a status pair synthesize an invalid-instruction status.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct-combined-object`.
- Verifier key: `wrong_sink x parser_reached_target_stack_path`.
- Vulnerability class: `stack-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
