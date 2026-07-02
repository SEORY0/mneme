---
type: causal-policy
title: "Thread Ipv6 Coap Meshcop Construct Wrong Sink Parser Reached Target Sink Out Of Bounds Write Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "thread-ipv6-coap-meshcop"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "thread-ipv6-coap-meshcop", "out-of-bounds-write", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-target-sink", "thread-ipv6-coap-meshcop", "libfuzzer", "out-of-bounds-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Thread Ipv6 Coap Meshcop Construct Wrong Sink Parser Reached Target Sink Out Of Bounds Write Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_target_sink` on `thread-ipv6-coap-meshcop` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Build the fuzzer input as the harness selector byte followed by a complete IPv6 UDP datagram.
2. Route the packet to the local Thread management CoAP endpoint, encode a POST request with the energy-scan URI path and valid MeshCoP TLVs, then keep the channel mask valid while setting the scan count high enough that repeated software scan results exceed the fixed result array.
3. Keep IP and UDP lengths and checksum coherent.

## Format Contract
- Input format: [[thread-ipv6-coap-meshcop]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `thread-ipv6-coap-meshcop` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
