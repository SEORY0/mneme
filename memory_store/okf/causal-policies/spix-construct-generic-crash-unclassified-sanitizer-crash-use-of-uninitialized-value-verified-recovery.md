---
type: causal-policy
title: "Spix Construct Generic Crash Unclassified Sanitizer Crash Use Of Uninitialized Value Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal unclassified_sanitizer_crash."
failure_class: "generic_crash"
verifier_signal: "unclassified_sanitizer_crash"
candidate_family: "construct"
input_format: "spix"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "unclassified-sanitizer-crash", "spix", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "unclassified_sanitizer_crash", "spix", "libfuzzer", "use-of-uninitialized-value", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Spix Construct Generic Crash Unclassified Sanitizer Crash Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x unclassified_sanitizer_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[spix]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a valid serialized Leptonica Pix carrier with internally consistent dimensions, word-stride, and raster-size fields. Use a 1bpp page-shaped raster with enough long horizontal textline-like bands across both halves of the page so the dewarp debug model path creates debug images and calls the directory-to-PDF helper; the vulnerable build uses an unchecked directory canonicalization result on that debug path, while the fixed build exits cleanly.

## Policy
When `generic_crash x unclassified_sanitizer_crash` appears for `spix` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[spix]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `spix` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 77, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
