---
type: causal-policy
title: "AAC Usac MPS Seed Replay Parser Reached Target Confirmed Undefined Behavior Index Out Of Bounds Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "seed_replay"
input_format: "aac-usac-mps"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-index-out-of-bounds"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "aac-usac-mps", "libfuzzer", "seed-replay", "undefined-behavior-index-out-of-bounds", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "aac-usac-mps", "libfuzzer", "undefined-behavior-index-out-of-bounds", "wrong-sink", "parser-reached-target-confirmed", "aac-usac-mps", "libfuzzer", "undefined-behavior-index-out-of-bounds", "verified_recovery", "seed_replay", "seed-replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# AAC Usac MPS Seed Replay Parser Reached Target Confirmed Undefined Behavior Index Out Of Bounds Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[aac-usac-mps]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_target_confirmed` on `aac-usac-mps`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Preserve a real raw AAC/USAC stream that already reaches deep MPEG surround decoder state instead of constructing the bitstream. The useful carrier configures MPS-related residual processing and reaches a sanitizer-reported arithmetic helper before the local verifier's sink matcher, but the official differential result confirms the described arbitrary-downmix residual-band condition is target-matched on the vulnerable image and clean on the fixed image.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[aac-usac-mps]]: The input is a raw AAC/USAC decoder stream. Streams beginning with an ADTS sync are handled as ADTS; otherwise the decoder treats the bytes as its non-ADTS configuration and frame stream. Valid MPS/USAC corpus carriers can configure MPEG surround residual processing and are much more effective than hand-built envelopes. Local sanitizer stacks may surface helper arithmetic or transform routines even when the accepted stream has reached the target MPS state.
- Harness [[libfuzzer]]: The libFuzzer harness passes the whole input buffer directly to the xAAC decoder. There is no outer archive, length prefix, integrity field, mode selector, or FuzzedDataProvider split. After configuration, the same byte stream is repeatedly decoded while the decoder reports consumed-byte counts.

## Negative Memory
- Do not corrupt the outer `aac-usac-mps` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[aac-usac-mps]] and [[libfuzzer]].
