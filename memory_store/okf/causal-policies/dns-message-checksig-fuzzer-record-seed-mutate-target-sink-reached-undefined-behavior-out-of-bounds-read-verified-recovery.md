---
type: causal-policy
title: "Dns Message Checksig Fuzzer Record Seed Mutate Target Sink Reached Undefined Behavior Out Of Bounds Read Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal target_sink_reached."
failure_class: "wrong_sink"
verifier_signal: "target_sink_reached"
candidate_family: "seed_mutate"
input_format: "dns-message-checksig-fuzzer-record"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-sink-reached", "dns-message-checksig-fuzzer-record", "seed-mutate", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "target_sink_reached", "dns-message-checksig-fuzzer-record", "libfuzzer", "undefined-behavior-out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Dns Message Checksig Fuzzer Record Seed Mutate Target Sink Reached Undefined Behavior Out Of Bounds Read Verified Recovery

## Policy
For `wrong_sink x target_sink_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the harness setup byte to request an additional SIG-style signature record with view lookup
  enabled, then provide a syntactically valid signature RDATA body over the harness-built root SOA
  question.
1. The signature check walks into view/zone lookup without an intermediate trie node, so the
  duplicate-link check examines the last entry of an empty chain.

## Format Contract
- The input is not a raw DNS packet.
- The fuzzer builds a fixed root SOA question and, when requested by the setup bitfield, appends
  either TSIG or SIG-style additional data whose RDATA is copied from the remaining input.
- A valid signature seed can therefore be reused by changing harness setup rather than constructing
  full wire DNS headers.

## Harness Contract
- LibFuzzer passes raw bytes to the target, but the harness consumes an initial setup bitfield
  before constructing the DNS message.
- That byte controls whether to append a signature, choose TSIG versus SIG-style data, set time
  adjustments, install query TSIG/key state, and enable keyring/view lookup.
- The next byte contributes to generated DNS header flags/opcode; the rest becomes signature RDATA
  only when a signature is enabled.

## Related Knowledge
- Format facts: [[dns-message-checksig-fuzzer-record]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
