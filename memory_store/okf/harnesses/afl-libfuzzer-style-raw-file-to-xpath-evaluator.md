---
type: harness
title: "Afl Libfuzzer Style Raw File To Xpath Evaluator"
access_scope: generate
confidence: medium
tags: ["afl-libfuzzer-style-raw-file-to-xpath-evaluator", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
okf_support: 1
---
# Afl Libfuzzer Style Raw File To Xpath Evaluator

## Round 13 Facts
- The target reads the whole PoC file as the XPath expression, copies it into a null-terminated buffer, rejects invalid UTF-8 in the expression bytes, compiles it, then evaluates it against a fixed in-memory XML document and transform context. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving.

## Round 33 Input Contract

### Input Contract
- The harness reads the whole file as the XPath expression, copies it to a NUL-terminated buffer, rejects invalid UTF-8 in the expression bytes before compiling, then evaluates against a fixed in-memory XML document and transform context. There is no leading mode byte, checksum, length envelope, or FuzzedDataProvider carving. The local image wrapper runs the XPath fuzz target, so returned XPath objects are freed after evaluation rather than serialized as XSLT output.

### Format Links
- [[libxslt-xpath-expression]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
