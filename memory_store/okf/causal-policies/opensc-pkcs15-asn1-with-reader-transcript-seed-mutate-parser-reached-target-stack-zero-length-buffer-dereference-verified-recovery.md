---
type: causal-policy
title: "OPENSC Pkcs15 ASN1 With Reader Transcript Seed Mutate Parser Reached Target Stack Zero Length Buffer Dereference Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_target_stack."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack"
candidate_family: "seed_mutate"
input_format: "opensc-pkcs15-asn1-with-reader-transcript"
harness_convention: "libfuzzer"
vuln_class: "zero-length-buffer-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack", "opensc-pkcs15-asn1-with-reader-transcript", "libfuzzer", "seed-mutate", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_target_stack", "opensc-pkcs15-asn1-with-reader-transcript", "libfuzzer", "zero-length-buffer-dereference", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# OPENSC Pkcs15 ASN1 With Reader Transcript Seed Mutate Parser Reached Target Stack Zero Length Buffer Dereference Verified Recovery

- key: `generic_crash x parser_reached_target_stack`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[opensc-pkcs15-asn1-with-reader-transcript]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from an existing PKCS#15 decode corpus input so the virtual card-reader transcript remains coherent. Preserve the harness framing and reader-response chunks, but replace the ASN.1 decode buffer with an EC public-key object whose EC point OCTET STRING is syntactically present with no content. The vulnerable decoder dereferences the first EC point byte before checking that the decoded OCTET STRING has positive length.

## Policy
For `generic_crash x parser_reached_target_stack` on `opensc-pkcs15-asn1-with-reader-transcript`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `opensc-pkcs15-asn1-with-reader-transcript` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `opensc-pkcs15-asn1-with-reader-transcript` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The parsed object is DER-style ASN.1 for OpenSC PKCS#15 public-key decoding. EC public keys carry an EC point as an OCTET STRING; the ASN.1 layer can produce an empty value for that field even though later EC-key handling expects at least one byte of point data.

## Harness Contract
The fuzz input begins with a little-endian length prefix for the ASN.1 decode buffer, followed by that buffer. The remaining bytes are consumed as a virtual smart-card reader transcript made of little-endian length-prefixed chunks, with the first chunk acting as ATR data and later chunks as APDU responses. There is no additional mode selector.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
