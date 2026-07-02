---
type: causal-policy
title: "Vcf Text Construct Text Vcf Generic Crash Parser Reached Target Function Integer Overflow To Out Of Bounds Write Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_target_function."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_function"
candidate_family: "construct_text_vcf"
input_format: "vcf-text"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-to-out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct-text-vcf", "vcf-text", "integer-overflow-to-out-of-bounds-write", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-target-function", "vcf-text", "libfuzzer", "integer-overflow-to-out-of-bounds-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Vcf Text Construct Text Vcf Generic Crash Parser Reached Target Function Integer Overflow To Out Of Bounds Write Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_target_function` on `vcf-text` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Build a valid text VCF that the hts_open fuzzer recognizes as variant data, with a normal fileformat line, contig metadata, FORMAT metadata, a sample header, and one record.
2. Define multiple string FORMAT fields and many samples.
3. Make earlier string fields large enough that each individual field remains under the per-field memory guard, while their combined allocation advances the per-record FORMAT backing buffer past the signed offset range.
4. Then include a following small FORMAT field so its stored offset wraps in the vulnerable build and is used during sample-field filling; the fixed build rejects the aggregate size.

## Format Contract
- Input format: [[vcf-text]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `vcf-text` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
