---
type: causal-policy
title: "VCF N Allele 16bit Wrap Negative Info Key Out Of Bounds Read Verified Recovery"
description: "Verified recovery for no_crash where a 16-bit allele-count wrap yields a negative INFO key that vcf_format indexes without a lower-bound check."
failure_class: "no_crash"
verifier_signal: "parser_reached_negative_info_key_unchecked"
candidate_family: "construct"
input_format: "vcf-bcf"
harness_convention: "htslib-hts-open-fuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "vcf-bcf", "out-of-bounds-read", "integer-wrap", "verified-recovery"]
match_keys: ["no_crash", "parser_reached_negative_info_key_unchecked", "vcf-bcf", "htslib-hts-open-fuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# VCF N Allele 16bit Wrap Negative Info Key Out Of Bounds Read Verified Recovery

## Policy
For `no_crash` on the htslib `hts_open` fuzzer (mem: -> view_vcf -> bcf_write), the bug is a negative-index
OOB read in `vcf_format`: it checks only the upper bound (`z->key >= n`) of an INFO key, not the lower bound
(`z->key < 0`). Reach it by overflowing the 16-bit allele count so the record encoding desynchronizes and a
crafted leftover byte is reinterpreted as a negative INT8 INFO key.

## Procedure
1. Build a BCF record whose `n_allele` field (16-bit) exceeds 65535 so it wraps to a small value;
   `bcf_unpack` then consumes fewer allele encodings than were written.
2. Lay out the leftover allele bytes so they are reinterpreted as a FILTER/INFO block whose INFO key
   decodes to a NEGATIVE INT8 value.
3. The VCF formatter (`vcf_format`) indexes `h->id[BCF_DT_ID][z->key]` with that negative key -> heap OOB
   read. The fix adds the `z->key < 0` lower-bound check.
4. Construct from a minimal valid BCF (header + one record); minimum-margin: only the allele-count wrap +
   the one negative-key byte differ from a valid record. Confirm fix exits 0.

## Format Contract
- See [[vcf-bcf]]. The harness opens the input as BCF in memory and re-serializes to VCF, so both the BCF
  binary record layout (shared header dict indices, typed vectors) and the VCF formatter path are exercised.

## Negative Memory
- Do not corrupt the header dictionary itself (crashes both builds / bad_format); keep it valid and only
  wrap the allele count + craft the one negative key.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
