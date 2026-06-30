---
type: causal-policy
title: "No Crash Clean Exit Pdf Encrypt Dictionary Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "pdf-encrypt-dictionary"
harness_convention: "libfuzzer-ghostscript-stdin"
vuln_class: "encryption-parameter-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "pdf-encrypt-dictionary", "negative-memory", "round-7"]
match_keys: ["no_crash", "clean_exit", "pdf-encrypt-dictionary", "libfuzzer-ghostscript-stdin", "encryption-parameter-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Clean Exit Pdf Encrypt Dictionary Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-encrypt-dictionary]]
- related harness facts: [[libfuzzer-ghostscript-stdin]]

## Failure Shape
Generic PostScript and unencryped PDF inputs stayed clean. Minimal PDFs with xref/trailer wiring and
Encrypt dictionaries across several Standard security-handler versions also stayed clean, suggesting
the missing trigger is not just the presence of an invalid Length value but a later encrypted-
object/decryption path that consumes the derived key length.

## Policy
Treat `no_crash x clean_exit` on `pdf-encrypt-dictionary` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
A PDF Encrypt dictionary is reached from the trailer and must include the Standard filter plus
version, revision, permissions, owner/user strings, and for newer revisions stream/string filter and
crypt-filter dictionaries. The Length entry is meaningful only for specific encryption variants and
must satisfy range and granularity constraints.

## Harness Contract
The harness feeds raw stdin to Ghostscript configured for the CUPS raster device. It does not carve
a prefix from the input; Ghostscript auto-detects PostScript or PDF and processes the document
through its normal interpreter.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

## Round 27 Reinforcement
- key: `no_crash x pdf_parsed_clean_or_password_rejected`
- Seed mutations reached qpdf's PDF parsing and encrypted-file handling but did not produce an invalid AES key length.
- V4 AES inputs normalize the encryption key to a valid AES width before object decryption, and crypt-filter length fields did not affect the key bytes passed to Pl_AES_PDF.
- V5 encrypted-file paths recovered a full-width file key or rejected the file before stream decryption.
