---
type: negative-memory
title: "No Crash Clean Exit Wpantund Fuzz Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "seed_mutate_ncp_state_and_truncated_spinel"
input_format: "wpantund-fuzz"
harness_convention: "afl-libfuzzer-file"
vuln_class: "use-of-uninitialized-memory"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "wpantund-fuzz", "afl-libfuzzer-file", "seed-mutate-ncp-state-and-truncated-spinel", "use-of-uninitialized-memory", "negative-memory", "round-28"]
match_keys: ["no_crash", "clean_exit", "wpantund-fuzz", "afl-libfuzzer-file", "use-of-uninitialized-memory", "negative_memory", "seed-mutate", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Clean Exit Wpantund Fuzz Negative Memory

- key: `no_crash x clean_exit`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[wpantund-fuzz]]
- harnesses: [[afl-libfuzzer-file]]

## Dead-End Shape
The top-level selector and HDLC/Spinel envelope were correct, and both bundled NCP seeds executed cleanly. Distinct probes covered off-mesh route add/remove, on-mesh prefix add/remove, address-table truncation, inserted/removed property variants, larger-seed state reuse, and scalar VALUE_IS truncations for properties whose handlers ignore unpack status. All remained clean, suggesting the missing gate is a more specific initialized NCP state, callback/task state, or property sequence rather than a standalone malformed frame.

## Policy
For `no_crash x clean_exit` on `wpantund-fuzz`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `seed_mutate_ncp_state_and_truncated_spinel` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[wpantund-fuzz]]: wpantund fuzz inputs begin with a one-byte mode selector. Config mode consumes raw configuration text after the selector. NCP mode consumes an HDLC-framed Spinel byte stream; frames are flag-delimited, escaped for flag/control bytes, and in this fuzz build carry trailing FCS bytes that are stripped without normal CRC validation. Spinel VALUE_IS, VALUE_INSERTED, and VALUE_REMOVED frames carry packed command and property identifiers followed by property-specific typed payloads.
- Harness [[afl-libfuzzer-file]]: The NCP-input harness creates a socketpair, configures wpantund to use one descriptor as the NCP socket, then writes remaining fuzz bytes one at a time through the other descriptor while pumping MainLoop. A special command byte in the byte stream can wait for outbound frames or fast-forward simulated time. The selector for NCP mode is required before any HDLC data; the control-interface selector is a stub.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
