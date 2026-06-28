---
type: causal-policy
title: Mvg Parser Reached Renderer Crash Verified Recovery
description: Server-verified recovery for mvg when generic_crash pairs with parser_reached_renderer_crash.
failure_class: generic_crash
verifier_signal: parser_reached_renderer_crash
candidate_family: construct
input_format: mvg
harness_convention: libfuzzer-graphicsmagick-mvg
vuln_class: arithmetic-overflow-to-renderer-crash
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, parser-reached-renderer-crash, mvg, libfuzzer-graphicsmagick-mvg, construct, arithmetic-overflow-to-renderer-crash, verified-recovery]
match_keys: [generic-crash, parser-reached-renderer-crash, mvg, libfuzzer-graphicsmagick-mvg, construct, arithmetic-overflow-to-renderer-crash, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a mvg candidate reaches `parser_reached_renderer_crash` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-graphicsmagick-mvg]]` and format contract `[[mvg]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use a raw MVG document with a valid initial canvas declaration and a single ellipse primitive. Keep the canvas ordinary but make the ellipse radius relation exceed the renderer's point-allocation arithmetic range while otherwise using normal numeric fields, so the vulnerable renderer overflows during ellipse tracing and the fixed build rejects or avoids the bad allocation.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
