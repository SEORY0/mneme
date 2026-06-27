---
type: causal-policy
title: "No Crash Haproxy Config Cfg Parser Reached Too Many Words Clean Exit Negative Memory"
description: "Negative memory for no_crash with cfg_parser_reached_too_many_words_clean_exit on haproxy-config inputs."
failure_class: no_crash
verifier_signal: cfg_parser_reached_too_many_words_clean_exit
candidate_family: construct
input_format: haproxy-config
harness_convention: libfuzzer-raw-config-file
vuln_class: out-of-bounds-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, cfg-parser-reached-too-many-words-clean-exit, haproxy-config, out-of-bounds-read, negative_memory]
match_keys: [no-crash, cfg-parser-reached-too-many-words-clean-exit, haproxy-config, out-of-bounds-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Haproxy Config Cfg Parser Reached Too Many Words Clean Exit Negative Memory

- key: `no_crash x cfg_parser_reached_too_many_words_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[haproxy-config]]

## Dead End
A blank line followed by many bare arguments reached the argument-counting warning path and cleanly reported too many words. Attempts to use config-level environment expansion were blocked because this stripped harness reported section keywords as out of section, so it did not establish the virtual-argument expansion state needed for the described pointer trust issue.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
