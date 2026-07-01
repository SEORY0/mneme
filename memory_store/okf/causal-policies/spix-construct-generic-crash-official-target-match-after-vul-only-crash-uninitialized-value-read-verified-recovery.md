---
type: causal-policy
title: "Spix Construct Generic Crash Official Target Match After Vul Only Crash Uninitialized Value Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal official_target_match_after_vul_only_crash."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_vul_only_crash"
candidate_family: "construct"
input_format: "spix"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match-after-vul-only-crash", "spix", "libfuzzer", "construct", "uninitialized-value-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "official_target_match_after_vul_only_crash", "spix", "libfuzzer", "uninitialized-value-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Spix Construct Generic Crash Official Target Match After Vul Only Crash Uninitialized Value Read Verified Recovery

- key: `generic_crash x official_target_match_after_vul_only_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[spix]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a structurally valid serialized Leptonica PIX: magic, dimensions, depth, word stride, zero colormap count, and raster byte count all consistent with the raster. Use a modest grayscale raster with foreground/background variation so the page-segmentation harness reaches its analysis path; the vulnerable build then trips the unterminated generated text buffer while the fixed build rejects the overread.

## Policy
When `generic_crash x official_target_match_after_vul_only_crash` appears for `spix` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

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
- Support: server-verified round 37 solve after 2 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
