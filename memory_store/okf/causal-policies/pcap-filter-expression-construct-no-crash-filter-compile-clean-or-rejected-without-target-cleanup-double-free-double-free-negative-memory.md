---
type: negative-memory
title: "Pcap Filter Expression Construct No Crash Filter Compile Clean Or Rejected Without Target Cleanup Double Free Double Free Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal filter_compile_clean_or_rejected_without_target_cleanup_double_free."
failure_class: "no_crash"
verifier_signal: "filter_compile_clean_or_rejected_without_target_cleanup_double_free"
candidate_family: "construct"
input_format: "pcap-filter-expression"
harness_convention: "afl-libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "filter-compile-clean-or-rejected-without-target-cleanup-double-free", "pcap-filter-expression", "afl-libfuzzer", "construct", "double-free", "negative-memory", "round-33"]
match_keys: ["no_crash", "filter_compile_clean_or_rejected_without_target_cleanup_double_free", "pcap-filter-expression", "afl-libfuzzer", "construct", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Pcap Filter Expression Construct No Crash Filter Compile Clean Or Rejected Without Target Cleanup Double Free Double Free Negative Memory

- key: `no_crash x filter_compile_clean_or_rejected_without_target_cleanup_double_free`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pcap-filter-expression]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
The reachable double-free appears tied to allocation-failure arms in the optimizer initialization path: those arms manually free optimizer arrays and then long-jump into the shared cleanup. Small arithmetic and value-propagation expressions exited cleanly or were rejected before the target cleanup path. Large disjunctions did reach the optimizer, but the reproducible crash was a recursive optimizer stack overflow that also crashed the fixed image, so it was over-broad and off-target. Larger balanced, arithmetic-heavy, and unique-offset pressure shapes did not produce a sanitizer signal before clean exit or timeout-like behavior.

## Policy
Treat `no_crash x filter_compile_clean_or_rejected_without_target_cleanup_double_free` on `pcap-filter-expression` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `filter_compile_clean_or_rejected_without_target_cleanup_double_free`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `filter_compile_clean_or_rejected_without_target_cleanup_double_free`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pcap-filter-expression]]. The input is a textual libpcap filter expression followed by a datalink selector byte. The filter text is copied into a NUL-terminated string before compilation. Ordinary predicates such as packet-byte comparisons, Boolean disjunctions, and arithmetic expressions can reach pcap_compile when paired with a compatible datalink value, but syntax or generation errors are swallowed by the harness as clean exits.

## Harness Contract
Use [[afl-libfuzzer]]. The active fuzz target reads raw bytes, uses the final byte as the datalink type for pcap_open_dead with a fixed snap length, copies all bytes into the filter buffer, terminates the filter at the final byte, and invokes pcap_compile with optimization enabled. There is no pcap file envelope, no packet records, no mode prefix, and no FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 17 attempts.
- Scope: generator repair and basin avoidance only.
