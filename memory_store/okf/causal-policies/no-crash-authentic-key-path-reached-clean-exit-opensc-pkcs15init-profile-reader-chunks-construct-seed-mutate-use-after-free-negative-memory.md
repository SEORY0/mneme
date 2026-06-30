---
type: negative-memory
title: "No Crash Authentic Key Path Reached Clean Exit OPENSC Pkcs15init Profile Reader Chunks Construct Seed Mutate Use After Free Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal authentic_key_path_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "authentic_key_path_reached_clean_exit"
candidate_family: "construct+seed_mutate"
input_format: "opensc-pkcs15init-profile-reader-chunks"
harness_convention: "libfuzzer-opensc-pkcs15init"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "authentic-key-path-reached-clean-exit", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "construct-seed-mutate", "negative-memory", "round-26"]
match_keys: ["no_crash", "authentic_key_path_reached_clean_exit", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Authentic Key Path Reached Clean Exit OPENSC Pkcs15init Profile Reader Chunks Construct Seed Mutate Use After Free Negative Memory

- key: `no_crash x authentic_key_path_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15init-profile-reader-chunks]]
- related harness facts: [[libfuzzer-opensc-pkcs15init]]

## Failure Shape
The best constructed carrier reached the AuthentIC card driver, parsed an AuthentIC pkcs15init profile, bound PKCS#15 state, and entered the RSA private-key creation path. The normal private-key template ACLs caused the SDO ACL helper to return a positive serialized length that the caller treated as failure, so object content was never populated. Mutating those ACL methods to valid but unserialized methods allowed SDO creation to proceed, but the later access-rule fixer rejected the same methods before object content allocation. Removing explicit private-key ACLs fell back to default open ACL entries, which still serialized to a positive length. Reusing the shipped pkcs15init corpus response stream with the AuthentIC profile and ATR failed to maintain a usable PKCS#15 bind. No attempted family produced a sanitizer crash in the vulnerable image.

## Policy
Treat `no_crash x authentic_key_path_reached_clean_exit` on `opensc-pkcs15init-profile-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `authentic_key_path_reached_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `authentic_key_path_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is split at the first NUL byte. The prefix is OpenSC profile configuration text. The suffix is a virtual smart-card reader stream made of little-endian two-byte chunk lengths followed by chunk bodies. The first chunk is the card ATR used for driver selection. Later chunks are APDU responses; status words are stored at the end of each response chunk and response bodies precede them. The AuthentIC profile defines a PKCS#15 application DF, PKCS#15 metadata EFs, and private-key/public-key/certificate templates. The private-key template ACL methods directly affect both SDO ACL serialization and later PKCS#15 access-rule synthesis.

## Harness Contract
The selected target is fuzz_pkcs15init. It installs a fuzz reader, connects a card using the first reader chunk, parses the profile prefix, binds pkcs15init state, initializes the app, attempts PKCS#15 bind, then exercises PIN storage, data-object storage, key generation, secret-key operations, finalization, sanity check, and erase. All reader chunks are consumed front-to-back; this harness is not a raw APDU-only parser and not the separate card fuzzer.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 5 attempts.
- Scope: generator repair and basin avoidance only.
