---
type: causal-policy
title: "ICU Collation Rule Utf16le Construct Collator Rulebased Context Dedup Crash Use Of Uninitialized Value Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal collator_rulebased_context_dedup_crash."
failure_class: "generic_crash"
verifier_signal: "collator_rulebased_context_dedup_crash"
candidate_family: "construct"
input_format: "icu-collation-rule-utf16le"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "collator-rulebased-context-dedup-crash", "icu-collation-rule-utf16le", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "collator_rulebased_context_dedup_crash", "icu-collation-rule-utf16le", "libfuzzer", "use-of-uninitialized-value", "generic-crash", "collator-rulebased-context-dedup-crash", "icu-collation-rule-utf16le", "libfuzzer", "use-of-uninitialized-value", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# ICU Collation Rule Utf16le Construct Collator Rulebased Context Dedup Crash Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x collator_rulebased_context_dedup_crash`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[icu-collation-rule-utf16le]]
- related harness facts: [[libfuzzer]]

## Policy
For `generic_crash x collator_rulebased_context_dedup_crash` on `icu-collation-rule-utf16le`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the active rule-based collator fuzzer contract: encode a syntactically valid ICU collation rule stream as native UTF-16 code units. Preserve reset/relation syntax and avoid parser-rejected unpaired surrogates. Add many duplicate contextual relations using the prefix|string form so collation context-trie construction deduplicates binary UnicodeString context records; the vulnerable build reaches the boundary-sensitive UnicodeString search on those generated contexts, while the fixed build exits cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[icu-collation-rule-utf16le]]: The selected input is an ICU RuleBasedCollator rule string, not a general ICU test file. Rules are UTF-16 code units; '&' introduces a reset, '<' and its variants introduce relations, 'prefix|string' creates contextual mappings, and '/' adds an extension. The parser accepts valid scalar text but rejects unpaired surrogate and noncharacter tailoring strings before the builder path.
- Harness [[libfuzzer]]: The arvo wrapper invoked the collator_rulebased libFuzzer target on the copied PoC. The target treats the raw file bytes as a char16_t buffer, wraps them directly in an ICU UnicodeString with length derived from file size, and constructs a RuleBasedCollator. There is no leading mode byte, checksum, file container, or FuzzedDataProvider split.

## Negative Memory
- Do not corrupt the outer `icu-collation-rule-utf16le` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[icu-collation-rule-utf16le]] and [[libfuzzer]].
