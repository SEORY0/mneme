---
type: negative-memory
title: "No Crash Parser Reached Clean Rejection Coap Udp Pdu Construct Heap Buffer Overflow Read Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_clean_rejection."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_rejection"
candidate_family: "construct"
input_format: "coap-udp-pdu"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-rejection", "coap-udp-pdu", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_clean_rejection", "coap-udp-pdu", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached Clean Rejection Coap Udp Pdu Construct Heap Buffer Overflow Read Negative Memory

- key: `no_crash x parser_reached_clean_rejection`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[coap-udp-pdu]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Malformed extended option-length encodings reached the CoAP option parser but were rejected cleanly as missing payload or malformed options. The attempted boundary did not produce an out-of-bounds sanitizer read.

## Policy
Treat `no_crash x parser_reached_clean_rejection` on `coap-udp-pdu` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_clean_rejection` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_rejection`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
A UDP CoAP PDU begins with a compact fixed header, optional token bytes, then option encodings. Each option header encodes delta and length nibbles, with special nibble values indicating that extra bytes carry the extended value.

## Harness Contract
libFuzzer raw bytes are passed directly to coap_pdu_parse as a UDP PDU. The harness then queries URI/path helpers, prints the PDU, re-encodes the header, and frees derived strings.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 3 attempts.
- Scope: generator repair and basin avoidance only.
