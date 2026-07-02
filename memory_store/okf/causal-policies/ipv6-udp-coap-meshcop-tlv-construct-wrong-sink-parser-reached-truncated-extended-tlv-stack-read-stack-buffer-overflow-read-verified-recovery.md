---
type: causal-policy
title: "Ipv6 Udp Coap Meshcop Tlv Construct Wrong Sink Parser Reached Truncated Extended Tlv Stack Read Stack Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for ipv6-udp-coap-meshcop-tlv when wrong_sink pairs with parser_reached_truncated_extended_tlv_stack_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_truncated_extended_tlv_stack_read"
candidate_family: "construct"
input_format: "ipv6-udp-coap-meshcop-tlv"
harness_convention: "libfuzzer-ip6-send-fuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-truncated-extended-tlv-stack-read", "ipv6-udp-coap-meshcop-tlv", "libfuzzer-ip6-send-fuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-truncated-extended-tlv-stack-read", "ipv6-udp-coap-meshcop-tlv", "libfuzzer-ip6-send-fuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Ipv6 Udp Coap Meshcop Tlv Construct Wrong Sink Parser Reached Truncated Extended Tlv Stack Read Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_truncated_extended_tlv_stack_read`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[ipv6-udp-coap-meshcop-tlv]]
- related harness facts: [[libfuzzer-ip6-send-fuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_truncated_extended_tlv_stack_read`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `stack-buffer-overflow-read`
- related format facts: [[ipv6-udp-coap-meshcop-tlv]]
- related harness facts: [[libfuzzer-ip6-send-fuzzer]]

### Policy
When `wrong_sink x parser_reached_truncated_extended_tlv_stack_read` appears for `ipv6-udp-coap-meshcop-tlv`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-ip6-send-fuzzer]] harness contract and the [[ipv6-udp-coap-meshcop-tlv]] format contract before changing sink fields.
2. Recreate the verified causal relation: Construct a complete IPv6 UDP datagram to the local Thread management CoAP service, using a CoAP POST for the commissioner-set resource and a MeshCoP payload marker. In the MeshCoP TLV payload, include a well-formed commissioner session TLV and one valid commissioning TLV so the request is parsed as a commissioner-set body, then fill the copied TLV buffer with well-formed unknown data and end with a TLV header whose length selects extended-TLV form but omits the extended-length field. The validation loop checks only the base TLV header before calling the generic next-TLV helper, causing the vulnerable build to read past the copied stack buffer while the fixed build rejects the truncated extended TLV.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
OpenThread Thread-management traffic for this path is a raw IPv6 datagram carrying UDP to the Thread management CoAP port. The CoAP request must use POST, Uri-Path options for the commissioner-set resource, and a payload marker before MeshCoP TLVs. MeshCoP TLVs use a type byte, a one-byte base length, and, when the base length is the extended marker, an additional length field before the value. Commissioner-set parsing expects a commissioner session TLV and at least one valid commissioning TLV such as joiner UDP port or steering data; unknown TLVs are otherwise skipped by walking to the next TLV.

### Harness Contract
The ip6-send libFuzzer harness consumes raw bytes with no file envelope. The first byte is a link-security selector and is not part of the IPv6 datagram; all remaining bytes are appended as the outbound IPv6 message and passed to otIp6Send on an initialized leader instance. The carrier therefore needs internally consistent IPv6 payload length, UDP length, CoAP options, and MeshCoP payload layout; there is no FuzzedDataProvider front/back split.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_truncated_extended_tlv_stack_read`.
- Vulnerability class: `stack-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
