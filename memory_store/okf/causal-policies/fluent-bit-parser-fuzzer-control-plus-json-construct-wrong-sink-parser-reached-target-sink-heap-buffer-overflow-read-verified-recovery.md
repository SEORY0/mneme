---
type: causal-policy
title: "Fluent Bit Parser Fuzzer Control Plus Json Construct Wrong Sink Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-json"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "fluent-bit-parser-fuzzer-control-plus-json", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "fluent-bit-parser-fuzzer-control-plus-json", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Fluent Bit Parser Fuzzer Control Plus Json Construct Wrong Sink Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use the parser fuzzer control prefix to select JSON mode and enable time parsing with a chosen time key. The JSON record must remain a map and include a large preceding field so the selected key is packed near a MsgPack buffer boundary. Give that selected time key a non-string primitive value. During time resolution the parser treats the MsgPack primitive union as string metadata; the bogus length triggers the invalid-time error path, and the later diagnostic copy reads past the packed buffer boundary.

## Policy
When `wrong_sink x parser_reached_target_sink` appears for `fluent-bit-parser-fuzzer-control-plus-json` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[fluent-bit-parser-fuzzer-control-plus-json]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `fluent-bit-parser-fuzzer-control-plus-json` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 29 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
