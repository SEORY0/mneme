---
type: format
title: "Libxslt Xpath Expression"
access_scope: generate
confidence: medium
tags: ["libxslt-xpath-expression", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
okf_support: 1
---
# Libxslt Xpath Expression

## Round 13 Facts
- The input is not an XML document or stylesheet in this harness; it is a raw XPath expression. The expression itself must be valid UTF-8 and syntactically valid before evaluation. EXSLT namespaces, including the crypto namespace, are pre-registered by the harness. RC4 decrypt accepts a key string and a hex-encoded ciphertext string, decodes the hex to bytes, decrypts it, and returns the result as an XPath string.

## Round 33 Factual Contract

### Schema / Invariants
- The input format is a single XPath expression, not XML or XSLT. The expression bytes must themselves be valid UTF-8 and syntactically valid before evaluation. The crypto namespace is registered in the evaluation context. crypto:rc4_decrypt accepts a key string and a hex ciphertext string, pads the key to the implementation RC4 key length, decodes the hex to binary, decrypts it, NUL-terminates the result, and returns that raw byte string as an XPath string.

### Harness Links
- [[afl-libfuzzer-style-raw-file-to-xpath-evaluator]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
