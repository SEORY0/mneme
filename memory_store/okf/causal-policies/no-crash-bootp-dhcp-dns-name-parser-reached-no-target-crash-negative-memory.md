---
type: causal-policy
title: "No Crash Bootp Dhcp Dns Name Parser Reached No Target Crash Negative Memory"
description: "Negative memory for no_crash with parser_reached_no_target_crash on bootp-dhcp-dns-name inputs."
failure_class: no_crash
verifier_signal: parser_reached_no_target_crash
candidate_family: construct
input_format: bootp-dhcp-dns-name
harness_convention: afl-fuzzshark
vuln_class: heap-buffer-overflow-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-target-crash, bootp-dhcp-dns-name, heap-buffer-overflow-write, negative_memory]
match_keys: [no-crash, parser-reached-no-target-crash, bootp-dhcp-dns-name, heap-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Bootp Dhcp Dns Name Parser Reached No Target Crash Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[bootp-dhcp-dns-name]]

## Dead End
The active harness was BOOTP over UDP rather than a direct DNS dissector. DHCP domain-search and SIP-server options delivered long DNS names, RFC3396 splits, standard labels, and extended bitstring labels, but the local verifier did not report the DNS max-name overflow.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
