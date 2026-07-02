---
type: causal-policy
title: "Wget Config Construct Wrong Sink Parser Reached Glob Use After Free Heap Use After Free Verified Recovery"
description: "Round 34 verified recovery for wget-config when wrong_sink pairs with parser_reached_glob_use_after_free."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_glob_use_after_free"
candidate_family: "construct"
input_format: "wget-config"
harness_convention: "honggfuzz-file"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-glob-use-after-free", "wget-config", "honggfuzz-file", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-glob-use-after-free", "wget-config", "honggfuzz-file", "construct", "heap-use-after-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Wget Config Construct Wrong Sink Parser Reached Glob Use After Free Heap Use After Free Verified Recovery

- key: `wrong_sink x parser_reached_glob_use_after_free`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[wget-config]]
- related harness facts: [[honggfuzz-file]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_glob_use_after_free`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-use-after-free`
- related format facts: [[wget-config]]
- related harness facts: [[honggfuzz-file]]

### Policy
When `wrong_sink x parser_reached_glob_use_after_free` appears for `wget-config`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[honggfuzz-file]] harness contract and the [[wget-config]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use a wget2 config include directive so the option parser sends the value through gnulib glob with tilde expansion and directory marking enabled. The triggering path expands an existing user's home directory and uses redundant directory separators plus a current-directory component, causing glob to keep using an expanded directory buffer after it has been freed during result marking/prefix handling.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is a wget2 configuration file made of directive/value records. The parser accepts directive values after whitespace, equals, or comma separators. Include directives recurse through read_config_expand and call glob with tilde expansion and directory marking; several filename-valued options can also invoke shell-style tilde expansion, but broad filename-option variants were clean here.

### Harness Contract
The options fuzzer treats the raw file bytes as the contents of one intercepted config file served through an in-memory FILE object. It caps input size, disables writes, suppresses normal config loading, and starts wget2 with a fixed command-line config argument. Filesystem directory enumeration is constrained by the harness, so reaching glob depends on config parsing rather than writing auxiliary files.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_glob_use_after_free`.
- Vulnerability class: `heap-use-after-free`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
