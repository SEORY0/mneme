---
type: "causal-policy"
title: "Ipv6 Udp Coap Meshcop Tlv Construct Wrong Sink Parser Reached Target Sink Official Match Stack Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_target_sink_official_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink_official_match"
candidate_family: "construct"
input_format: "ipv6-udp-coap-meshcop-tlv"
harness_convention: "libfuzzer-ip6-send"
vuln_class: "stack-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-target-sink-official-match", "ipv6-udp-coap-meshcop-tlv", "libfuzzer-ip6-send", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_target_sink_official_match", "ipv6-udp-coap-meshcop-tlv", "libfuzzer-ip6-send", "stack-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Ipv6 Udp Coap Meshcop Tlv Construct Wrong Sink Parser Reached Target Sink Official Match Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink_official_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ipv6-udp-coap-meshcop-tlv]]
- related harness facts: [[libfuzzer-ip6-send]]

## Failure Shape
Build the post-selector bytes as a complete IPv6 datagram carrying UDP to the Thread management CoAP service, with a valid checksum, mesh-local source and leader-local destination so the packet is treated as Thread-management traffic. Encode a CoAP POST for the commissioner-set resource with a payload marker. In the MeshCoP payload, include one valid commissioning TLV early to satisfy the handler's valid-data gate, pad with an ignored TLV, and place a malformed Commissioner Session ID TLV at the end of a full-sized copied TLV buffer so the typed session-id getter reads beyond the stack buffer. The fixed build validates the malformed TLV and stays clean.

## Policy
When `wrong_sink x parser_reached_target_sink_official_match` appears for `[[ipv6-udp-coap-meshcop-tlv]]` under `[[libfuzzer-ip6-send]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[ipv6-udp-coap-meshcop-tlv]]` format contract and `[[libfuzzer-ip6-send]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[ipv6-udp-coap-meshcop-tlv]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
