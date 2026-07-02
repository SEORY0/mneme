---
type: causal-policy
title: "Raw Pkcs11 Fuzzer Record Seed Mutate Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "raw-pkcs11-fuzzer-record"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "raw-pkcs11-fuzzer-record", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached", "raw-pkcs11-fuzzer-record", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Raw Pkcs11 Fuzzer Record Seed Mutate Parser Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a corpus seed that already selects the PKCS#11 verify operation and initializes a virtual card with a reachable public-key object.
2. Preserve the mechanism, login, signature buffer, and virtual-card response tail.
3. Increase only the verify-data segment so it crosses the harness chunking threshold; the vulnerable verify loop then copies from the remaining card-data pointer instead of from the verify-data pointer and over-reads the fuzz input tail.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The fuzz record is a raw byte stream with a leading operation selector.
- The verify operation consumes a native-width mechanism value, a login-type byte, a NUL-terminated PIN string, then several little-endian length-prefixed buffers for object id, verify data, and signature.
- The remaining bytes are consumed by the virtual smart-card reader as length-prefixed APDU response chunks.
- Harness [[libfuzzer]]:
  - The libFuzzer harness passes the whole file to LLVMFuzzerTestOneInput.
  - The first byte selects one PKCS#11 operation; operation-specific parsers consume fields from the front, and the leftover tail becomes virtual-reader data.
  - The verify path uses direct C_Verify for small verify data and an update/final loop for larger verify data.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[raw-pkcs11-fuzzer-record]] and [[libfuzzer]].
