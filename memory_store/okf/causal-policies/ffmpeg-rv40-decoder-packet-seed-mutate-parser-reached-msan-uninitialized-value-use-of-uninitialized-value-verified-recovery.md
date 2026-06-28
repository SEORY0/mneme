---
type: causal-policy
title: "Ffmpeg RV40 Decoder Packet Seed Mutate Parser Reached Msan Uninitialized Value Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for ffmpeg-rv40-decoder-packet when wrong_sink pairs with parser_reached_msan_uninitialized_value."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_msan_uninitialized_value"
candidate_family: "seed_mutate"
input_format: "ffmpeg-rv40-decoder-packet"
harness_convention: "oss-fuzz-run_poc-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-msan-uninitialized-value", "ffmpeg-rv40-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "seed-mutate", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-msan-uninitialized-value", "ffmpeg-rv40-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "seed-mutate", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Ffmpeg RV40 Decoder Packet Seed Mutate Parser Reached Msan Uninitialized Value Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_msan_uninitialized_value`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[ffmpeg-rv40-decoder-packet]]
- related harness facts: [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

## Policy
When `wrong_sink x parser_reached_msan_uninitialized_value` appears for `ffmpeg-rv40-decoder-packet`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Feed the RV40 target decoder a compact raw packet that reaches frame finish with missing or incomplete slice data.
2. The fuzzer allocation leaves some frame buffers uninitialized, and error-resilience filtering reads that content during clipping/filtering after decode finalization.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ffmpeg-rv40-decoder-packet]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[oss-fuzz-run-poc-ffmpeg-target-decoder]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: seed_mutate.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_msan_uninitialized_value`.
- Vulnerability class: `use-of-uninitialized-value`.
- Recovery summary: Feed the RV40 target decoder a compact raw packet that reaches frame finish with missing or incomplete slice data.
