---
type: "negative-memory"
title: "Lua Source Construct No Crash Parser Reached Clean Exit Or Lua Error Without Native Fault Tailcall Callframe Invariant Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_reached_clean_exit_or_lua_error_without_native_fault."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit_or_lua_error_without_native_fault"
candidate_family: "construct"
input_format: "lua-source"
harness_convention: "libfuzzer"
vuln_class: "tailcall-callframe-invariant"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-reached-clean-exit-or-lua-error-without-native-fault", "lua-source", "libfuzzer", "construct", "tailcall-callframe-invariant", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_reached_clean_exit_or_lua_error_without_native_fault", "lua-source", "libfuzzer", "tailcall-callframe-invariant", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Lua Source Construct No Crash Parser Reached Clean Exit Or Lua Error Without Native Fault Tailcall Callframe Invariant Negative Memory

- key: `no_crash x parser_reached_clean_exit_or_lua_error_without_native_fault`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[lua-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Text chunks reached the Lua loader and executor, but the harness does not open standard libraries, so C-library, metatable, coroutine, and debug-assisted tail-call paths were not reachable. Pure Lua variants covering direct tail recursion, vararg recursion, changing vararg frames, upvalue-closing tail calls, multi-result returns, and maximum legal parameter frames exited cleanly or were rejected by language register limits without sanitizer output.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_reached_clean_exit_or_lua_error_without_native_fault` on `[[lua-source]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_clean_exit_or_lua_error_without_native_fault` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit_or_lua_error_without_native_fault`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 12 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
