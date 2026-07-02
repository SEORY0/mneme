---
type: "causal-policy"
title: "Asn1 DER RSA Key Construct Wrong Sink Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "asn1-der-rsa-key"
harness_convention: "honggfuzz-libfuzzer-compatible"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-target-sink", "asn1-der-rsa-key", "honggfuzz-libfuzzer-compatible", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "asn1-der-rsa-key", "honggfuzz-libfuzzer-compatible", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Asn1 DER RSA Key Construct Wrong Sink Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[asn1-der-rsa-key]]
- related harness facts: [[honggfuzz-libfuzzer-compatible]]

## Failure Shape
Construct a malformed DER RSA public-key wrapper that still satisfies the PKCS#8 RSA algorithm-identifier gate after the decoder's cached tag state is shifted. Place the BIT STRING at the point where the outer decoder resumes, and keep the BIT STRING minimal with a valid unused-bit count so the vulnerable bitmap-size calculation includes the count octet itself. The RSA parser then allocates for that inflated bitmap length and copies from the shorter actual bit-string payload, producing a one-byte heap overread; the fixed build rejects or sizes the bitmap correctly.

## Policy
When `wrong_sink x parser_reached_target_sink` appears for `[[asn1-der-rsa-key]]` under `[[honggfuzz-libfuzzer-compatible]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[asn1-der-rsa-key]]` format contract and `[[honggfuzz-libfuzzer-compatible]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[asn1-der-rsa-key]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 3 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
