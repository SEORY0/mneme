---
type: negative-memory
title: "No Crash Usage Banner Or Clean Exit Openthread Cli Uart Or Ip6 Message Construct Buffer Overflow Write Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal usage_banner_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "usage_banner_or_clean_exit"
candidate_family: "construct"
input_format: "openthread-cli-uart-or-ip6-message"
harness_convention: "honggfuzz-file"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "usage-banner-or-clean-exit", "openthread-cli-uart-or-ip6-message", "honggfuzz-file", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "usage_banner_or_clean_exit", "openthread-cli-uart-or-ip6-message", "honggfuzz-file", "buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Usage Banner Or Clean Exit Openthread Cli Uart Or Ip6 Message Construct Buffer Overflow Write Negative Memory

- key: `no_crash x usage_banner_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-cli-uart-or-ip6-message]]
- related harness facts: [[honggfuzz-file]]

## Failure Shape
CLI command sequences and a raw IP6/CoAP-shaped packet did not trigger AppendUintOption. The observed target banner indicates the active harness is the CLI UART fuzzer; the missing relation is a command path that causes a CoAP message to append a uint option with the vulnerable length/header relationship inside the simulated instance.

## Policy
Treat `no_crash x usage_banner_or_clean_exit` on `openthread-cli-uart-or-ip6-message` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `usage_banner_or_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `usage_banner_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
OpenThread CLI input is textual UART command data. CoAP commands can start the service, register resources, set resource content, and send requests with URI, type, payload, and blockwise options. The vulnerable helper encodes uint options by trimming leading zero bytes before appending an option header and value.

## Harness Contract
The active target accepts a whole file as UART bytes for cli-uart-received-fuzzer under a honggfuzz-style wrapper. It initializes an OpenThread instance, passes copied bytes to the UART receive hook, then processes tasklets. There is no FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 4 attempts.
- Scope: generator repair and basin avoidance only.
