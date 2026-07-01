---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct No Crash Atr Table Probe No Target Crash Atr List Terminator Negative Memory"
description: "Round 34 negative memory for opensc-pkcs15-reader-chunk-stream when no_crash pairs with atr_table_probe_no_target_crash."
failure_class: "no_crash"
verifier_signal: "atr_table_probe_no_target_crash"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "atr-list-terminator"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "atr-table-probe-no-target-crash", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "atr-table-probe-no-target-crash", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "atr-list-terminator", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opensc Pkcs15 Reader Chunk Stream Construct No Crash Atr Table Probe No Target Crash Atr List Terminator Negative Memory

- key: `no_crash x atr_table_probe_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x atr_table_probe_no_target_crash`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `atr-list-terminator`
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Exact and near-miss IAS/ECC Gemalto, Oberthur, Sagem, PIV Gemalto, PIV Oberthur, and compact-historical-byte ATR probes all exited cleanly. The extracted vulnerable source already showed terminators on the visible IAS/ECC and PIV ATR lists, so the failing attempts likely did not exercise the specific unterminated IDPrime list in the built target or the affected list is selected only after an additional card/application state gate.

### Policy
Treat `no_crash x atr_table_probe_no_target_crash` on `opensc-pkcs15-reader-chunk-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
OpenSC ATR matching compares the first reader chunk against static and configured ATR tables. Tables may include full ATR strings and optional masks; nonmatching ATRs normally walk entries until a null terminator. Some Gemalto/PIV/IAS-ECC paths also infer card type from historical bytes before falling back to known ATR tables.

### Harness Contract
The libFuzzer target uses the same synthetic OpenSC reader chunk stream: the first chunk supplies ATR bytes, later chunks supply APDU response bodies plus trailing status words. ATR-only bugs should trigger during card-driver matching before PKCS#15 operation chunks are consumed.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x atr_table_probe_no_target_crash`.
- Vulnerability class: `atr-list-terminator`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
