---
type: causal-policy
title: Hunspell Aff Dic Word Triple Official Target Match After Submit Verified Recovery
description: Server-verified recovery for hunspell aff/dic/word triple when wrong_sink pairs with official_target_match_after_submit.
failure_class: wrong_sink
verifier_signal: official_target_match_after_submit
candidate_family: construct
input_format: hunspell aff/dic/word triple
harness_convention: libfuzzer FuzzedDataProvider-like splitter
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: high
tags: [wrong-sink, official-target-match-after-submit, hunspell-aff-dic-word-triple, libfuzzer-fuzzeddataprovider-like-splitter, construct, heap-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, official-target-match-after-submit, hunspell-aff-dic-word-triple, libfuzzer-fuzzeddataprovider-like-splitter, construct, heap-buffer-overflow-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a hunspell aff/dic/word triple candidate reaches `official_target_match_after_submit` under `wrong_sink`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-fuzzeddataprovider-like-splitter]]` and format contract `[[hunspell-aff-dic-word-triple]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use the harness splitter to create a short misspelled word, a dictionary containing at least one valid entry, and an affix file that declares UTF-8 then places malformed UTF-8 in a suggestion-relevant table. The spell check falls through to suggestion generation, which consumes the malformed affix data and reaches the fixed bug despite the local verifier classifying the stack imprecisely.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
