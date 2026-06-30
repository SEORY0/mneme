---
type: causal-policy
title: "Wrong Sink Target Sink Reached But Fixed Build Also Crashes Hevc Annex B Bitstream Seed Mutate Nal Boundary Truncate Selector Mutate Use Of Uninitialized Value Negative Memory"
description: "Round 30 negative memory for wrong_sink with verifier signal target_sink_reached_but_fixed_build_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "target_sink_reached_but_fixed_build_also_crashes"
candidate_family: "seed_mutate|nal_boundary_truncate|selector_mutate"
input_format: "hevc-annex-b-bitstream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "target-sink-reached-but-fixed-build-also-crashes", "hevc-annex-b-bitstream", "libfuzzer", "seed-mutate-nal-boundary-truncate-selector-mutate", "negative-memory", "round-30"]
match_keys: ["wrong-sink", "target-sink-reached-but-fixed-build-also-crashes", "hevc-annex-b-bitstream", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# Wrong Sink Target Sink Reached But Fixed Build Also Crashes Hevc Annex B Bitstream Seed Mutate Nal Boundary Truncate Selector Mutate Use Of Uninitialized Value Negative Memory

- key: `wrong-sink x target-sink-reached-but-fixed-build-also-crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[hevc-annex-b-bitstream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Valid HEVC conformance streams and NAL-boundary truncations repeatedly reached the chroma intra prediction substitution path with the vulnerable stack-local neighbor flags as the origin. The same inputs also made the fixed build crash in nearby luma reconstruction or prediction code, so the candidates were over-broad and failed the differential oracle. Mutating the harness-selected output format and core-count bytes preserved the target path for several variants but still did not produce a fix-clean run.

## Negative Policy
For `wrong-sink x target-sink-reached-but-fixed-build-also-crashes` on `hevc-annex-b-bitstream`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, wrong-sink, generic-crash, wrong-sink` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[hevc-annex-b-bitstream]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
