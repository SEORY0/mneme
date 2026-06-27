---
type: harness
title: "Afl Libfuzzer Style Raw File To Xpath Evaluator"
harness_convention: "afl/libfuzzer-style raw file to XPath evaluator"
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Afl Libfuzzer Style Raw File To Xpath Evaluator

## Input Contract
- For `libxslt-xpath-expression`, The target reads the whole PoC file as the XPath expression, copies it into a null-terminated buffer, rejects invalid UTF-8 in the expression bytes, compiles it, then evaluates it against a fixed in-memory XML document and transform context. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving.
