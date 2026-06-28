---
type: causal-policy
title: Hevc Elementary Stream Target Match Verified Recovery
description: Server-verified recovery for hevc elementary stream when generic_crash pairs with target_match.
failure_class: generic_crash
verifier_signal: target_match
candidate_family: construct
input_format: hevc elementary stream
harness_convention: libfuzzer
vuln_class: memory-uninitialized-use
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, target-match, hevc-elementary-stream, libfuzzer, construct, memory-uninitialized-use, verified-recovery]
match_keys: [generic-crash, target-match, hevc-elementary-stream, libfuzzer, construct, memory-uninitialized-use, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a hevc elementary stream candidate reaches `target_match` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer]]` and format contract `[[hevc-elementary-stream]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use the raw HEVC decoder fuzzer contract and provide a compact elementary stream that passes initial decoder setup, selects a supported output format/core count through harness-controlled bytes, then feeds parameter-set and slice-like NAL units sufficient to enter frame decoding and the SAO CTB shifting path. The trigger is an under-specified decoded state that leaves SAO data uninitialized before it is consumed during frame processing.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
