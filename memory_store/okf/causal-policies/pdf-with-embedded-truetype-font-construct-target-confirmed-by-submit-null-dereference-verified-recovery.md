---
type: causal-policy
title: Pdf With Embedded Truetype Font Target Confirmed By Submit Verified Recovery
description: Server-verified recovery for pdf-with-embedded-truetype-font when generic_crash pairs with target_confirmed_by_submit.
failure_class: generic_crash
verifier_signal: target_confirmed_by_submit
candidate_family: construct
input_format: pdf-with-embedded-truetype-font
harness_convention: libfuzzer-poppler-qt-pdf
vuln_class: null-dereference
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, target-confirmed-by-submit, pdf-with-embedded-truetype-font, libfuzzer-poppler-qt-pdf, construct, null-dereference, verified-recovery]
match_keys: [generic-crash, target-confirmed-by-submit, pdf-with-embedded-truetype-font, libfuzzer-poppler-qt-pdf, construct, null-dereference, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a pdf-with-embedded-truetype-font candidate reaches `target_confirmed_by_submit` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-poppler-qt-pdf]]` and format contract `[[pdf-with-embedded-truetype-font]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use a complete enough PDF wrapper to make the Qt Poppler fuzzer load and render a page, and reference an embedded TrueType font stream through normal page font resources. The embedded font must be structurally recognizable as a TrueType face but omit required table data so font parsing proceeds into the missing-table case; the fixed build handles the absent table, while the vulnerable build dereferences invalid parser state.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
