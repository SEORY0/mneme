---
type: causal-policy
title: "Opensc Pkcs15 Reader Apdu Chunk Stream Construct Wrong Sink Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-apdu-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "opensc-pkcs15-reader-apdu-chunk-stream", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "sink_mismatch", "opensc-pkcs15-reader-apdu-chunk-stream", "libfuzzer", "heap-buffer-overflow-read", "wrong-sink", "sink-mismatch", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Opensc Pkcs15 Reader Apdu Chunk Stream Construct Wrong Sink Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-pkcs15-reader-apdu-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use a chunk stream whose first chunk presents an ATR that selects the Oberthur card driver. Let early generic PKCS#15 discovery probes fail fast with ordinary file-not-found responses so they do not consume or rebase the Oberthur profile sequence. Then provide enough successful Oberthur select, PIN-status, and transparent-file responses to reach the container metadata parser, and make the container metadata advertise a record while supplying a record body that is shorter than the fields the parser unconditionally reads.

## Policy
When `wrong_sink x sink_mismatch` appears for `opensc-pkcs15-reader-apdu-chunk-stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opensc-pkcs15-reader-apdu-chunk-stream]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `opensc-pkcs15-reader-apdu-chunk-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 3 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
