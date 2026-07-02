---
type: causal-policy
title: "3dgs Mdl5 Seed Mutate Generic Crash Parser Reached Target Material Texture Scan Integer Overflow To Heap Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_material_texture_scan."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_material_texture_scan"
candidate_family: "seed_mutate"
input_format: "3dgs-mdl5"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-to-heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-material-texture-scan", "3dgs-mdl5", "libfuzzer", "seed-mutate", "integer-overflow-to-heap-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_material_texture_scan", "3dgs-mdl5", "libfuzzer", "integer-overflow-to-heap-buffer-overflow-read", "generic-crash", "parser-reached-target-material-texture-scan", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# 3dgs Mdl5 Seed Mutate Generic Crash Parser Reached Target Material Texture Scan Integer Overflow To Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_material_texture_scan`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[3dgs-mdl5]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Start from a valid 3D GameStudio MDL model with an embedded skin so Assimp selects the MDL importer and reaches material setup. Preserve the model carrier and skin type, then make the embedded texture dimensions nonzero while their unsigned pixel-count product wraps to zero. The vulnerable build allocates an empty texel array, then material color replacement scans it as if a texture exists and reads past the allocation; the fixed build rejects the inconsistent dimension product.

## Policy
When `generic_crash x parser_reached_target_material_texture_scan` appears for `3dgs-mdl5` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[3dgs-mdl5]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `3dgs-mdl5` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 3 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and retargeting only.
