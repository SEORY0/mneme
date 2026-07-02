---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunks Construct Seed Mutate No Crash Dnie Parser Reached Clean Exit Unchecked Uncompressed Length Negative Memory"
description: "Round 34 negative memory for opensc-pkcs15-reader-chunks when no_crash pairs with dnie_parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "dnie_parser_reached_clean_exit"
candidate_family: "construct|seed_mutate"
input_format: "opensc-pkcs15-reader-chunks"
harness_convention: "honggfuzz-libfuzzer"
vuln_class: "unchecked-uncompressed-length"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dnie-parser-reached-clean-exit", "opensc-pkcs15-reader-chunks", "honggfuzz-libfuzzer", "construct-seed-mutate", "negative-memory", "round-34"]
match_keys: ["no-crash", "dnie-parser-reached-clean-exit", "opensc-pkcs15-reader-chunks", "honggfuzz-libfuzzer", "construct-seed-mutate", "unchecked-uncompressed-length", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opensc Pkcs15 Reader Chunks Construct Seed Mutate No Crash Dnie Parser Reached Clean Exit Unchecked Uncompressed Length Negative Memory

- key: `no_crash x dnie_parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunks]]
- related harness facts: [[honggfuzz-libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x dnie_parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- candidate family: `construct|seed_mutate`
- vulnerability class: `unchecked-uncompressed-length`
- related format facts: [[opensc-pkcs15-reader-chunks]]
- related harness facts: [[honggfuzz-libfuzzer]]

### Failure Shape
The final constructed candidates reached DNIe ATR matching, valid TokenInfo parsing, ODF parsing, and a compressed certificate-DF read. Mismatched declared/actual decompressed lengths and an oversized declared decompressed length invoked the DNIe decompressor, including allocator warning behavior, but the wrapper returned cleanly instead of producing a sanitizer-visible crash. ATR-mutated corpus seeds and earlier compressed TokenInfo variants also stayed clean or failed before the target path.

### Policy
Treat `no_crash x dnie_parser_reached_clean_exit` on `opensc-pkcs15-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The reader input is a stream of native-endian length-prefixed chunks. The first chunk supplies the ATR; subsequent chunks are APDU responses whose final status bytes set the card status word and whose preceding bytes become response data. DNIe selection walks the master file and application/file identifiers, FCI responses carry an ISO wrapper plus a proprietary attribute describing DF, plain EF, or compressed EF files, and compressed EF content begins with little-endian uncompressed/compressed lengths followed by a zlib stream. PKCS#15 TokenInfo is ASN.1 with version, manufacturer, and token flags; ODF entries are context-specific choices containing ASN.1 paths to DF files.

### Harness Contract
The fuzz target installs a fake OpenSC reader, connects a card from the first ATR chunk, binds PKCS#15, and consumes later chunks as APDU responses. If binding succeeds it consumes additional chunks for operation inputs and iterates PKCS#15 objects, but all card I/O still comes from the same front-to-back chunk stream.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct|seed_mutate`.
- Verifier key: `no_crash x dnie_parser_reached_clean_exit`.
- Vulnerability class: `unchecked-uncompressed-length`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
