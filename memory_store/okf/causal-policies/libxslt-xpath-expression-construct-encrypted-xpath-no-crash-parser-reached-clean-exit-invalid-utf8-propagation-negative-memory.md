---
type: negative-memory
title: "Libxslt Xpath Expression Construct Encrypted Xpath No Crash Parser Reached Clean Exit Invalid Utf8 Propagation Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct-encrypted-xpath"
input_format: "libxslt-xpath-expression"
harness_convention: "afl-libfuzzer-style-raw-file-to-xpath-evaluator"
vuln_class: "invalid-utf8-propagation"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "libxslt-xpath-expression", "afl-libfuzzer-style-raw-file-to-xpath-evaluator", "construct-encrypted-xpath", "invalid-utf8-propagation", "negative-memory", "round-33"]
match_keys: ["no_crash", "parser_reached_clean_exit", "libxslt-xpath-expression", "afl-libfuzzer-style-raw-file-to-xpath-evaluator", "construct-encrypted-xpath", "invalid-utf8-propagation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Libxslt Xpath Expression Construct Encrypted Xpath No Crash Parser Reached Clean Exit Invalid Utf8 Propagation Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxslt-xpath-expression]]
- related harness facts: [[afl-libfuzzer-style-raw-file-to-xpath-evaluator]]

## Failure Shape
A valid ASCII XPath expression can drive EXSLT crypto:rc4_decrypt with a printable key and hex ciphertext so the decrypted return value is malformed text, but the XPath target exited cleanly. Direct return, XPath string built-ins, EXSLT string/date/math consumers, dynamic expression compilation, QName/URI consumers, and a format-number pattern sink all failed to turn the malformed returned string into a sanitizer-observed vulnerable-image crash. The likely missing condition is a narrower in-evaluator consumer or a result-serialization path not exercised by this fixed XPath harness entry point.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `libxslt-xpath-expression` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `parser_reached_clean_exit`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[libxslt-xpath-expression]]. The input format is a single XPath expression, not XML or XSLT. The expression bytes must themselves be valid UTF-8 and syntactically valid before evaluation. The crypto namespace is registered in the evaluation context. crypto:rc4_decrypt accepts a key string and a hex ciphertext string, pads the key to the implementation RC4 key length, decodes the hex to binary, decrypts it, NUL-terminates the result, and returns that raw byte string as an XPath string.

## Harness Contract
Use [[afl-libfuzzer-style-raw-file-to-xpath-evaluator]]. The harness reads the whole file as the XPath expression, copies it to a NUL-terminated buffer, rejects invalid UTF-8 in the expression bytes before compiling, then evaluates against a fixed in-memory XML document and transform context. There is no leading mode byte, checksum, length envelope, or FuzzedDataProvider carving. The local image wrapper runs the XPath fuzz target, so returned XPath objects are freed after evaluation rather than serialized as XSLT output.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 98 attempts.
- Scope: generator repair and basin avoidance only.
