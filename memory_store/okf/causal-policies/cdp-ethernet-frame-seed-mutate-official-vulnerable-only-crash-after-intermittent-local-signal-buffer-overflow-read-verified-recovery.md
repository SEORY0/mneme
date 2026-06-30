---
type: causal-policy
title: "Cdp Ethernet Frame Seed Mutate Official Vulnerable Only Crash After Intermittent Local Signal Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for no_crash with verifier signal official_vulnerable_only_crash_after_intermittent_local_signal."
failure_class: "no_crash"
verifier_signal: "official_vulnerable_only_crash_after_intermittent_local_signal"
candidate_family: "seed_mutate"
input_format: "cdp-ethernet-frame"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "official-vulnerable-only-crash-after-intermittent-local-signal", "cdp-ethernet-frame", "libfuzzer", "seed-mutate", "buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["no_crash", "official_vulnerable_only_crash_after_intermittent_local_signal", "cdp-ethernet-frame", "libfuzzer", "buffer-overflow-read", "verified_recovery", "seed-mutate", "buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Cdp Ethernet Frame Seed Mutate Official Vulnerable Only Crash After Intermittent Local Signal Buffer Overflow Read Verified Recovery

## Policy
For `no_crash x official_vulnerable_only_crash_after_intermittent_local_signal`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a structurally valid 802.3 CDP Ethernet frame: CDP multicast destination, LLC/SNAP CDP protocol, accepted CDP version and TTL, plus the mandatory chassis, port, capabilities, software, and platform TLVs. In the address TLV, keep the NLPID/IP address-record gates recognizable, but make the record's declared address payload shorter than the fixed IPv4 reparse assumes. Add uninterpreted trailing data outside the CDP payload so the raw input allocation/layout makes the vulnerable reparse fault while the fixed build rejects or bounds-checks the short address record.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[cdp-ethernet-frame]]: The input is a raw Ethernet frame carrying CDP. The frame starts with the CDP multicast destination, a source MAC, and a big-endian 802.3 length that covers the LLC/SNAP and CDP payload. The LLC/SNAP header uses SNAP bytes, a Cisco organization code, and the CDP protocol id. The CDP payload has version, TTL, checksum bytes that are not enforced by this build, and TLVs with a two-byte type and two-byte total length. The address TLV begins with a four-byte address count followed by address subrecords: protocol type, protocol-length byte, protocol bytes, two-byte address length, and address bytes. Successful full decode also expects chassis, port, capabilities, and software or platform description TLVs.
- Harness [[libfuzzer]]: The libFuzzer harness passes the raw file bytes unchanged to LLDP, CDP, SONMP, and EDP decoders. There is no FuzzedDataProvider, no leading mode selector, and no checksum repair layer. Inputs shorter than the harness minimum or longer than the harness maximum are ignored before decoding. For CDP, the destination/protocol gates select the CDP decoder; unrelated trailing bytes after the CDP payload can remain physically present in the raw input without being part of the CDP length.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[cdp-ethernet-frame]] and [[libfuzzer]].
