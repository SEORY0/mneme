---
type: causal-policy
title: "Jpeg Construct Wrong Sink Parser Reached Vulnerable Only Target Accepted Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_vulnerable_only_target_accepted."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vulnerable_only_target_accepted"
candidate_family: "construct"
input_format: "jpeg"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "jpeg", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-vulnerable-only-target-accepted", "jpeg", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Jpeg Construct Wrong Sink Parser Reached Vulnerable Only Target Accepted Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_vulnerable_only_target_accepted` on `jpeg` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Build a coherent baseline JPEG rather than only mutating a seed header.
2. Keep SOI, quantization and Huffman tables, a baseline frame, a scan header, and enough entropy-coded zero blocks consistent with the component layout.
3. Use component sampling factors where the maximum factor is not divisible by the chroma component factor, and make the image span enough MCUs that the incorrectly truncated resampling ratio reads beyond allocator alignment padding.
4. The fixed build rejects the fractional sampling relation before the unsafe resample/color-conversion path.

## Format Contract
- Input format: [[jpeg]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `jpeg` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
