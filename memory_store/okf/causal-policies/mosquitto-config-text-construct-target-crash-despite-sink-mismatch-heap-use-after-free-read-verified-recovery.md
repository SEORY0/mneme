---
type: causal-policy
title: "Mosquitto Config Text Construct Target Crash Despite Sink Mismatch Heap Use After Free Read Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal target_crash_despite_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "target_crash_despite_sink_mismatch"
candidate_family: "construct"
input_format: "mosquitto-config-text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-crash-despite-sink-mismatch", "mosquitto-config-text", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "target_crash_despite_sink_mismatch", "mosquitto-config-text", "libfuzzer", "heap-use-after-free-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Mosquitto Config Text Construct Target Crash Despite Sink Mismatch Heap Use After Free Read Verified Recovery

- key: `wrong_sink x target_crash_despite_sink_mismatch`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[mosquitto-config-text]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `mosquitto-config-text` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `target_crash_despite_sink_mismatch` on `mosquitto-config-text` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Create a default listener through a default-listener directive, then append an explicit listener so the listener array is reallocated, then use another default-listener directive that touches the stale default-listener pointer. The parser must process directives sequentially in a single config.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
Mosquitto config is newline-separated directive text. Default listener directives create or modify the implicit listener, while listener directives append explicit listeners. Later directives operate on the parser state established by earlier lines.

## Harness Contract
The libFuzzer input is written directly to a temporary Mosquitto configuration file and checked with broker test-config mode. Although the task metadata suggested an archive-like format, the active harness consumes raw config text with no wrapper.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
