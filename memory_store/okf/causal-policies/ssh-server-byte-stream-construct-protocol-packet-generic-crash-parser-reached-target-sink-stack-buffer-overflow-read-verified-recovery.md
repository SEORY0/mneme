---
type: causal-policy
title: "SSH Server Byte Stream Construct Protocol Packet Generic Crash Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for ssh-server-byte-stream keyed by generic_crash x parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct_protocol_packet"
input_format: "ssh-server-byte-stream"
harness_convention: "libfuzzer-libssh-server-socket"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "ssh-server-byte-stream", "libfuzzer-libssh-server-socket", "construct-protocol-packet", "stack-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "parser-reached-target-sink", "ssh-server-byte-stream", "libfuzzer-libssh-server-socket", "construct-protocol-packet", "stack-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# SSH Server Byte Stream Construct Protocol Packet Generic Crash Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ssh-server-byte-stream]]
- related harness facts: [[libfuzzer-libssh-server-socket]]

## Policy
When `ssh-server-byte-stream` under `[[libfuzzer-libssh-server-socket]]` produces `parser_reached_target_sink` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[ssh-server-byte-stream]]` through `[[libfuzzer-libssh-server-socket]]`.
2. Apply the verified recovery: Build a minimal SSH server-side byte stream that satisfies the text identification gate and one plaintext binary packet envelope, then enter the userauth request handler with the public-key method selected. The triggering invariant is a multi-field unpack where an early length-prefixed field is accepted but the following length-prefixed field is incomplete, forcing cleanup rollback over mixed scalar and string output arguments.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The harness consumes an SSH byte stream: an identification line is followed by binary packets with packet length, padding length, payload, and padding. SSH protocol strings inside the payload are length-prefixed, and the authentication request path dispatches on service, method, and public-key fields before parsing the key blob fields.

## Harness Contract
- LibFuzzer bytes are written as the client side of a socketpair to a libssh server instance. There is no FuzzedDataProvider or mode selector; the raw file bytes must include the SSH stream framing needed before pre-crypto packet dispatch reaches userauth parsing.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct_protocol_packet.
