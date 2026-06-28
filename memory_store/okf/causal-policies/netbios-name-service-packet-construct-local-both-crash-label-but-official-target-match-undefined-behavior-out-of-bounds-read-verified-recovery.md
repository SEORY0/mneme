---
type: causal-policy
title: "Netbios Name Service Packet Construct Local Both Crash Label But Official Target Match Undefined Behavior Out Of Bounds Read Verified Recovery"
description: "Round 12 verified recovery for generic_crash with verifier signal local_both_crash_label_but_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_both_crash_label_but_official_target_match"
candidate_family: "construct"
input_format: "netbios-name-service-packet"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-both-crash-label-but-official-target-match", "netbios-name-service-packet", "verified-recovery", "round-12"]
match_keys: ["generic_crash", "local_both_crash_label_but_official_target_match", "netbios-name-service-packet", "libfuzzer", "undefined-behavior-out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Netbios Name Service Packet Construct Local Both Crash Label But Official Target Match Undefined Behavior Out Of Bounds Read Verified Recovery

- key: `generic_crash x local_both_crash_label_but_official_target_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[netbios-name-service-packet]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `netbios-name-service-packet` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `local_both_crash_label_but_official_target_match` on `netbios-name-service-packet` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a syntactically plausible NetBIOS name-service query so the name parser reaches compressed-name handling, then make a later name component consist of a compression pointer marker without its companion byte. The vulnerable build reads the missing low byte while the fixed build rejects the incomplete pointer before dereference.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The packet starts with a NetBIOS name-service header containing count fields. A question record contains an encoded NetBIOS name followed by type and class fields when parsing succeeds. Encoded names use a length-prefixed doubled-letter representation, and domain components may use DNS-style compression pointers.

## Harness Contract
The libFuzzer target passes the raw input bytes directly to Samba's NMB packet parser as one datagram, then rebuilds and frees parsed packets only if parsing returns a packet. No selector byte or external file wrapper is used.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
