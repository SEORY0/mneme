---
type: causal-policy
title: "Dhcpv4 Construct Parser Reached Confirmed Target Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached_confirmed_target."
failure_class: "generic_crash"
verifier_signal: "parser_reached_confirmed_target"
candidate_family: "construct"
input_format: "dhcpv4"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-confirmed-target", "construct", "dhcpv4", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached_confirmed_target", "dhcpv4", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Dhcpv4 Construct Parser Reached Confirmed Target Verified Recovery

- key: `generic_crash x parser_reached_confirmed_target`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[dhcpv4]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `dhcpv4` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached_confirmed_target` on `dhcpv4` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Construct a valid DHCPv4 packet header with the required magic and a valid message-type option, then
append a truncated duplicate of that option containing only the option code. The decoder recognizes
the first option, enters the consecutive-option coalescing path, and then attempts to inspect a
missing length byte for the trailing duplicate header.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
DHCPv4 uses a fixed BOOTP-style header followed by an option area. Normal options are tag-length-
value records, with special padding/end tags. The message-type option is required by this decoder
before full option parsing proceeds.

## Harness Contract
The FreeRADIUS fuzzer binary selects a protocol decoder from its target name; for this run the local
wrapper executed the DHCPv4 protocol decoder on the raw input buffer.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
