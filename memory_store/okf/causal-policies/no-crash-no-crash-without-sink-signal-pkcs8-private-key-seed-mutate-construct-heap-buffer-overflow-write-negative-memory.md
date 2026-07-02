---
type: negative-memory
title: "No Crash No Crash Without Sink Signal Pkcs8 Private Key Seed Mutate Construct Heap Buffer Overflow Write Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal no_crash_without_sink_signal."
failure_class: "no_crash"
verifier_signal: "no_crash_without_sink_signal"
candidate_family: "seed_mutate|construct"
input_format: "pkcs8-private-key"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "no-crash-without-sink-signal", "pkcs8-private-key", "libfuzzer", "seed-mutate-construct", "negative-memory", "round-26"]
match_keys: ["no_crash", "no_crash_without_sink_signal", "pkcs8-private-key", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash No Crash Without Sink Signal Pkcs8 Private Key Seed Mutate Construct Heap Buffer Overflow Write Negative Memory

- key: `no_crash x no_crash_without_sink_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pkcs8-private-key]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The PKCS#8 harness accepted real EC private-key seeds and several constructed explicit-domain EC/DH variants, but none produced the target crash. EC attempts preserved the PrivateKeyInfo envelope and omitted the embedded public point so key load would derive it through scalar multiplication. DH attempts used valid AlgorithmIdentifier parameters to force Montgomery precomputation and public-value derivation. The likely remaining gap is finding the exact internal BigInt allocation boundary where a Montgomery temporary is sized narrowly enough for the reducer's larger access pattern; the tested valid-looking domains either did not reach that exact temporary shape or allocation rounding masked it.

## Policy
Treat `no_crash x no_crash_without_sink_signal` on `pkcs8-private-key` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `no_crash_without_sink_signal` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `no_crash_without_sink_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The harness input is a PKCS#8 PrivateKeyInfo, either DER or PEM. The outer structure contains a version, an AlgorithmIdentifier, and an OCTET STRING containing the algorithm-specific private key. EC private keys use an ECPrivateKey SEQUENCE with version and private scalar, optionally carrying parameters or a public point; when the public point is absent Botan derives it from the domain base point. Explicit EC domain parameters are a SEQUENCE containing a prime-field descriptor, curve coefficients encoded as OCTET STRING values, an encoded base point, an order, and a cofactor. DH/DSA private keys use AlgorithmIdentifier parameters carrying group integers, and the private-key OCTET STRING contains a DER INTEGER scalar.

## Harness Contract
The libFuzzer entrypoint passes the raw input bytes directly to Botan::PKCS8::load_key through a memory data source with no FuzzedDataProvider carving. The task wrapper runs the pkcs8 fuzzer on one file path. Parser exceptions are caught by the fuzzer, so malformed ASN.1 and rejected key parameters usually appear as clean no-crash executions rather than bad_format.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 8 attempts.
- Scope: generator repair and basin avoidance only.
