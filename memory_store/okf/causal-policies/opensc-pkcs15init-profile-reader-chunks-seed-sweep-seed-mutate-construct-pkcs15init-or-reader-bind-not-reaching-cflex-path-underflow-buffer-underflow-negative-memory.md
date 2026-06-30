---
type: negative-memory
title: "Opensc Pkcs15init Profile Reader Chunks Seed Sweep Seed Mutate Construct Pkcs15init Or Reader Bind Not Reaching Cflex Path Underflow Buffer Underflow Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow."
failure_class: "no_crash"
verifier_signal: "pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow"
candidate_family: "seed_sweep|seed_mutate|construct"
input_format: "opensc-pkcs15init-profile-reader-chunks"
harness_convention: "libfuzzer-opensc-pkcs15init"
vuln_class: "buffer-underflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "pkcs15init-or-reader-bind-not-reaching-cflex-path-underflow", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "seed-sweep-seed-mutate-construct", "buffer-underflow", "negative-memory", "round-29"]
match_keys: ["no_crash", "pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "buffer-underflow", "no-crash", "pkcs15init-or-reader-bind-not-reaching-cflex-path-underflow", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "buffer-underflow", "negative_memory", "seed_sweep|seed_mutate|construct", "seed-sweep-seed-mutate-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# Opensc Pkcs15init Profile Reader Chunks Seed Sweep Seed Mutate Construct Pkcs15init Or Reader Bind Not Reaching Cflex Path Underflow Buffer Underflow Negative Memory

- key: `no_crash x pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15init-profile-reader-chunks]]
- related harness facts: [[libfuzzer-opensc-pkcs15init]]

## Failure Shape
Corpus replay and constructed carriers reached only clean execution under the verifier. Reader-corpus inputs preserved the virtual-reader chunk envelope but did not select the CardFlex short-path state. PKCS#15 init candidates selected a Flex-family ATR and varied the application DF path between normal, single-file-id, and empty-path profiles, with both synthetic success responses and a real seed response transcript, but still did not keep the card/profile state alive through the PKCS#15 bind gate into the erase/delete helper. The remaining missing condition is likely a coherent Flex APDU transcript that both binds PKCS#15 state and exposes an application or object path shorter than the card-specific delete helper assumes.

## Policy
Treat `no_crash x pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow` on `opensc-pkcs15init-profile-reader-chunks` for `buffer-underflow` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pkcs15init_or_reader_bind_not_reaching_cflex_path_underflow`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The pkcs15init fuzzer input is split at the first NUL byte. The prefix is OpenSC profile configuration text; the suffix is a virtual-reader stream of little-endian two-byte length-prefixed chunks. The first reader chunk is the ATR used for card-driver selection. Later chunks are APDU responses whose status words are the final two bytes of each chunk and whose response bodies precede those status words. The OpenSC profile language can define an MF, a PKCS15-AppDF, PIN metadata, ACLs, and key/PIN/data templates; file paths are normally inherited from parent DFs and extended by file IDs, while an AppDF without an explicit path or file-id can exist as a zero-length profile path if no child definition requires inherited path construction.

## Harness Contract
The pkcs15init harness parses the profile prefix, installs a fake smart-card reader from the chunk stream, connects a card from the ATR, binds a pkcs15init profile to the selected card driver, initializes an application, attempts a PKCS#15 bind, then only continues to object operations, finalization, sanity checking, and erase if the PKCS#15 bind succeeds. The related pkcs15-reader harness uses the same virtual-reader chunk contract without the leading profile prefix and binds PKCS#15 directly from APDU responses.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 13 attempts.
- Scope: generator repair and basin avoidance only.
