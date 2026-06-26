---
type: causal-policy
title: No Crash Parser Not Reached Or No Target Crash Negative Memory
description: Negative memory for no_crash with verifier signal parser_not_reached_or_no_target_crash.
failure_class: no_crash
verifier_signal: parser_not_reached_or_no_target_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached-or-no-target-crash, negative_memory]
match_keys: [no-crash, parser-not-reached-or-no-target-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Not Reached Or No Target Crash Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x parser_not_reached_or_no_target_crash`
- outcome: persistent failure basin
- support_count: 2
- candidate_families: construct
- observed_formats: ac3, ipv4-tcp-tls

### Procedure
Treat this as an envelope or harness-shape failure. Rebuild the carrier around the exact fuzzer input contract, confirm parser reachability, then add one target invariant.

### Diagnosed Dead Ends
- The active target is the AC3 decoder fuzzer. A syncword-framed AC3-like packet was accepted by the harness but did not reach the coupling band-structure corner case. The remaining missing gate is a valid enough AC3/EAC3 bitstream that enables coupling and supplies inconsistent band-structure state without being rejected earlier.
- The active nDPI fuzzer expects whole packets, not a raw TLS record. Wrapping malformed ClientHello extension data in a minimal IPv4/TCP packet still produced no parser-reached evidence. The remaining missing gate is likely flow-state or packet-shape context that causes nDPI to dispatch into the TLS dissector before the malformed extension bounds are evaluated.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
