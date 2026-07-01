---
type: causal-policy
title: "Php Script Construct Generic Crash Parser Reached Zend Lex Tstring Shorthand Echo Identifier Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_zend_lex_tstring_shorthand_echo_identifier."
failure_class: "generic_crash"
verifier_signal: "parser_reached_zend_lex_tstring_shorthand_echo_identifier"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "honggfuzz-libfuzzer-php-parser-raw-source"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct", "php-script", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-zend-lex-tstring-shorthand-echo-identifier", "php-script", "honggfuzz-libfuzzer-php-parser-raw-source", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Php Script Construct Generic Crash Parser Reached Zend Lex Tstring Shorthand Echo Identifier Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_zend_lex_tstring_shorthand_echo_identifier` on `php-script` under `honggfuzz-libfuzzer-php-parser-raw-source`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Construct ordinary PHP source containing a class trait-adaptation block.
2. End one valid trait alias using a PHP close tag as the grammar semicolon, then immediately reopen with the shorthand echo open tag while the parser is still ready for another trait method reference.
3. The shorthand-generated echo token has no identifier span, but the vulnerable semi-reserved identifier reduction passes it to zend_lex_tstring, causing an out-of-bounds read; the fixed build rejects that token as an identifier.

## Format Contract
- Input format: [[php-script]].
- Harness contract: [[honggfuzz-libfuzzer-php-parser-raw-source]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `php-script` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
