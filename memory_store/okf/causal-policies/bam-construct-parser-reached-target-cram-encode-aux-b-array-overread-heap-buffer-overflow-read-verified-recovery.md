---
type: causal-policy
title: "Bam Construct Parser Reached Target Cram Encode Aux B Array Overread Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for bam when wrong_sink pairs with parser_reached_target_cram_encode_aux_b_array_overread."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_cram_encode_aux_b_array_overread"
candidate_family: "construct"
input_format: "bam"
harness_convention: "libfuzzer-raw-htslib-hts-open"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-cram-encode-aux-b-array-overread", "bam", "libfuzzer-raw-htslib-hts-open", "construct", "verified-recovery", "round-31"]
match_keys: ["wrong-sink", "parser-reached-target-cram-encode-aux-b-array-overread", "bam", "libfuzzer-raw-htslib-hts-open", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 31
---
# Bam Construct Parser Reached Target Cram Encode Aux B Array Overread Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_cram_encode_aux_b_array_overread`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[bam]]
- related harness facts: [[libfuzzer-raw-htslib-hts-open]]

## Policy
When `wrong_sink x parser_reached_target_cram_encode_aux_b_array_overread` appears for `bam`, preserve accepted sequence-record parsing and target CRAM writeback aux encoding rather than generic BAM rejection.

## Procedure
1. Construct a valid compressed BAM stream with a normal header and an accepted unmapped alignment record.
2. Keep qname, sequence, and quality fields self-consistent and avoid CIGAR/reference requirements that stop CRAM writeback.
3. End aux data with a non-CG B-array tag whose subtype is present but whose element-count field is truncated at the record allocation boundary.
4. Size the logical record with HTSlib allocation rounding in mind so CRAM auxiliary encoding performs the cross-boundary count read.

## Format Contract
Use [[bam]]; preserve BGZF/BAM header and record consistency while mutating only the terminal aux B-array boundary relation.

## Harness Contract
Use [[libfuzzer-raw-htslib-hts-open]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 31 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_target_cram_encode_aux_b_array_overread`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: The verified split reached cram_encode_aux on a boundary-ending B-array aux field that the fixed build rejects cleanly.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, clean parser reachability, or fixed-build crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
