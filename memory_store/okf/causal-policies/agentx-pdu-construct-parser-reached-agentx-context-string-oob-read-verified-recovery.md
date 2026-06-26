---
type: causal-policy
title: "Agentx Pdu Construct Parser Reached Agentx Context String Oob Read Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_agentx_context_string_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_agentx_context_string_oob_read"
candidate_family: "construct"
input_format: "agentx-pdu"
harness_convention: "afl-libfuzzer-raw-bytes"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-agentx-context-string-oob-read", "construct", "agentx-pdu", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_agentx_context_string_oob_read", "agentx-pdu", "afl-libfuzzer-raw-bytes", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Agentx Pdu Construct Parser Reached Agentx Context String Oob Read Verified Recovery

- key: `wrong_sink x parser_reached_agentx_context_string_oob_read`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[agentx-pdu]]
- harnesses: [[afl-libfuzzer-raw-bytes]]

## Failure Shape
The verifier-confirmed candidate preserved the `agentx-pdu` parser envelope under `afl-libfuzzer-raw-bytes` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_agentx_context_string_oob_read` on `agentx-pdu` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a syntactically coherent AgentX PDU whose common header length exactly matches the available
payload, enable the non-default-context path, then make the context string length claim more data
than remains. The vulnerable parser copies the context bytes before enforcing the remaining-length
invariant; the fixed build rejects the short payload.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
AgentX PDUs start with a fixed common header containing version, command, flags, identifiers, and a
body-length field. The body length must match the remaining bytes for the parser to continue. A non-
default-context flag routes the start of the body through the AgentX string decoder before command-
specific fields.

## Harness Contract
The fuzzer passes the raw input buffer directly to the AgentX parser; there is no file wrapper,
checksum, mode selector, or FuzzedDataProvider carving.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
