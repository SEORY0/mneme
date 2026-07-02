---
type: causal-policy
title: "Opensc Coolkey Reader Chunks Construct Reader Transcript Wrong Sink Vulnerable Crash Fixed Clean After Empty Lifecycle Fallback Stack Buffer Overflow Read Gated By Empty Verified Recovery"
description: "Round 34 verified recovery for opensc-coolkey-reader-chunks when wrong_sink pairs with vulnerable_crash_fixed_clean_after_empty_lifecycle_fallback."
failure_class: "wrong_sink"
verifier_signal: "vulnerable_crash_fixed_clean_after_empty_lifecycle_fallback"
candidate_family: "construct-reader-transcript"
input_format: "opensc-coolkey-reader-chunks"
harness_convention: "libfuzzer-pkcs15-reader"
vuln_class: "stack-buffer-overflow-read gated by empty-response logic"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "vulnerable-crash-fixed-clean-after-empty-lifecycle-fallback", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-reader-transcript", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "vulnerable-crash-fixed-clean-after-empty-lifecycle-fallback", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-reader-transcript", "stack-buffer-overflow-read-gated-by-empty-response-logic", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Opensc Coolkey Reader Chunks Construct Reader Transcript Wrong Sink Vulnerable Crash Fixed Clean After Empty Lifecycle Fallback Stack Buffer Overflow Read Gated By Empty Verified Recovery

- key: `wrong_sink x vulnerable_crash_fixed_clean_after_empty_lifecycle_fallback`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

## Round 34 Verified Support

- key: `wrong_sink x vulnerable_crash_fixed_clean_after_empty_lifecycle_fallback`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct-reader-transcript`
- vulnerability class: `stack-buffer-overflow-read gated by empty-response logic`
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

### Policy
When `wrong_sink x vulnerable_crash_fixed_clean_after_empty_lifecycle_fallback` appears for `opensc-coolkey-reader-chunks`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-pkcs15-reader]] harness contract and the [[opensc-coolkey-reader-chunks]] format contract before changing sink fields.
2. Recreate the verified causal relation: Drive the virtual reader into the CoolKey driver, then make the full lifecycle query fall back and answer the fallback lifecycle query with a successful status but no response body. After that gate, provide a CoolKey combined object that includes a harmless non-key object before a private RSA key so the CoolKey object-selection quirk lets later key operations proceed. The observable crash is produced by a later RSA operation whose returned body advertises more output than the local stack response buffer can hold; the fixed build rejects the empty fallback response before reaching that operation.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is a sequence of little-endian length-prefixed reader chunks. The first chunk is used as ATR data; later chunks are APDU responses with response data before trailing status bytes. CoolKey initialization can list a combined object, read it, and unpack an uncompressed combined-object area containing a token-name header and embedded V1 object records. A useful private-key record needs class, key type, identifier, usage booleans, and RSA public-key attributes; placing a non-key record before the key works with the driver's object lookup behavior during key selection.

### Harness Contract
The fuzz target installs a fake OpenSC reader, connects a card, binds PKCS#15, then consumes two more chunks as operation input and parameters before iterating PKCS#15 objects. Before synthetic CoolKey binding, normal PKCS#15 file probes consume APDU response chunks, so the transcript needs explicit failing probe responses to keep the later operation chunks aligned.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct-reader-transcript`.
- Verifier key: `wrong_sink x vulnerable_crash_fixed_clean_after_empty_lifecycle_fallback`.
- Vulnerability class: `stack-buffer-overflow-read gated by empty-response logic`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
