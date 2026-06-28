---
type: causal-policy
title: "Net Snmp Config Text Construct Config Config Parser Reached Asan Signal Off By One Read Verified Recovery"
description: "Round 9 verified recovery for generic_crash with verifier signal config_parser_reached_asan_signal."
failure_class: "generic_crash"
verifier_signal: "config_parser_reached_asan_signal"
candidate_family: "construct-config"
input_format: "net-snmp-config-text"
harness_convention: "afl-file-fuzzer"
vuln_class: "off-by-one-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "config-parser-reached-asan-signal", "net-snmp-config-text", "construct-config", "verified-recovery", "round-9"]
match_keys: ["generic_crash", "config_parser_reached_asan_signal", "net-snmp-config-text", "afl-file-fuzzer", "off-by-one-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Net Snmp Config Text Construct Config Config Parser Reached Asan Signal Off By One Read Verified Recovery

## Policy
For `generic_crash x config_parser_reached_asan_signal`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the active config-file fuzzer rather than an SNMP packet.
1. Provide line-oriented Net-SNMP configuration tokens that drive address or trap parsing with
  malformed network-address text.
1. The vulnerable build reaches the libsnmp off-by-one read during config token handling; the fixed
  build exits cleanly.

## Format Contract
- The accepted input is Net-SNMP configuration text: line-oriented tokens with whitespace-separated
  arguments.
- Packet envelopes such as AgentX or BER SNMP messages are treated as config tokens and do not reach
  packet parsers under this wrapper.

## Harness Contract
- The AFL-style wrapper writes the raw bytes to a temporary config file and calls the Net-SNMP
  read_config path.
- There is no front selector and no FuzzedDataProvider layout; line/token syntax determines the
  parser branch.

## Related Knowledge
- Format facts: [[net-snmp-config-text]]
- Harness facts: [[afl-file-fuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
