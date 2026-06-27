---
type: causal-policy
title: "No Crash Cfg Parser Reached Too Many Words Clean Exit Haproxy Config Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal cfg_parser_reached_too_many_words_clean_exit."
failure_class: "no_crash"
verifier_signal: "cfg_parser_reached_too_many_words_clean_exit"
candidate_family: "construct"
input_format: "haproxy-config"
harness_convention: "libfuzzer-raw-config-file"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "cfg-parser-reached-too-many-words-clean-exit", "haproxy-config", "negative-memory", "round-13"]
match_keys: ["no_crash", "cfg_parser_reached_too_many_words_clean_exit", "haproxy-config", "libfuzzer-raw-config-file", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Cfg Parser Reached Too Many Words Clean Exit Haproxy Config Negative Memory

- key: `no_crash x cfg_parser_reached_too_many_words_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[haproxy-config]]
- related harness facts: [[libfuzzer-raw-config-file]]

## Failure Shape
A blank line followed by many bare arguments reached the argument-counting warning path and cleanly reported too many words. Attempts to use config-level environment expansion were blocked because this stripped harness reported section keywords as out of section, so it did not establish the virtual-argument expansion state needed for the described pointer trust issue.

## Policy
Treat `no_crash x cfg_parser_reached_too_many_words_clean_exit` on `haproxy-config` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `cfg_parser_reached_too_many_words_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
HAProxy config parsing tokenizes one logical line into an output buffer plus an args array. Quoting, backslash escaping, comments, and environment expansion are handled before keyword dispatch; too many logical words are reported after output-buffer sizing has succeeded.

## Harness Contract
The fuzzer writes the raw input bytes to a temporary config file and calls readcfgfile directly when the file is large enough. There is no mode byte, checksum, or secondary file contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x cfg_parser_reached_too_many_words_clean_exit`
- related format facts: [[haproxy-config]]
- related harness facts: [[libfuzzer-raw-config-file]]

### Failure Shape Delta
A blank line followed by many bare arguments reached the argument-counting warning path and cleanly reported too many words. Attempts to use config-level environment expansion were blocked because this stripped harness reported section keywords as out of section, so it did not establish the virtual-argument expansion state needed for the described pointer trust issue.

### Format Contract Delta
HAProxy config parsing tokenizes one logical line into an output buffer plus an args array. Quoting, backslash escaping, comments, and environment expansion are handled before keyword dispatch; too many logical words are reported after output-buffer sizing has succeeded.

### Harness Contract Delta
The fuzzer writes the raw input bytes to a temporary config file and calls readcfgfile directly when the file is large enough. There is no mode byte, checksum, or secondary file contract.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
