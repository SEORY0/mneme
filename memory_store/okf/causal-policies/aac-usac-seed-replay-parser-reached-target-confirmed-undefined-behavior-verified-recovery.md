---
type: causal-policy
title: "AAC Usac Seed Replay Parser Reached Target Confirmed Undefined Behavior Verified Recovery"
description: "Round 15 server-verified recovery for aac-usac keyed by wrong_sink x parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "seed_replay"
input_format: "aac-usac"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "aac-usac", "libfuzzer", "seed-replay", "undefined-behavior", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "aac-usac", "libfuzzer", "undefined-behavior", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# AAC Usac Seed Replay Parser Reached Target Confirmed Undefined Behavior Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[aac-usac]]
- related harness facts: [[libfuzzer]]

## Policy
When `aac-usac` under `libfuzzer` reaches `parser_reached_target_confirmed` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use an in-repository AAC/USAC seed that reaches MPEG surround processing instead of constructing
   the bitstream from scratch. The accepted stream configures residual MPS processing and triggers
   the residual frequency-index bug; the local stack labels a helper, but official submission
   confirms the target condition.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The decoder accepts raw AAC/USAC streams, including streams with MPEG surround configuration. MPS
  configuration carries normal and residual sampling-frequency index state, and corpus samples with
  MPS payloads reach the residual processing code more reliably than hand-built byte envelopes.

## Harness Contract
- The libFuzzer harness passes raw decoder bytes to the libxaac decoder target. There is no leading
  mode selector, archive layer, or FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: seed_replay.
