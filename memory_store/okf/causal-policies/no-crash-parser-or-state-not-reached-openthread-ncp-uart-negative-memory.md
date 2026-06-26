---
type: causal-policy
title: "No Crash Parser Or State Not Reached Openthread Ncp Uart Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_or_state_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_or_state_not_reached"
candidate_family: "hand_construct"
input_format: "openthread-ncp-uart"
harness_convention: "libfuzzer"
vuln_class: "bounds-check-missing-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-or-state-not-reached", "openthread-ncp-uart", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_or_state_not_reached", "openthread-ncp-uart", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Or State Not Reached Openthread Ncp Uart Negative Memory

## Policy
Treat `no_crash x parser_or_state_not_reached` as a persistent failure basin for `openthread-ncp-uart` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- A CLI-style network-data registration script did not drive the selected NCP UART harness into the network-data leader update path. The likely missing gate is Spinel-over-UART framing plus the exact property/update transaction that causes local network data to be registered with the leader.

## Format and Harness Gates
- Format: OpenThread NCP UART fuzzing expects a stream of NCP/Spinel UART bytes, not CLI text. The vulnerable logic compares encoded Thread network-data TLVs; each TLV has a type/stability discriminator, a length, and nested value/sub-TLV regions whose advertised lengths govern iteration.
- Harness: The selected libFuzzer target initializes an OpenThread instance as a leader, initializes the NCP, copies the raw input to a UART receive buffer, calls the platform UART receive hook once, and then drains tasklets/platform work for a bounded number of iterations.

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
