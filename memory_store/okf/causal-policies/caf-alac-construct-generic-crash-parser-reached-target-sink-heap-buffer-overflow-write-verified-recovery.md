---
type: causal-policy
title: "Caf Alac Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Write Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "caf-alac"
harness_convention: "libfuzzer-sndfile-virtual-io"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "caf-alac", "libfuzzer-sndfile-virtual-io", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached_target_sink", "caf-alac", "libfuzzer-sndfile-virtual-io", "heap-buffer-overflow-write", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Caf Alac Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[caf-alac]]
- related harness facts: [[libfuzzer-sndfile-virtual-io]]

## Failure Shape
Build a coherent CAF ALAC stream rather than a loose cookie/data blob: the stream description declares ALAC with a small channel count and minimal frame length, the magic cookie mirrors those decoder parameters, the packet table declares the compressed packet size, and the data chunk carries one packet. In that packet, use escape-coded mono ALAC elements so predictor coding is bypassed, then provide more mono elements than the declared channel capacity can hold. The vulnerable decoder keeps advancing its output channel index and writes past the channel-scaled decode buffer; the fixed build rejects the over-capacity element sequence.

## Policy
When `generic_crash x parser_reached_target_sink` appears for `caf-alac` under `libfuzzer-sndfile-virtual-io`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[caf-alac]]` format contract and `[[libfuzzer-sndfile-virtual-io]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `caf-alac` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
