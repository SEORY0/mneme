---
type: causal-policy
title: "Wolfssl Randomized Tls Client Stream Construct Local No Crash Official Target Match Weak Ecc Curve Accepted Verified Recovery"
description: "Round 27 verified recovery for no_crash with verifier signal local_no_crash_official_target_match."
failure_class: "no_crash"
verifier_signal: "local_no_crash_official_target_match"
candidate_family: "construct"
input_format: "wolfssl-randomized-tls-client-stream"
harness_convention: "libfuzzer"
vuln_class: "weak-ecc-curve-accepted"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-no-crash-official-target-match", "wolfssl-randomized-tls-client-stream", "libfuzzer", "construct", "weak-ecc-curve-accepted", "verified-recovery", "round-27"]
match_keys: ["no_crash", "local_no_crash_official_target_match", "wolfssl-randomized-tls-client-stream", "libfuzzer", "weak-ecc-curve-accepted", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Wolfssl Randomized Tls Client Stream Construct Local No Crash Official Target Match Weak Ecc Curve Accepted Verified Recovery

## Policy
For `no_crash x local_no_crash_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build the input for the randomized wolfSSL client harness, not as a bare TLS record.
2. Use front-loaded allocation-control bytes that make allocations succeed, then successful randomized-I/O controls with a length-delimited TLS server transcript, and keep the final byte as the client-method selector.
3. The delivered TLS transcript should reach certificate parsing with a TLS server hello followed by a certificate message containing an ECC public key below the 224-bit minimum.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The effective input is a randomized harness envelope around TLS bytes.
- The TLS portion uses normal record and handshake framing; the useful transcript for this task contains a server hello and certificate message carrying a weak ECC certificate.
- Bare TLS bytes alone are not enough for the selected binary because the randomized harness consumes control bytes before network data.
- Harness [[libfuzzer]]:
  - The wrapper runs the wolfSSL randomized client fuzzer on the raw file.
  - The final byte selects one of the client method contexts.
  - Before TLS bytes are consumed, allocation randomization reads bytes from the front; odd choices allow an allocation and even choices fail it.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[wolfssl-randomized-tls-client-stream]] and [[libfuzzer]].
