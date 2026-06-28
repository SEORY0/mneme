---
type: causal-policy
title: "No Crash Parser Reached Clean Or Rejected Trace Perfetto Trace Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_reached_clean_or_rejected_trace."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_or_rejected_trace"
candidate_family: "construct"
input_format: "perfetto-trace"
harness_convention: "libfuzzer"
vuln_class: "logic-regression"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-or-rejected-trace", "perfetto-trace", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_reached_clean_or_rejected_trace", "perfetto-trace", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Reached Clean Or Rejected Trace Perfetto Trace Negative Memory

## Policy
Treat `no_crash x parser_reached_clean_or_rejected_trace` as a persistent failure basin for `perfetto-trace` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Tiny protobuf-like packets, JSON-shaped data, compressed-stream magic, and empty input all parsed or rejected cleanly. The described generated-proto stale-file regression does not expose an obvious crash through the trace-processor parsing harness without a more specific generated trace packet.

## Format and Harness Gates
- Format: The trace processor expects raw Perfetto trace bytes, typically protobuf-framed trace packets. Invalid protobuf envelopes are accepted as fuzz input but are ignored or rejected without surfacing sanitizer findings.
- Harness: The libFuzzer target copies the entire input into an owned buffer, calls TraceProcessorStorage.Parse once, and then calls NotifyEndOfFile only when parsing reports success. There is no leading mode byte and no FuzzedDataProvider layout.

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
