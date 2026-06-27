---
type: causal-policy
title: "No Crash Libxslt Xpath Expression Parser Reached Clean Exit Negative Memory"
description: "Negative memory for no_crash with parser_reached_clean_exit on libxslt-xpath-expression inputs."
failure_class: no_crash
verifier_signal: parser_reached_clean_exit
candidate_family: seed_mutate_then_construct_encrypted_xpath
input_format: libxslt-xpath-expression
harness_convention: "afl/libfuzzer-style raw file to XPath evaluator"
vuln_class: invalid-utf8-propagation
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-clean-exit, libxslt-xpath-expression, invalid-utf8-propagation, negative_memory]
match_keys: [no-crash, parser-reached-clean-exit, libxslt-xpath-expression, invalid-utf8-propagation]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Libxslt Xpath Expression Parser Reached Clean Exit Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[libxslt-xpath-expression]]

## Dead End
A valid XPath expression can call the EXSLT RC4 decrypt function with ciphertext that decrypts to malformed text, but returning that malformed string alone and passing it through common XPath and EXSLT string consumers did not produce a sanitizer-observed crash in this harness. The likely missing ingredient is a narrower consumer or output serialization path that treats the returned string as trusted UTF-8.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
