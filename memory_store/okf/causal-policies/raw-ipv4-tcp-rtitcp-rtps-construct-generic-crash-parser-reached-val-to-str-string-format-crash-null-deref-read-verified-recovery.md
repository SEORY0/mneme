---
type: causal-policy
title: "Raw Ipv4 Tcp Rtitcp Rtps Construct Generic Crash Parser Reached Val To Str String Format Crash Null Deref Read Verified Recovery"
description: "Server-verified recovery for raw-ipv4-tcp-rtitcp-rtps when generic_crash pairs with parser_reached_val_to_str_string_format_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_val_to_str_string_format_crash"
candidate_family: "construct"
input_format: "raw-ipv4-tcp-rtitcp-rtps"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "null-deref-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-val-to-str-string-format-crash", "raw-ipv4-tcp-rtitcp-rtps", "libfuzzer-fuzzshark-ip", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-val-to-str-string-format-crash", "raw-ipv4-tcp-rtitcp-rtps", "libfuzzer-fuzzshark-ip", "construct", "null-deref-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Raw Ipv4 Tcp Rtitcp Rtps Construct Generic Crash Parser Reached Val To Str String Format Crash Null Deref Read Verified Recovery

- key: `generic_crash x parser_reached_val_to_str_string_format_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[raw-ipv4-tcp-rtitcp-rtps]]
- related harness facts: [[libfuzzer-fuzzshark-ip]]

## Policy
When `generic_crash x parser_reached_val_to_str_string_format_crash` appears for `raw-ipv4-tcp-rtitcp-rtps`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-fuzzshark-ip` harness contract and the `raw-ipv4-tcp-rtitcp-rtps` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the fuzzshark IP contract: raw IPv4 carrying TCP, with TCP payload recognized as RTI-TCP and containing an RTPS data message. Keep the RTPS header valid and use a DATA submessage with inline QoS enabled. Inside the inline parameter list, include a data-representation sequence whose element is outside the known value-string table while preserving the parameter length and sentinel structure; this forces the RTPS value-string fallback to treat an integer as a string pointer. The fixed build rejects or formats the unknown representation safely.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[raw-ipv4-tcp-rtitcp-rtps]]. RTI-TCP data messages are reached through a raw IPv4/TCP carrier. The RTI-TCP header precedes an RTPS message with RTPS magic, protocol version, vendor id, GUID prefix, and submessages. RTPS DATA submessages carry reader and writer entity ids, a writer sequence number, a key-hash suffix, and optional inline QoS when the Q flag is set. Inline QoS is a parameter list with parameter id, length, value, and a sentinel terminator; the data-representation parameter contains a sequence count followed by representation identifiers.

## Harness Contract
Use [[libfuzzer-fuzzshark-ip]]. The fuzzshark target is configured for the IP dissector. The PoC file bytes are fed directly as one raw IPv4 packet; there is no pcap wrapper, no stdin line protocol beyond the raw file, and no FuzzedDataProvider front/back carving. Nested dispatch depends on the IPv4 protocol field, TCP payload, and RTI-TCP/RTPS magic and length fields.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x parser_reached_val_to_str_string_format_crash`.
- Vulnerability class: `null-deref-read`.
- Recovery summary: Use the fuzzshark IP contract: raw IPv4 carrying TCP, with TCP payload recognized as RTI-TCP and containing an RTPS data message. Keep the RTPS header valid and use a DATA submessage with inline QoS enabled. Inside the inline parameter list, include a data-representation sequence whose element is outside the known value-string table while preserving the parameter length and sentinel structure; this forces the RTPS value-string fallback to treat an integer as a string pointer. The fixed build rejects or formats the unknown representation safely.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
