---
type: causal-policy
title: "Opensc Coolkey Reader Chunks Construct Direct Reader Chunks No Crash Coolkey Path Reached Clean Exit Identifier Confusion Negative Memory"
description: "Round 34 negative memory for opensc-coolkey-reader-chunks when no_crash pairs with coolkey_path_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "coolkey_path_reached_clean_exit"
candidate_family: "construct-direct-reader-chunks"
input_format: "opensc-coolkey-reader-chunks"
harness_convention: "libfuzzer-pkcs15-reader"
vuln_class: "identifier-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "coolkey-path-reached-clean-exit", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-direct-reader-chunks", "negative-memory", "round-34"]
match_keys: ["no-crash", "coolkey-path-reached-clean-exit", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-direct-reader-chunks", "identifier-confusion", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opensc Coolkey Reader Chunks Construct Direct Reader Chunks No Crash Coolkey Path Reached Clean Exit Identifier Confusion Negative Memory

- key: `no_crash x coolkey_path_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

## Round 34 Negative Support

- key: `no_crash x coolkey_path_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- candidate family: `construct-direct-reader-chunks`
- vulnerability class: `identifier-confusion`
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

### Failure Shape
The chunk stream can bind the CoolKey driver and populate the synthetic CoolKey object list. The strongest family used a direct object-list transcript where a malformed or private-key-shaped record was intended to be cached under a different list entry through the vulnerable object lookup relation, with the fixed path receiving a harmless replacement record. Local debug confirmed CoolKey/PKCS#15 execution, but the attempted state confusions either produced only rejected PKCS#15 operations or clean PIN/key iteration, and the official vulnerable run exited cleanly.

### Policy
Treat `no_crash x coolkey_path_reached_clean_exit` on `opensc-coolkey-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The input is a sequence of little-endian length-prefixed reader chunks. The first chunk is ATR data. Later chunks are APDU responses: the final two bytes are status words and any preceding bytes are copied as response data. CoolKey initialization requires successful applet-selection and lifecycle responses, then LIST_OBJECTS responses. A direct object entry carries a big-endian object identifier, a big-endian object length, and ACL fields; object data returned by READ_OBJECT is a CoolKey object record with a record-type byte, object identifier, compressed fixed-attribute word, attribute count, and typed attribute records. A combined-object route uses a single listed combined object containing a combined header, uncompressed decompressed area, token-name header, and embedded V1 records.

### Harness Contract
The libFuzzer target feeds raw bytes to a virtual OpenSC reader. The reader consumes length-prefixed chunks front-to-back: connect consumes ATR, card-driver matching and PKCS#15 binding consume APDU response chunks, then the harness consumes two additional chunks as operation input and parameter buffers before iterating discovered PKCS#15 objects through decrypt, derive, wrap, signature, and PIN APIs. CoolKey is reached through APDU-speaking card-driver matching; a generic ATR can avoid earlier ATR table matches and leave early APDU chunks for CoolKey selection.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct-direct-reader-chunks`.
- Verifier key: `no_crash x coolkey_path_reached_clean_exit`.
- Vulnerability class: `identifier-confusion`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
