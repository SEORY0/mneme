---
type: causal-policy
title: "Vcf Text Construct Text Vcf Parser Reached Target Sanitizer Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_target_sanitizer_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sanitizer_crash"
candidate_family: "construct_text_vcf"
input_format: "vcf-text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sanitizer-crash", "vcf-text", "libfuzzer", "construct-text-vcf", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_target_sanitizer_crash", "vcf-text", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Vcf Text Construct Text Vcf Parser Reached Target Sanitizer Crash Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_sanitizer_crash`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the raw hts_open memory-file harness with a valid text VCF header and record. Keep text parsing on the normal VCF path, then make the ALT list exceed the internal allele-count capacity so the writer later interprets leftover allele encoding as later BCF fields. Shape the first leftover encoded allele so formatting sees a negative INFO key with a minimal value payload, reaching the signed-key check gap in the VCF writer.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[vcf-text]]: VCF text input starts with metadata lines and a tab-separated column header, followed by tab-separated records. ALT alleles are comma-separated in text, but the parser stores alleles in an internal BCF shared block while the record allele count is narrower than the shared payload. On writeback, the internal BCF representation is unpacked and INFO keys are resolved through the header dictionary.
- Harness [[libfuzzer]]: The htslib fuzz harness passes raw input bytes to an in-memory hts_open source. For variant input, it reads the VCF header, writes a header to a null sink, then repeatedly reads records and writes them back through bcf_write/vcf_format. Text VCF records are parsed before writeback, so the raw BCF record checker is not the relevant gate for this construction.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[vcf-text]] and [[libfuzzer]].
