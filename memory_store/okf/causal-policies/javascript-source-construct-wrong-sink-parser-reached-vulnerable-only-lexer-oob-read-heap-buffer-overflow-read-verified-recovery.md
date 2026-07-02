---
type: causal-policy
title: "Javascript Source Construct Wrong Sink Parser Reached Vulnerable Only Lexer Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for javascript-source when wrong_sink pairs with parser_reached_vulnerable_only_lexer_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vulnerable_only_lexer_oob_read"
candidate_family: "construct"
input_format: "javascript-source"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-vulnerable-only-lexer-oob-read", "javascript-source", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-vulnerable-only-lexer-oob-read", "javascript-source", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Javascript Source Construct Wrong Sink Parser Reached Vulnerable Only Lexer Oob Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_vulnerable_only_lexer_oob_read`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[javascript-source]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_vulnerable_only_lexer_oob_read`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[javascript-source]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_vulnerable_only_lexer_oob_read` appears for `javascript-source`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[javascript-source]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use raw script text that reaches tokenization and ends immediately after a token prefix whose lexer path expects an optional continuation character. The parser accepts the token prefix, then the multi-token helper probes past the end of the input while deciding whether a longer operator is present; the fixed build rejects the end-of-buffer condition cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is plain JavaScript source text with no container header, length field, checksum, or trailing selector. Punctuation-style operator tokens are consumed directly by the lexer, and some operator prefixes are resolved by a helper that checks whether a continuation character follows.

### Harness Contract
libFuzzer supplies the raw byte slice directly as the script source. Empty inputs are ignored; otherwise the harness creates an interpreter context, processes the script, and does not carve mode bytes or use FuzzedDataProvider.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_vulnerable_only_lexer_oob_read`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
