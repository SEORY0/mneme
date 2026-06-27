---
type: causal-policy
title: "No Crash Parser Reached Or Clean Reject DER Ecdsa Signature Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal parser_reached_or_clean_reject."
failure_class: "no_crash"
verifier_signal: "parser_reached_or_clean_reject"
candidate_family: "construct"
input_format: "der-ecdsa-signature"
harness_convention: "libfuzzer-opensc-asn1-sig-value"
vuln_class: "asn1-ecdsa-signature-parsing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-or-clean-reject", "der-ecdsa-signature", "negative-memory", "round-20"]
match_keys: ["no-crash", "parser-reached-or-clean-reject", "der-ecdsa-signature"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Parser Reached Or Clean Reject DER Ecdsa Signature Negative Memory

- key: `no_crash x parser_reached_or_clean_reject`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[der-ecdsa-signature]]
- harnesses: [[libfuzzer-opensc-asn1-sig-value]]

## Dead End
The round 20 attempts for `der-ecdsa-signature` under `libfuzzer-opensc-asn1-sig-value` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Well-formed and malformed DER ECDSA signatures were either converted cleanly or rejected cleanly. Oversized, zero-length, negative, indefinite, truncated, and wrong-tag integer hypotheses did not violate the converter's output-size checks under this harness.

## Negative Policy
When retrieval matches `no_crash x parser_reached_or_clean_reject`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[der-ecdsa-signature]] and [[libfuzzer-opensc-asn1-sig-value]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
