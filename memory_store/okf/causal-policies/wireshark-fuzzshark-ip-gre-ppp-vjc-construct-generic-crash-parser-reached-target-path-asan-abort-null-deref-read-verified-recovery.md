---
type: "causal-policy"
title: "Wireshark Fuzzshark Ip GRE PPP VJC Construct Generic Crash Parser Reached Target Path Asan Abort Null Deref Read Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_target_path_asan_abort."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_path_asan_abort"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-ip-gre-ppp-vjc"
harness_convention: "afl-libfuzzer-compatible-fuzzshark-ip"
vuln_class: "null-deref-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-target-path-asan-abort", "wireshark-fuzzshark-ip-gre-ppp-vjc", "afl-libfuzzer-compatible-fuzzshark-ip", "construct", "null-deref-read", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_target_path_asan_abort", "wireshark-fuzzshark-ip-gre-ppp-vjc", "afl-libfuzzer-compatible-fuzzshark-ip", "null-deref-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Wireshark Fuzzshark Ip GRE PPP VJC Construct Generic Crash Parser Reached Target Path Asan Abort Null Deref Read Verified Recovery

- key: `generic_crash x parser_reached_target_path_asan_abort`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[wireshark-fuzzshark-ip-gre-ppp-vjc]]
- related harness facts: [[afl-libfuzzer-compatible-fuzzshark-ip]]

## Failure Shape
Use the fuzzshark IP contract: wrap the target bytes as a raw IPv4 packet that dispatches to GRE, then GRE protocol PPP, then PPP protocol VJ compressed TCP/IP. Keep the outer packet structurally acceptable and make the compressed VJ header internally plausible enough to pass the PPP/VJC handoff, but omit the prior VJ conversation state so the vulnerable compressed-path conversation lookup is reached with no saved connection. The fixed build rejects or guards that missing-state path cleanly.

## Policy
When `generic_crash x parser_reached_target_path_asan_abort` appears for `[[wireshark-fuzzshark-ip-gre-ppp-vjc]]` under `[[afl-libfuzzer-compatible-fuzzshark-ip]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[wireshark-fuzzshark-ip-gre-ppp-vjc]]` format contract and `[[afl-libfuzzer-compatible-fuzzshark-ip]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[wireshark-fuzzshark-ip-gre-ppp-vjc]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 43 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
