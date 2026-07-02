---
type: causal-policy
title: "Open62541 Json Variant Seed Mutate Generic Crash Parser Reached Target Match Official Null Dereference Verified Recovery"
description: "Round 34 verified recovery for open62541-json-variant when generic_crash pairs with parser_reached_target_match_official."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match_official"
candidate_family: "seed_mutate"
input_format: "open62541-json-variant"
harness_convention: "libfuzzer"
vuln_class: "null-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match-official", "open62541-json-variant", "libfuzzer", "seed-mutate", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-target-match-official", "open62541-json-variant", "libfuzzer", "seed-mutate", "null-dereference", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Open62541 Json Variant Seed Mutate Generic Crash Parser Reached Target Match Official Null Dereference Verified Recovery

- key: `generic_crash x parser_reached_target_match_official`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[open62541-json-variant]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_target_match_official`
- outcome: server-verified vulnerable/fixed split
- candidate family: `seed_mutate`
- vulnerability class: `null-dereference`
- related format facts: [[open62541-json-variant]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x parser_reached_target_match_official` appears for `open62541-json-variant`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[open62541-json-variant]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use a syntactically valid OPC UA JSON Variant whose body is an ExtensionObject-like object. Keep the top-level Variant Type and Body gates valid, include a nested TypeId object and a nested Body object, but make the TypeId resolve to no known datatype while omitting the explicit encoding marker. This reaches the Variant ExtensionObject unwrap path, where the vulnerable decoder treats the unknown structure body as a decoded body and dereferences a null datatype; the fixed build rejects or skips it cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is raw JSON decoded as an OPC UA Variant. A valid Variant is a JSON object with numeric Type and Body fields. Type values select OPC UA builtin datatypes; an ExtensionObject body is itself an object with TypeId, optional Encoding, and Body fields. Unknown structure-encoded ExtensionObject bodies can be represented as nested JSON objects that the decoder may preserve or skip rather than decode.

### Harness Contract
The libFuzzer harness passes the complete file bytes directly as a UA_ByteString to UA_decodeJson with the destination type fixed to Variant. There is no prefix, checksum, mode selector, or FuzzedDataProvider layout; malformed JSON or schemas that fail the first Variant decode exit before the vulnerable path.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `seed_mutate`.
- Verifier key: `generic_crash x parser_reached_target_match_official`.
- Vulnerability class: `null-dereference`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
