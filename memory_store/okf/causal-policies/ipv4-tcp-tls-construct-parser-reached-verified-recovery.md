---
type: causal-policy
title: "Ipv4 Tcp Tls Construct Parser Reached Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "ipv4-tcp-tls"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "construct", "ipv4-tcp-tls", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached", "ipv4-tcp-tls", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Ipv4 Tcp Tls Construct Parser Reached Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[ipv4-tcp-tls]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `ipv4-tcp-tls` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached` on `ipv4-tcp-tls` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Construct a raw IPv4/TCP packet that the DPI harness classifies as TLS, then carry a TLS ServerHello
with an ALPN extension whose uncommon protocol name is longer than the fixed local buffer used by
the ALPN check.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The packet is raw IPv4 with a TCP segment and TLS record payload. The TLS ServerHello contains
standard version, random, session, cipher, compression, and extension fields; ALPN is encoded as an
extension with a vector of length-prefixed protocol names.

## Harness Contract
The nDPI fuzzer passes the input bytes directly to ndpi_detection_process_packet. The input is not
pcap-framed; the first bytes must be an IP packet, and port/payload shape influence TLS protocol
detection.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
