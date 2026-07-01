---
type: causal-policy
title: "Hevc Annex B Elementary Stream Construct Wrong Sink Parser Reached Target Origin Fixed Clean Use Of Uninitialized Value Verified Recovery"
description: "Round 34 verified recovery for hevc-annex-b-elementary-stream when wrong_sink pairs with parser_reached_target_origin_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_origin_fixed_clean"
candidate_family: "construct"
input_format: "hevc-annex-b-elementary-stream"
harness_convention: "libfuzzer-raw-libhevc-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-origin-fixed-clean", "hevc-annex-b-elementary-stream", "libfuzzer-raw-libhevc-decoder", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-target-origin-fixed-clean", "hevc-annex-b-elementary-stream", "libfuzzer-raw-libhevc-decoder", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Hevc Annex B Elementary Stream Construct Wrong Sink Parser Reached Target Origin Fixed Clean Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_target_origin_fixed_clean`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[hevc-annex-b-elementary-stream]]
- related harness facts: [[libfuzzer-raw-libhevc-decoder]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_target_origin_fixed_clean`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `use-of-uninitialized-value`
- related format facts: [[hevc-annex-b-elementary-stream]]
- related harness facts: [[libfuzzer-raw-libhevc-decoder]]

### Policy
When `wrong_sink x parser_reached_target_origin_fixed_clean` appears for `hevc-annex-b-elementary-stream`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-raw-libhevc-decoder]] harness contract and the [[hevc-annex-b-elementary-stream]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use a compact raw HEVC Annex-B elementary stream that preserves VPS, SPS, PPS, and an intra-coded VCL unit with chroma present and small transform units. The useful carrier reaches CTB reconstruction and chroma intra reference substitution; the trigger is a 4x4 luma-neighbor flag array state where not all per-quadrant luma flags are initialized before the chroma path combines them. Avoid broad conformance streams that also expose unrelated luma prediction uninitialized reads in both builds.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is a raw HEVC elementary stream, not a container. Start-code-delimited parameter-set NAL units must precede the VCL slice. Streams with coherent intra prediction, chroma enabled, and small transform-unit structure reach the target CTB reconstruction path; arbitrary parameter-set stubs, late truncation, or unrelated multi-frame carriers either decode cleanly or crash in unrelated prediction/filtering code.

### Harness Contract
The libFuzzer target consumes the whole file as decoder bytes. Two early bytes select output color format and core count, but those bytes remain part of the stream; there is no FuzzedDataProvider split, checksum, file wrapper, or length prefix. The harness first decodes headers, allocates output buffers based on decoded or default dimensions, then repeatedly feeds the remaining raw bytes to frame decode.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_target_origin_fixed_clean`.
- Vulnerability class: `use-of-uninitialized-value`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
