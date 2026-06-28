---
type: causal-policy
title: "Dhcpv6 With Foreign Radius Option Regression Seed Mutate Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 13 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "regression_seed_mutate"
input_format: "dhcpv6-with-foreign-radius-option"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "dhcpv6-with-foreign-radius-option", "regression-seed-mutate", "verified-recovery", "round-13"]
match_keys: ["wrong_sink", "sink_mismatch", "dhcpv6-with-foreign-radius-option", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# Dhcpv6 With Foreign Radius Option Regression Seed Mutate Sink Mismatch Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x sink_mismatch`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a raw DHCPv6 packet that passes the outer packet validator and carries a foreign RADIUS payload inside an option whose declared length contains the whole embedded payload. The embedded RADIUS data must use the long-extended fragment path with at least one fragment that is accepted as part of the same attribute sequence, followed by a trailing fragment that does not have enough remaining bytes for its own header. This keeps the outer DHCPv6 decoder on the foreign-option path and makes the inner RADIUS decoder read past the available fragment bytes.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Normal DHCPv6 packets start with a compact message header followed by options; relay packets use a larger relay header. Options are big-endian code-and-length records, and the option length gates all nested decoding. Some DHCPv6 options are decoded by a foreign protocol dictionary, so their payload is handed to another protocol parser after the DHCPv6 option envelope is accepted. RADIUS long-extended attributes are fragmentable records where consecutive fragments can be coalesced by matching header fields, and the fragment loop must still ensure that each following fragment has enough room for the fragment header before inspecting it.

## Harness Contract
- The active fuzzer binary is selected by the executable name and, for DHCPv6, passes the raw libFuzzer byte buffer directly to the DHCPv6 protocol decoder. There is no leading mode byte and no FuzzedDataProvider carving; all selector behavior comes from the DHCPv6 message type and option codes inside the input.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
