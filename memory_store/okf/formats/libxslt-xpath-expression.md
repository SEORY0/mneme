---
type: format
title: "Libxslt Xpath Expression"
access_scope: generate
confidence: medium
tags: ["libxslt-xpath-expression", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libxslt Xpath Expression

## Round 13 Facts
- The input is not an XML document or stylesheet in this harness; it is a raw XPath expression. The expression itself must be valid UTF-8 and syntactically valid before evaluation. EXSLT namespaces, including the crypto namespace, are pre-registered by the harness. RC4 decrypt accepts a key string and a hex-encoded ciphertext string, decodes the hex to bytes, decrypts it, and returns the result as an XPath string.
