---
type: causal-policy
title: "Wpantund Fuzz Construct Hdlc Spinel And Seed Mutate No Crash Clean Exit Use After Free Negative Memory"
description: "Negative memory for wpantund-fuzz candidates that ended in no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct-hdlc-spinel-and-seed-mutate"
input_format: "wpantund-fuzz"
harness_convention: "afl-libfuzzer-file"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "wpantund-fuzz", "afl-libfuzzer-file", "construct-hdlc-spinel-and-seed-mutate", "use-after-free", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit", "wpantund-fuzz", "afl-libfuzzer-file", "construct-hdlc-spinel-and-seed-mutate", "use-after-free", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Wpantund Fuzz Construct Hdlc Spinel And Seed Mutate No Crash Clean Exit Use After Free Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[wpantund-fuzz]]
- related harness facts: [[afl-libfuzzer-file]]

## Policy
Treat `no_crash x clean_exit` for `[[wpantund-fuzz]]` under `[[afl-libfuzzer-file]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: The harness envelope and Spinel frame structure were accepted well enough to execute cleanly, but the attempts did not produce a vulnerable-build crash in the on-mesh-prefix removal path. Distinct attempts covered direct complete-list replacement, preserving bundled NCP corpus state, explicit network state changes, explicit address-table state, inserted/removed event variants, inner-frame wait cadence matching the corpus, and reuse of the larger NCP seed before the target transition. The likely missing condition is a more specific wpantund internal state or callback/task relation, not the basic HDLC/Spinel encoding.
3. Rebuild around `[[wpantund-fuzz]]` and `[[afl-libfuzzer-file]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- wpantund-fuzz inputs begin with a one-byte mode selector. NCP mode consumes an HDLC-flag-delimited Spinel UART byte stream. Spinel property callbacks use a header byte, packed command id, packed property id, and property-specific typed payload. Thread on-mesh full-list updates carry repeated length-wrapped structs containing an IPv6 prefix, prefix length, stable flag, on-mesh flags, local-origin flag, and registering locator. Empty full-list updates are represented by the property callback with no entry payload.

## Harness Contract
- The AFL/libFuzzer wrapper reads the PoC as raw file bytes. The first byte selects config, NCP socket input, or a stubbed control-interface path. In NCP mode, the harness creates a socketpair, writes remaining bytes one at a time to the simulated NCP socket, and pumps the main loop after writes. A special byte in the stream is interpreted by the harness as a wait or time-fast-forward command and is not written to the NCP socket; bundled corpus frames often place this wait immediately after an HDLC frame flag.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 11.
