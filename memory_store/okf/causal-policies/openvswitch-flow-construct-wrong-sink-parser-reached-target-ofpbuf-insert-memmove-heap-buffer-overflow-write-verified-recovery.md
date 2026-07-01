---
type: causal-policy
title: "Openvswitch Flow Construct Wrong Sink Parser Reached Target Ofpbuf Insert Memmove Heap Buffer Overflow Write Verified Recovery"
description: "Round 32 server-verified recovery for openvswitch-flow keyed by wrong_sink x parser_reached_target_ofpbuf_insert_memmove."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_ofpbuf_insert_memmove"
candidate_family: "construct"
input_format: "openvswitch-flow"
harness_convention: "afl-libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-ofpbuf-insert-memmove", "openvswitch-flow", "afl-libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-target-ofpbuf-insert-memmove", "openvswitch-flow", "afl-libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Openvswitch Flow Construct Wrong Sink Parser Reached Target Ofpbuf Insert Memmove Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_target_ofpbuf_insert_memmove`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[openvswitch-flow]]
- related harness facts: [[afl-libfuzzer]]

## Policy
When `openvswitch-flow` under `[[afl-libfuzzer]]` produces `parser_reached_target_ofpbuf_insert_memmove` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[openvswitch-flow]]` through `[[afl-libfuzzer]]`.
2. Apply the verified recovery: Satisfy the harness C-string contract, choose a flow-mod command that requires actions, and build a valid flow string that sets the default Ethernet packet type without causing the nx-match writer to mark Ethernet as implied. Add enough no-prerequisite metadata/register-style match fields to make the encoded match non-empty before the packet-type stub is inserted. This reaches the packet-type insertion path, where the vulnerable buffer insert grows the buffer and then moves too many bytes.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The OVS flow grammar is a comma-separated flow-mod string with match fields and an actions clause for commands that require actions. Protocol/packet-type selectors can set the default packet type; many L2/L3 fields add Ethernet prerequisites and suppress the vulnerable insertion condition, while metadata/register-style fields can encode match data without setting that implied-Ethernet flag.

## Harness Contract
- The first input byte selects the OpenFlow flow-mod command by modulo arithmetic. The remaining bytes are passed as one NUL-terminated C string; newlines and interior NULs are rejected before parsing. The harness parses the flow string, chooses a usable protocol, encodes the flow mod, and frees the resulting buffers.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
