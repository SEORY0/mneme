---
type: causal-policy
title: "Hevc Elementary Stream Seed Sweep Wrong Sink Parser Reached Use Of Uninitialized Value Near Decoder Reconstruction Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_use_of_uninitialized_value_near_decoder_reconstruction."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_use_of_uninitialized_value_near_decoder_reconstruction"
candidate_family: "seed_sweep"
input_format: "hevc-elementary-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "seed-sweep", "hevc-elementary-stream", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-use-of-uninitialized-value-near-decoder-reconstruction", "hevc-elementary-stream", "libfuzzer", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Hevc Elementary Stream Seed Sweep Wrong Sink Parser Reached Use Of Uninitialized Value Near Decoder Reconstruction Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_use_of_uninitialized_value_near_decoder_reconstruction` on `hevc-elementary-stream` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a real HEVC elementary-stream seed rather than a handcrafted stub, preserving coherent parameter sets, slice data, and reconstruction state.
2. The raw stream must remain decoder-valid while the harness-selected decode options stay in supported ranges.
3. A seed that naturally drives picture reconstruction with underspecified neighboring state can produce the vulnerable uninitialized-use behavior; submit even when local triage labels a nearby reconstruction helper instead of the named SAO function, because the fixed build is the reliable discriminator.

## Format Contract
- Input format: [[hevc-elementary-stream]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `hevc-elementary-stream` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
