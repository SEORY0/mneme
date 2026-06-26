---
type: causal-policy
title: No Crash Parser Reached Without State Failure Negative Memory
description: Negative memory for no_crash with verifier signal parser_reached_without_state_failure.
failure_class: no_crash
verifier_signal: parser_reached_without_state_failure
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-without-state-failure, negative_memory]
match_keys: [no-crash, parser-reached-without-state-failure, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Reached Without State Failure Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x parser_reached_without_state_failure`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: chunked-http-stream-with-proxy-protocol-prefix

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- A stream containing repeated valid PROXY prefixes and HTTP requests reached the HTTP parser but did not trigger the target state bug. The remaining likely requirement is a more precise chunk-boundary or request-reuse sequence that makes header parsing revisit the PROXY bytes during a later getHeaders call.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
