---
type: negative-memory
title: "Raw Ipv4 Nested Ieee1905 Construct No Crash Parser Not Reached Or Safe Address Storage Heap Buffer Overflow Read Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal parser_not_reached_or_safe_address_storage."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_safe_address_storage"
candidate_family: "construct"
input_format: "raw-ipv4-nested-ieee1905"
harness_convention: "afl-fuzzshark-ip"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-not-reached-or-safe-address-storage", "raw-ipv4-nested-ieee1905", "afl-fuzzshark-ip", "construct", "heap-buffer-overflow-read", "negative-memory", "round-37"]
match_keys: ["no_crash", "parser_not_reached_or_safe_address_storage", "raw-ipv4-nested-ieee1905", "afl-fuzzshark-ip", "heap-buffer-overflow-read", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Raw Ipv4 Nested Ieee1905 Construct No Crash Parser Not Reached Or Safe Address Storage Heap Buffer Overflow Read Negative Memory

- key: `no_crash x parser_not_reached_or_safe_address_storage`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-ipv4-nested-ieee1905]]
- related harness facts: [[afl-fuzzshark-ip]]

## Failure Shape
The raw-IP harness requires an IP protocol carrier before IEEE1905 can be reached through the ethertype table. Distinct carrier hypotheses included direct tunnel dispatch, NHRP traffic-indication dispatch, SNAP-style NHRP dispatch, and a short-address WPAN MPX bridge to IEEE1905. All exited cleanly. The likely miss is that the candidate either did not reach the IEEE1905 reassembly call through the nested carrier, or the carrier normalized packet addresses into storage that did not expose the short-address over-read.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_not_reached_or_safe_address_storage` on `raw-ipv4-nested-ieee1905` under `afl-fuzzshark-ip` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_not_reached_or_safe_address_storage` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_or_safe_address_storage`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 6 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
