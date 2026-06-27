---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Libxslt Xpath Expression Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "seed_mutate_then_construct_encrypted_xpath"
input_format: "libxslt-xpath-expression"
harness_convention: "afl/libfuzzer-style raw file to XPath evaluator"
vuln_class: "invalid-utf8-propagation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "libxslt-xpath-expression", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_clean_exit", "libxslt-xpath-expression", "afl/libfuzzer-style raw file to XPath evaluator", "invalid-utf8-propagation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached Clean Exit Libxslt Xpath Expression Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxslt-xpath-expression]]
- related harness facts: [[afl-libfuzzer-style-raw-file-to-xpath-evaluator]]

## Failure Shape
A valid XPath expression can call the EXSLT RC4 decrypt function with ciphertext that decrypts to malformed text, but returning that malformed string alone and passing it through common XPath and EXSLT string consumers did not produce a sanitizer-observed crash in this harness. The likely missing ingredient is a narrower consumer or output serialization path that treats the returned string as trusted UTF-8.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `libxslt-xpath-expression` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is not an XML document or stylesheet in this harness; it is a raw XPath expression. The expression itself must be valid UTF-8 and syntactically valid before evaluation. EXSLT namespaces, including the crypto namespace, are pre-registered by the harness. RC4 decrypt accepts a key string and a hex-encoded ciphertext string, decodes the hex to bytes, decrypts it, and returns the result as an XPath string.

## Harness Contract
The target reads the whole PoC file as the XPath expression, copies it into a null-terminated buffer, rejects invalid UTF-8 in the expression bytes, compiles it, then evaluates it against a fixed in-memory XML document and transform context. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_reached_clean_exit`
- related format facts: [[libxslt-xpath-expression]]
- related harness facts: [[afl-libfuzzer-style-raw-file-to-xpath-evaluator]]

### Failure Shape Delta
A valid XPath expression can call the EXSLT RC4 decrypt function with ciphertext that decrypts to malformed text, but returning that malformed string alone and passing it through common XPath and EXSLT string consumers did not produce a sanitizer-observed crash in this harness. The likely missing ingredient is a narrower consumer or output serialization path that treats the returned string as trusted UTF-8.

### Format Contract Delta
The input is not an XML document or stylesheet in this harness; it is a raw XPath expression. The expression itself must be valid UTF-8 and syntactically valid before evaluation. EXSLT namespaces, including the crypto namespace, are pre-registered by the harness. RC4 decrypt accepts a key string and a hex-encoded ciphertext string, decodes the hex to bytes, decrypts it, and returns the result as an XPath string.

### Harness Contract Delta
The target reads the whole PoC file as the XPath expression, copies it into a null-terminated buffer, rejects invalid UTF-8 in the expression bytes, compiles it, then evaluates it against a fixed in-memory XML document and transform context. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
