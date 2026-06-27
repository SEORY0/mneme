---
type: causal-policy
title: "No Crash X509 Processed Cleanly X509 Der Certificate With General Name Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal x509_processed_cleanly."
failure_class: "no_crash"
verifier_signal: "x509_processed_cleanly"
candidate_family: "construct"
input_format: "x509-der-certificate-with-general-name"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "x509-processed-cleanly", "x509-der-certificate-with-general-name", "negative-memory", "round-13"]
match_keys: ["no_crash", "x509_processed_cleanly", "x509-der-certificate-with-general-name", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash X509 Processed Cleanly X509 Der Certificate With General Name Negative Memory

- key: `no_crash x x509_processed_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[x509-der-certificate-with-general-name]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Direct GENERAL_NAME and OTHERNAME DER objects were the wrong surface for the selected target, and a generated X.509 certificate with a subjectAltName OTHERNAME type mismatch still printed cleanly. The missing relation is a certificate extension that parses as a recognized OTHERNAME OID while retaining a mismatched ASN1_TYPE shape that the printer accepts far enough to dereference as the expected string type.

## Policy
Treat `no_crash x x509_processed_cleanly` on `x509-der-certificate-with-general-name` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `x509_processed_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The relevant structure is an X.509 DER certificate containing a subjectAltName extension with an otherName GeneralName. OtherName contains an object identifier and an explicitly tagged ASN.1 value; the vulnerable printers choose the expected value type from the object identifier rather than from the parsed ASN1_TYPE tag.

## Harness Contract
The selected wrapper is the OpenSSL X.509 fuzzer. It consumes the entire PoC as DER for d2i_X509, then prints the certificate and extensions to a null BIO. There is no command-line selector; standalone GENERAL_NAME DER does not reach the selected harness path.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x x509_processed_cleanly`
- related format facts: [[x509-der-certificate-with-general-name]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Direct GENERAL_NAME and OTHERNAME DER objects were the wrong surface for the selected target, and a generated X.509 certificate with a subjectAltName OTHERNAME type mismatch still printed cleanly. The missing relation is a certificate extension that parses as a recognized OTHERNAME OID while retaining a mismatched ASN1_TYPE shape that the printer accepts far enough to dereference as the expected string type.

### Format Contract Delta
The relevant structure is an X.509 DER certificate containing a subjectAltName extension with an otherName GeneralName. OtherName contains an object identifier and an explicitly tagged ASN.1 value; the vulnerable printers choose the expected value type from the object identifier rather than from the parsed ASN1_TYPE tag.

### Harness Contract Delta
The selected wrapper is the OpenSSL X.509 fuzzer. It consumes the entire PoC as DER for d2i_X509, then prints the certificate and extensions to a null BIO. There is no command-line selector; standalone GENERAL_NAME DER does not reach the selected harness path.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
