---
type: causal-policy
title: "X509 Der Certificate With General Name Seed Mutate Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for x509-der-certificate-with-general-name when wrong_sink pairs with parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "seed_mutate"
input_format: "x509-der-certificate-with-general-name"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "x509-der-certificate-with-general-name", "libfuzzer", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch", "x509-der-certificate-with-general-name", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# X509 Der Certificate With General Name Seed Mutate Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[x509-der-certificate-with-general-name]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached_sink_mismatch` appears for `x509-der-certificate-with-general-name`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `x509-der-certificate-with-general-name` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Seed-mutate a DER X.509 certificate that already reaches the X.509 fuzzer and contains a subjectAltName otherName using an OpenSSL-recognized otherName identifier whose printer expects a character-string ASN1_TYPE. Preserve the certificate, extension, GeneralNames, otherName wrapper, and all enclosing lengths; change only the explicitly tagged ANY value so it remains a valid ASN.1 object of a different primitive type that uses the ASN1_STRING container but is not the expected text type. This keeps extension decoding on the i2v_GENERAL_NAME path while the vulnerable printer treats the mismatched value as a NUL-terminated string.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[x509-der-certificate-with-general-name]]. The selected input is a DER X.509 certificate. X.509 extensions are carried as OCTET STRING-wrapped DER payloads. subjectAltName decodes as a sequence of GeneralName values. The otherName choice is context-tagged and contains an object identifier plus an explicitly tagged ASN1_ANY value. OpenSSL maps some recognized otherName identifiers to expected UTF8String or IA5String values during printing instead of checking the parsed ASN1_TYPE tag.

## Harness Contract
Use [[libfuzzer]]. The OpenSSL x509 libFuzzer harness consumes the entire PoC as raw DER for d2i_X509. If parsing succeeds, it prints the certificate, public key, and extensions to a null BIO, then serializes the certificate again. There is no in-band selector and standalone GENERAL_NAME DER does not reach this harness path.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `wrong_sink x parser_reached_sink_mismatch`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Seed-mutate a DER X.509 certificate that already reaches the X.509 fuzzer and contains a subjectAltName otherName using an OpenSSL-recognized otherName identifier whose printer expects a character-string ASN1_TYPE. Preserve the certificate, extension, GeneralNames, otherName wrapper, and all enclosing lengths; change only the explicitly tagged ANY value so it remains a valid ASN.1 object of a different primitive type that uses the ASN1_STRING container but is not the expected text type. This keeps extension decoding on the i2v_GENERAL_NAME path while the vulnerable printer treats the mismatched value as a NUL-terminated string.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
