---
type: causal-policy
title: Opensc Pkcs15 Asn1 Or Reader Chunk Stream Clean Exit Negative Memory
description: Negative memory for opensc-pkcs15-asn1-or-reader-chunk-stream candidates that ended in no_crash with verifier signal `clean_exit`.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: construct
input_format: opensc-pkcs15-asn1-or-reader-chunk-stream
harness_convention: libfuzzer
vuln_class: invalid-ec-key-type-handling
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, clean-exit, opensc-pkcs15-asn1-or-reader-chunk-stream, libfuzzer, construct, invalid-ec-key-type-handling, negative-memory]
match_keys: [no-crash, clean-exit, opensc-pkcs15-asn1-or-reader-chunk-stream, libfuzzer, construct, invalid-ec-key-type-handling, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `clean_exit`` for `opensc-pkcs15-asn1-or-reader-chunk-stream` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `clean_exit`.
2. Stop repeating the dead-end basin: Standalone EC-key ASN.1 probes and chunked virtual-reader APDU responses exited cleanly. The missing relation is probably valid PKCS#15/coolkey card state plus an invalid EC key object type, not merely an EC algorithm identifier in isolation.
3. Rebuild around `[[opensc-pkcs15-asn1-or-reader-chunk-stream]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.
