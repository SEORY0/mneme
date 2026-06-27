---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Bootp Dhcp Dns Name Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "bootp-dhcp-dns-name"
harness_convention: "afl-fuzzshark"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "bootp-dhcp-dns-name", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "bootp-dhcp-dns-name", "afl-fuzzshark", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached No Target Crash Bootp Dhcp Dns Name Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bootp-dhcp-dns-name]]
- related harness facts: [[afl-fuzzshark]]

## Failure Shape
The active harness was BOOTP over UDP rather than a direct DNS dissector. DHCP domain-search and SIP-server options delivered long DNS names, RFC3396 splits, standard labels, and extended bitstring labels, but the local verifier did not report the DNS max-name overflow.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `bootp-dhcp-dns-name` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
BOOTP/DHCP options can carry DNS names through the domain-search option and SIP-server option. Long options can be split and reassembled using the DHCP long-option convention before the composite option data is passed to the shared DNS-name expander.

## Harness Contract
The fuzzshark target invokes the BOOTP dissector from the UDP port table on raw UDP payload bytes. A valid BOOTP fixed header, DHCP magic cookie, and option list are needed before DNS-name option payloads are interpreted.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
