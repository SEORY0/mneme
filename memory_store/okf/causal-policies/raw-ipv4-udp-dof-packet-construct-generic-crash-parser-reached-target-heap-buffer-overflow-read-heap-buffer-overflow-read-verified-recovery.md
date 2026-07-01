---
type: causal-policy
title: "Raw Ipv4 UDP Dof Packet Construct Generic Crash Parser Reached Target Heap Buffer Overflow Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for raw-ipv4-udp-dof-packet keyed by generic_crash x parser_reached_target_heap_buffer_overflow_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_heap_buffer_overflow_read"
candidate_family: "construct"
input_format: "raw-ipv4-udp-dof-packet"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-heap-buffer-overflow-read", "raw-ipv4-udp-dof-packet", "libfuzzer-fuzzshark-ip", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "parser-reached-target-heap-buffer-overflow-read", "raw-ipv4-udp-dof-packet", "libfuzzer-fuzzshark-ip", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Raw Ipv4 UDP Dof Packet Construct Generic Crash Parser Reached Target Heap Buffer Overflow Read Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_heap_buffer_overflow_read`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[raw-ipv4-udp-dof-packet]]
- related harness facts: [[libfuzzer-fuzzshark-ip]]

## Policy
When `raw-ipv4-udp-dof-packet` under `[[libfuzzer-fuzzshark-ip]]` produces `parser_reached_target_heap_buffer_overflow_read` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[raw-ipv4-udp-dof-packet]]` through `[[libfuzzer-fuzzshark-ip]]`.
2. Apply the verified recovery: Build a coherent raw IPv4 UDP packet whose UDP payload is dispatched to the registered DOF transport dissector. Inside DOF, use DNP and DPP headers that select the OAP application path, then take an OAP binding route that calls the Object-ID formatter. The trigger is an Object-ID buffer whose encoded class-width request is wider than the actual Object-ID buffer supplied to the raw unmarshal helper, causing the vulnerable build to read past the buffer while the fixed build rejects the short buffer.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The active Wireshark target expects raw IPv4 packet bytes rather than a pcap file or UDP payload alone. A valid carrier needs an IPv4 header, UDP header, and a DOF UDP port so the UDP dissector table hands the payload to DOF. DOF payloads are layered: DNP frames wrap DPP frames, DPP can dispatch to application protocols, and OAP bindings contain an interface identifier followed by an Object ID. DOF compressed integer and Object-ID fields encode their own width in leading bits, so declared width must be consistent with the actual remaining buffer to avoid the vulnerable raw read.

## Harness Contract
- The oss-fuzzshark wrapper is configured for the ip dissector and feeds the entire file as one raw frame buffer with unknown outer encapsulation. There is no corpus directory, no FuzzedDataProvider layout, and no capture-file wrapper; secondary dispatch depends on the packet headers and dissector tables reached from the raw IPv4 frame.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
