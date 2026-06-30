---
type: causal-policy
title: "HEVC Annex B Elementary Stream Seed Mutate Parser Reached Downstream Crash Target Confirmed By Submit Integer Overflow Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_downstream_crash_target_confirmed_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_downstream_crash_target_confirmed_by_submit"
candidate_family: "seed_mutate"
input_format: "hevc-annex-b-elementary-stream"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-downstream-crash-target-confirmed-by-submit", "hevc-annex-b-elementary-stream", "libfuzzer", "seed-mutate", "integer-overflow", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_downstream_crash_target_confirmed_by_submit", "hevc-annex-b-elementary-stream", "libfuzzer", "integer-overflow", "wrong-sink", "parser-reached-downstream-crash-target-confirmed-by-submit", "hevc-annex-b-elementary-stream", "libfuzzer", "integer-overflow", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# HEVC Annex B Elementary Stream Seed Mutate Parser Reached Downstream Crash Target Confirmed By Submit Integer Overflow Verified Recovery

- key: `wrong_sink x parser_reached_downstream_crash_target_confirmed_by_submit`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[hevc-annex-b-elementary-stream]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_downstream_crash_target_confirmed_by_submit` on `hevc-annex-b-elementary-stream`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a compact HEVC Annex-B seed that already has coherent VPS, SPS, PPS, and non-IDR slice NAL units. Preserve the stream and enable the SPS long-term-reference gate with an empty SPS long-term table, then insert an oversized unsigned Exp-Golomb value at the slice-level long-term-picture count. The vulnerable build accepts the wrapped DPB-size relation and later consumes inconsistent reference state; the fixed build rejects the count before that state is used.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[hevc-annex-b-elementary-stream]]: The useful carrier is a raw HEVC elementary stream made of start-code-delimited NAL units, not a container. Parameter sets must precede slices, and the target slice syntax depends on SPS and PPS gates such as long-term-reference presence, picture-order-count width, short-term reference sets, and slice-header flags. RBSP edits must be converted back to escaped NAL payload bytes so emulation-prevention rules remain valid.
- Harness [[libfuzzer]]: The libFuzzer target consumes the original input buffer directly. A few bytes near the start are also used by the harness to select decoder color format, architecture, and core count, but the same complete buffer is still passed to header decode and then repeatedly to frame decode. There is no FuzzedDataProvider layout or file wrapper.

## Negative Memory
- Do not corrupt the outer `hevc-annex-b-elementary-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[hevc-annex-b-elementary-stream]] and [[libfuzzer]].
