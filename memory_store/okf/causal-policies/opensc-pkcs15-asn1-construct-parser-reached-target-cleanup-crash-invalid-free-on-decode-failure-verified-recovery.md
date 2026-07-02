---
type: causal-policy
title: "OPENSC Pkcs15 ASN1 Construct Parser Reached Target Cleanup Crash Invalid Free On Decode Failure Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_target_cleanup_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_cleanup_crash"
candidate_family: "construct"
input_format: "opensc-pkcs15-asn1"
harness_convention: "libfuzzer"
vuln_class: "invalid-free-on-decode-failure"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-cleanup-crash", "opensc-pkcs15-asn1", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_target_cleanup_crash", "opensc-pkcs15-asn1", "libfuzzer", "invalid-free-on-decode-failure", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# OPENSC Pkcs15 ASN1 Construct Parser Reached Target Cleanup Crash Invalid Free On Decode Failure Verified Recovery

- key: `wrong_sink x parser_reached_target_cleanup_crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[opensc-pkcs15-asn1]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a DER-like PKCS#15 private-key directory entry that satisfies the outer private-key choice, common object attributes, and common key attributes. Include the optional private-key subclass subject-name field so the decoder records it as present, then make the required type-specific private-key attributes absent or malformed. The vulnerable cleanup path frees the wrong pointer after the partial decode failure; the fixed build rejects or cleans the partial state safely.

## Policy
For `wrong_sink x parser_reached_target_cleanup_crash` on `opensc-pkcs15-asn1`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `opensc-pkcs15-asn1` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `opensc-pkcs15-asn1` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The direct PKCS#15 decoder accepts a top-level constructed private-key choice. The object body contains common object attributes, common key attributes with an identifier and usage bit field, an optional private-key subclass section carrying a subject-name sequence, and a required type-specific key-attribute section such as RSA path and size data. Definite-length DER-like constructed fields are enough; a full smart-card transcript is not required for this harness.

## Harness Contract
The libFuzzer target passes the same raw input buffer directly to several PKCS#15 directory-entry decoders in a loop, then to public-key, tokeninfo, and unused-space parsers. There is no leading selector byte, no length-prefixed reader chunk stream, and no FuzzedDataProvider back/front split.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 6 attempts.
- Scope: generator repair and retargeting only.
