---
type: causal-policy
title: "No Crash Runtime Error Or Timeout Without Target Crash Lua Source Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal runtime_error_or_timeout_without_target_crash."
failure_class: "no_crash"
verifier_signal: "runtime_error_or_timeout_without_target_crash"
candidate_family: "construct"
input_format: "lua-source"
harness_convention: "libfuzzer"
vuln_class: "invalid-stack-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "runtime-error-or-timeout-without-target-crash", "lua-source", "negative_memory", "round-8"]
match_keys: ["no_crash", "runtime_error_or_timeout_without_target_crash", "lua-source", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Runtime Error Or Timeout Without Target Crash Lua Source Negative Memory

## Policy
Treat `no_crash x runtime_error_or_timeout_without_target_crash` as a persistent failure basin for `lua-source` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Scripts aimed at finalizers and deep call behavior did not reach the target because the harness does not open the standard libraries, so global helpers for metatables and unpacking are unavailable, and a recursive stress case did not produce the desired differential crash.

## Format and Harness Gates
- Format: The input is text-mode Lua source. Code can define local functions, tables, closures, expressions, and chunks, but standard-library helpers are absent unless provided by the core VM itself.
- Harness: The libFuzzer target creates a fresh Lua state without opening libraries, loads the raw bytes as text-only Lua source, executes the chunk if loading succeeds, then closes the state. No filename or binary chunk mode is available.

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
