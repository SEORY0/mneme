---
type: causal-policy
title: "No Crash Parser Executed Clean Pkcs12 Der Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_executed_clean."
failure_class: "no_crash"
verifier_signal: "parser_executed_clean"
candidate_family: "seed_mutate"
input_format: "pkcs12-der"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-executed-clean", "pkcs12-der", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_executed_clean", "pkcs12-der", "libfuzzer", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Executed Clean Pkcs12 Der Negative Memory

- key: `no_crash x parser_executed_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pkcs12-der]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid in-repo PKCS#12 containers reached the parser but did not create the specific cleanup state
where an already deinitialized key, certificate, or CRL output remains non-null and is deinitialized
again. Broad seed changes stayed in clean parse or clean error paths.

## Policy
Treat `no_crash x parser_executed_clean` on `pkcs12-der` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_executed_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
PKCS#12 DER inputs are ASN.1 containers holding authenticated safe bags. The target parser imports
the whole DER blob, verifies or ignores the MAC, decrypts encrypted bags with the harness password,
then searches bags for a private key, matching certificate chain, extra certificates, and optional
CRL.

## Harness Contract
The libFuzzer target feeds raw bytes as a DER PKCS#12 blob to the key parser fuzzer. The harness
uses a fixed password, calls simple_parse with output pointers for key, chain, extras, and CRL, and
manually deinitializes returned objects only when simple_parse reports success.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
