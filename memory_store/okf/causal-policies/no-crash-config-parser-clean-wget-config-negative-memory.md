---
type: causal-policy
title: "No Crash Config Parser Clean Wget Config Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal config_parser_clean."
failure_class: "no_crash"
verifier_signal: "config_parser_clean"
candidate_family: "seed_mutate"
input_format: "wget-config"
harness_convention: "afl-file"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "config-parser-clean", "wget-config", "negative_memory", "round-8"]
match_keys: ["no_crash", "config_parser_clean", "wget-config", "afl-file", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Config Parser Clean Wget Config Negative Memory

## Policy
Treat `no_crash x config_parser_clean` as a persistent failure basin for `wget-config` under `afl-file`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Config-line and corpus-seed variants exercised the options fuzzer without reaching a reproducing gnulib glob lifetime bug. Include directives with tilde, wildcard, malformed separator, and recursive-config forms remained clean under the harness.

## Format and Harness Gates
- Format: The input is a wget2 configuration file, not a URL. The parser accepts directive/value records with several separators; include directives may route path strings through glob expansion and tilde handling.
- Harness: The harness intercepts one fixed config filename and serves the raw fuzz bytes through an in-memory FILE object. It caps input size, disables real filesystem writes, disables normal config loading, and starts wget2 with a command-line option pointing at the intercepted config.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
