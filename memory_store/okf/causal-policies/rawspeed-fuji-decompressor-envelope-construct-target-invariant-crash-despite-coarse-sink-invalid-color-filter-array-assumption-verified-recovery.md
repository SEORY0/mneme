---
type: causal-policy
title: "Rawspeed Fuji Decompressor Envelope Construct Target Invariant Crash Despite Coarse Sink Invalid Color Filter Array Assumption Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal target_invariant_crash_despite_coarse_sink."
failure_class: "wrong_sink"
verifier_signal: "target_invariant_crash_despite_coarse_sink"
candidate_family: "construct"
input_format: "rawspeed-fuji-decompressor-envelope"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "invalid-color-filter-array-assumption"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-invariant-crash-despite-coarse-sink", "rawspeed-fuji-decompressor-envelope", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "target_invariant_crash_despite_coarse_sink", "rawspeed-fuji-decompressor-envelope", "afl-libfuzzer-wrapper", "invalid-color-filter-array-assumption", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Rawspeed Fuji Decompressor Envelope Construct Target Invariant Crash Despite Coarse Sink Invalid Color Filter Array Assumption Verified Recovery

- key: `wrong_sink x target_invariant_crash_despite_coarse_sink`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[rawspeed-fuji-decompressor-envelope]]
- harnesses: [[afl-libfuzzer-wrapper]]

## Failure Shape
The verifier-confirmed candidate preserved the `rawspeed-fuji-decompressor-envelope` parser envelope under `afl-libfuzzer-wrapper` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `target_invariant_crash_despite_coarse_sink` on `rawspeed-fuji-decompressor-envelope` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build the direct Fuji decompressor envelope with valid image metadata, a matching Fuji compressed header, and enough compressed payload to reach row copy. Use a CFA grid that is accepted by the generic CFA parser but contains a color class outside the red, green, and blue cases assumed by Fuji row copying.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The direct rawspeed Fuji fuzzer expects little-endian image metadata and CFA dimensions/entries, followed by a big-endian Fuji compressed header, per-strip compressed sizes, optional alignment padding, and strip payload bytes. Valid Fuji gates include fixed block width, matching rounded width, supported bit depth/type, and total lines matching image height.

## Harness Contract
The AFL-style wrapper feeds the raw file bytes to FujiDecompressorFuzzer. The fuzzer constructs a RawImage, installs the CFA table, creates image storage, runs Fuji decompression, and treats RawSpeed exceptions as non-crashing outcomes.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
