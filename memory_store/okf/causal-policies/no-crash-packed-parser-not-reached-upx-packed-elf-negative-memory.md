---
type: causal-policy
title: "No Crash Packed Parser Not Reached Upx Packed ELF Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal packed_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "packed_parser_not_reached"
candidate_family: "construct"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-upx-test-file"
vuln_class: "elf-dynamic-string-table-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packed-parser-not-reached", "upx-packed-elf", "negative-memory", "round-15"]
match_keys: ["no_crash", "packed_parser_not_reached", "upx-packed-elf", "libfuzzer-upx-test-file", "elf-dynamic-string-table-bounds", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Packed Parser Not Reached Upx Packed ELF Negative Memory

- key: `no_crash x packed_parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-elf]]
- related harness facts: [[libfuzzer-upx-test-file]]

## Failure Shape
- Empty data, a minimal ELF header, and an ordinary host ELF did not reach the UPX packed-ELF dynamic-
  table parser. The missing gate is a UPX-recognized packed ELF layout with valid UPX metadata and
  dynamic entries; only after that gate can DT_STRSZ be mutated to violate the string-table bound
  checks.

## Policy
Treat `no_crash x packed_parser_not_reached` on `upx-packed-elf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The vulnerable code is in UPX's Linux ELF unpacker. It expects an ELF file that is recognized as
  UPX-packed, with UPX metadata, program/dynamic tables, and dynamic entries including string table
  information. DT_STRSZ defines the dynamic string table size and is later used to bound symbol and
  version-string name lookups.

## Harness Contract
- The harness writes raw input bytes to a temporary file and invokes UPX in test mode on that file.
  The input is not length-prefixed and has no argv selector or FuzzedDataProvider layout, but it must
  pass UPX's packed-file recognition before the Linux ELF unpacker dynamic-table code is reached.

## Negative Memory
- Do not resubmit variants that only reproduce `packed_parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
