---
type: causal-policy
title: "Wireshark Idn Over Udp Construct Generic Crash Parser Reached Idn Dmx Dictionary Underflowed Index Heap Buffer Overflow Write Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached_idn_dmx_dictionary_underflowed_index."
failure_class: "generic_crash"
verifier_signal: "parser_reached_idn_dmx_dictionary_underflowed_index"
candidate_family: "construct"
input_format: "wireshark-idn-over-udp"
harness_convention: "afl-libfuzzer-compatible-fuzzshark"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-idn-dmx-dictionary-underflowed-index", "wireshark-idn-over-udp", "afl-libfuzzer-compatible-fuzzshark", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached_idn_dmx_dictionary_underflowed_index", "wireshark-idn-over-udp", "afl-libfuzzer-compatible-fuzzshark", "heap-buffer-overflow-write", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Wireshark Idn Over Udp Construct Generic Crash Parser Reached Idn Dmx Dictionary Underflowed Index Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_idn_dmx_dictionary_underflowed_index`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[wireshark-idn-over-udp]]
- related harness facts: [[afl-libfuzzer-compatible-fuzzshark]]

## Failure Shape
Build a minimal UDP datagram whose payload is an IDN MESSAGE for the registered IDN UDP service. Use a DMX-style chunk with a configuration header and a very small service word count. In the DMX dictionary, first use a dimmer-level-subset tag whose encoded size leaves the dictionary alignment logic short of a word boundary; this drives the loop index below the valid configuration-array range. Then emit a second dimmer-level-subset tag that includes base/count fields, causing the vulnerable build to store through the underflowed index while the fixed build rejects the index before use.

## Policy
When `generic_crash x parser_reached_idn_dmx_dictionary_underflowed_index` appears for `wireshark-idn-over-udp` under `afl-libfuzzer-compatible-fuzzshark`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[wireshark-idn-over-udp]]` format contract and `[[afl-libfuzzer-compatible-fuzzshark]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `wireshark-idn-over-udp` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 9 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
