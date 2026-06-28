---
type: causal-policy
title: "Sip Message Construct Parser Reached Sink Match Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "sip-message"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "construct", "sip-message", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "sip-message", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Sip Message Construct Parser Reached Sink Match Verified Recovery

- key: `wrong_sink x parser_reached_sink_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[sip-message]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `sip-message` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_sink_match` on `sip-message` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Feed a raw buffer consisting only of SIP line-break characters. The parser's leading empty-line skip
advances to the end of the buffer and then reads the cursor before rechecking the remaining length.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
SIP messages are line-oriented and OpenSIPS permits leading CR/LF pairs before the request or status
line. This parser path scans those leading separators before normal message-line parsing.

## Harness Contract
The harness passes raw bytes directly to the OpenSIPS message parser. There is no length prefix,
mode selector, or checksum gate; the buffer contents themselves form the SIP message.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
