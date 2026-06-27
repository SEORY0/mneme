---
type: causal-policy
title: "Openpgp Signed Message Parser Reached Proc Plaintext Uaf"
description: "Verified recovery for wrong_sink with parser_reached_proc_plaintext_uaf on openpgp signed message inputs."
failure_class: wrong_sink
verifier_signal: parser_reached_proc_plaintext_uaf
candidate_family: seed_mutate
input_format: "openpgp signed message"
harness_convention: libfuzzer
vuln_class: heap-use-after-free-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-proc-plaintext-uaf, openpgp-signed-message, heap-use-after-free-read, verified_recovery]
match_keys: [wrong-sink, parser-reached-proc-plaintext-uaf, openpgp-signed-message, heap-use-after-free-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Openpgp Signed Message Parser Reached Proc Plaintext Uaf

- key: `wrong_sink x parser_reached_proc_plaintext_uaf`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[openpgp-signed-message]]

## Failure Shape
A candidate family ended at `wrong_sink` before a verifier-confirmed repair. The successful shape kept the required `openpgp signed message` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a structurally valid signed OpenPGP message that routes through signature verification and plaintext packet processing. The useful carrier is a signed compressed/plaintext sample; preserving the signature-message envelope is more important than mutating packet bytes. The vulnerable build frees plaintext-related packet state and later reads it while processing the signed data path; the fixed build avoids that stale access.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_proc_plaintext_uaf` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
