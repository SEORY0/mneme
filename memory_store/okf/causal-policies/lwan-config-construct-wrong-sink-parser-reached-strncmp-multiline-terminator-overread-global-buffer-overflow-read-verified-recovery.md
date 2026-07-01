---
type: causal-policy
title: "Lwan Config Construct Wrong Sink Parser Reached Strncmp Multiline Terminator Overread Global Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for lwan-config when wrong_sink pairs with parser_reached_strncmp_multiline_terminator_overread."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_strncmp_multiline_terminator_overread"
candidate_family: "construct"
input_format: "lwan-config"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-strncmp-multiline-terminator-overread", "lwan-config", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-strncmp-multiline-terminator-overread", "lwan-config", "libfuzzer", "construct", "global-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Lwan Config Construct Wrong Sink Parser Reached Strncmp Multiline Terminator Overread Global Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_strncmp_multiline_terminator_overread`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[lwan-config]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_strncmp_multiline_terminator_overread`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `global-buffer-overflow-read`
- related format facts: [[lwan-config]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_strncmp_multiline_terminator_overread` appears for `lwan-config`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[lwan-config]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use the raw libFuzzer config input contract to enter the Lwan configuration lexer, open a multiline string, and avoid a full closing delimiter. Grow the input to the harness buffer boundary so the lexer reaches the multiline terminator check with only a delimiter prefix remaining; the vulnerable scanner compares a fixed-width terminator before proving enough bytes remain, while the fixed build rejects the boundary case.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
Lwan config text uses comments, ordinary strings, key-value lines with equals, brace-delimited sections, variable expansions, and triple-quoted multiline strings. Multiline strings are scanned until a matching three-character quote delimiter is found or EOF is reached.

### Harness Contract
The active libFuzzer target is the Lwan config fuzzer. It copies the raw input bytes into a fixed static buffer, clamps oversized inputs, opens the config parser over the copied bytes with one trailing byte excluded from the logical lexer range, recursively reads config lines, and uses no mode byte, checksum, or FuzzedDataProvider split.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_strncmp_multiline_terminator_overread`.
- Vulnerability class: `global-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
