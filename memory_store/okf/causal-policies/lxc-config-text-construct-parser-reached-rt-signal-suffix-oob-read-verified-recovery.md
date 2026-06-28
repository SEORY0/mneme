---
type: causal-policy
title: "Lxc Config Text Construct Parser Reached Rt Signal Suffix Oob Read Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_rt_signal_suffix_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_rt_signal_suffix_oob_read"
candidate_family: "construct"
input_format: "lxc-config-text"
harness_convention: "afl-libfuzzer-tempfile"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-rt-signal-suffix-oob-read", "construct", "lxc-config-text", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_rt_signal_suffix_oob_read", "lxc-config-text", "afl-libfuzzer-tempfile", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Lxc Config Text Construct Parser Reached Rt Signal Suffix Oob Read Verified Recovery

- key: `wrong_sink x parser_reached_rt_signal_suffix_oob_read`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[lxc-config-text]]
- harnesses: [[afl-libfuzzer-tempfile]]

## Failure Shape
The verifier-confirmed candidate preserved the `lxc-config-text` parser envelope under `afl-libfuzzer-tempfile` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_rt_signal_suffix_oob_read` on `lxc-config-text` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use a valid LXC signal configuration assignment and set the value to the realtime-signal prefix
without the expected min/max numeric suffix. The parser strips the signal prefixes and advances as
though the suffix exists before validating the next character, causing an out-of-bounds read.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
LXC configuration is line-oriented key/value text. Signal-related keys route their value through a
signal-name parser that recognizes ordinary signal names and realtime signal forms.

## Harness Contract
The fuzzer writes the raw input bytes to a temporary config file and calls the LXC config reader.
There is no outer binary envelope or checksum.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
