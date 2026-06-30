---
type: causal-policy
title: "Hevc Annex B Elementary Stream Seed Mutate Wrong Sink Parser Reached Target Ubsan Oob Index Undefined Behavior Out Of Bounds Index Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_ubsan_oob_index."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_ubsan_oob_index"
candidate_family: "seed_mutate"
input_format: "hevc-annex-b-elementary-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "undefined-behavior-out-of-bounds-index"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-ubsan-oob-index", "hevc-annex-b-elementary-stream", "libfuzzer-ffmpeg-target-decoder", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-ubsan-oob-index", "hevc-annex-b-elementary-stream", "libfuzzer-ffmpeg-target-decoder", "undefined-behavior-out-of-bounds-index"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Hevc Annex B Elementary Stream Seed Mutate Wrong Sink Parser Reached Target Ubsan Oob Index Undefined Behavior Out Of Bounds Index Verified Recovery

- key: `wrong-sink x parser-reached-target-ubsan-oob-index`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[hevc-annex-b-elementary-stream]]
- harnesses: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
Start from a valid RExt HEVC Annex-B stream that already carries coherent VPS, SPS, PPS, and an intra slice with chroma residual coding. Preserve the NAL ordering and RBSP escaping. In the PPS range-extension area, enable the CU chroma-QP offset-list feature with a legal full list, then add the corresponding slice-header enable bit while keeping the CABAC payload aligned. Finally, perturb a narrow CABAC payload region so the chroma-QP offset index decoder walks one past the last valid list entry; the vulnerable decoder indexes the fixed-size lists while the fixed build rejects the relation.

## Policy
For `wrong-sink x parser-reached-target-ubsan-oob-index` on `hevc-annex-b-elementary-stream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `hevc-annex-b-elementary-stream` carrier enough for the `libfuzzer-ffmpeg-target-decoder` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `hevc-annex-b-elementary-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
