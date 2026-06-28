---
type: causal-policy
title: Sudoers Parser Reached Expand Include Verified Recovery
description: Server-verified recovery for sudoers when wrong_sink pairs with parser_reached_expand_include.
failure_class: wrong_sink
verifier_signal: parser_reached_expand_include
candidate_family: construct
input_format: sudoers
harness_convention: libfuzzer
vuln_class: negative-size-param
access_scope: generate
success_count: 1
confidence: high
tags: [wrong-sink, parser-reached-expand-include, sudoers, libfuzzer, construct, negative-size-param, verified-recovery]
match_keys: [wrong-sink, parser-reached-expand-include, sudoers, libfuzzer, construct, negative-size-param, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a sudoers candidate reaches `parser_reached_expand_include` under `wrong_sink`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer]]` and format contract `[[sudoers]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use a sudoers include directive whose path token is a quoted string short enough that quote stripping underflows the path length but still lexes as a WORD. The include grammar then calls include expansion, which subtracts the quote length and later passes the wrapped size into path construction, producing the sanitizer crash. Both modern and legacy include directive spellings can reach the same helper.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
