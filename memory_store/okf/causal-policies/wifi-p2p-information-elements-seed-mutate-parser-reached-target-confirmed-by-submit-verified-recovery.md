---
type: causal-policy
title: "Wifi P2P Information Elements Seed Mutate Parser Reached Target Confirmed By Submit Verified Recovery"
description: "Round 10 verified recovery for generic_crash with verifier signal parser_reached_target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_confirmed_by_submit"
candidate_family: "seed_mutate"
input_format: "wifi-p2p-information-elements"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-confirmed-by-submit", "wifi-p2p-information-elements", "verified-recovery", "round-10"]
match_keys: ["generic_crash", "parser_reached_target_confirmed_by_submit", "wifi-p2p-information-elements", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# Wifi P2P Information Elements Seed Mutate Parser Reached Target Confirmed By Submit Verified Recovery

## Policy
For `generic_crash x parser_reached_target_confirmed_by_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid P2P probe-response IE seed and append a P2P vendor IE containing a Group Info attribute.
2. The client descriptor must be internally length-consistent, include a device-name TLV, and declare more secondary device types than the peer-info fixed buffer can hold.
3. The vulnerable build copies the declared list into fixed storage; the fixed build rejects or bounds it.

## Format Contract
- P2P attributes live inside a Wi-Fi vendor-specific IE with the P2P OUI/type. Group Info contains length-prefixed client descriptors; each descriptor carries device and interface addresses, capability/configuration fields, primary device type, a count-prefixed secondary device-type list, and a WPS Device Name TLV.
- Harness: The fuzzer passes raw IE bytes to scan-result and probe-request P2P handlers, and also treats long inputs as action frames. No outer 802.11 frame is needed for the scan/probe IE path.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
