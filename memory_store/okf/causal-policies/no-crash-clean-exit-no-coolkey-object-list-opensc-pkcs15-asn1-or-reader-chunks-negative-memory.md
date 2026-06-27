---
type: causal-policy
title: "No Crash Clean Exit No Coolkey Object List Opensc Pkcs15 ASN1 Or Reader Chunks Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal clean_exit_no_coolkey_object_list."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_coolkey_object_list"
candidate_family: "construct-asn1-and-chunked-reader"
input_format: "opensc-pkcs15-asn1-or-reader-chunks"
harness_convention: "libfuzzer-opensc-pkcs15"
vuln_class: "identifier-collision-logic-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-no-coolkey-object-list", "opensc-pkcs15-asn1-or-reader-chunks", "negative-memory", "round-20"]
match_keys: ["no-crash", "clean-exit-no-coolkey-object-list", "opensc-pkcs15-asn1-or-reader-chunks"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Clean Exit No Coolkey Object List Opensc Pkcs15 ASN1 Or Reader Chunks Negative Memory

- key: `no_crash x clean_exit_no_coolkey_object_list`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[opensc-pkcs15-asn1-or-reader-chunks]]
- harnesses: [[libfuzzer-opensc-pkcs15]]

## Dead End
The round 20 attempts for `opensc-pkcs15-asn1-or-reader-chunks` under `libfuzzer-opensc-pkcs15` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Both direct PKCS#15 ASN.1 records and length-prefixed reader-response streams reached only clean exits. The likely missing gate is a coolkey-specific emulated-card object-list population path; generic duplicate identifier records did not bind a card profile or object list that exercises the uniqueness invariant.

## Negative Policy
When retrieval matches `no_crash x clean_exit_no_coolkey_object_list`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[opensc-pkcs15-asn1-or-reader-chunks]] and [[libfuzzer-opensc-pkcs15]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
