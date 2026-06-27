---
type: causal-policy
title: "No Crash Vcf Parser Reached Clean Or Record Too Small Vcf Text Construct Text Vcf Integer Overflow Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal vcf_parser_reached_clean_or_record_too_small."
failure_class: "no_crash"
verifier_signal: "vcf_parser_reached_clean_or_record_too_small"
candidate_family: "construct_text_vcf"
input_format: "vcf-text"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "vcf-parser-reached-clean-or-record-too-small", "vcf-text", "negative-memory", "round-14"]
match_keys: ["no_crash", "vcf_parser_reached_clean_or_record_too_small", "vcf-text", "libfuzzer", "integer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Vcf Parser Reached Clean Or Record Too Small Vcf Text Construct Text Vcf Integer Overflow Negative Memory

- key: `no_crash x vcf_parser_reached_clean_or_record_too_small`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[vcf-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The VCF envelope parsed cleanly, but the candidate did not create enough combined FORMAT-field allocation pressure to overflow the per-record accumulated offset. A useful next attempt would need many FORMAT columns and sample columns while keeping each individual field under the per-field guard.

## Policy
Treat `no_crash x vcf_parser_reached_clean_or_record_too_small` on `vcf-text` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
