---
type: causal-policy
title: "Mvg Construct Parser Reached Renderer Crash Renderer Path Buffer Overflow Verified Recovery"
description: "Server-verified recovery for mvg when generic_crash pairs with parser_reached_renderer_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_renderer_crash"
candidate_family: "construct"
input_format: "mvg"
harness_convention: "graphicsmagick-mvg-raw-file"
vuln_class: "renderer-path-buffer-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-renderer-crash", "mvg", "graphicsmagick-mvg-raw-file", "construct", "verified-recovery", "round-17"]
match_keys: ["generic-crash", "parser-reached-renderer-crash", "mvg", "graphicsmagick-mvg-raw-file", "construct", "renderer-path-buffer-overflow", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Mvg Construct Parser Reached Renderer Crash Renderer Path Buffer Overflow Verified Recovery

- key: `generic_crash x parser_reached_renderer_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[mvg]]
- related harness facts: [[graphicsmagick-mvg-raw-file]]

## Policy
When `generic_crash x parser_reached_renderer_crash` appears for `mvg`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use a minimal line-oriented MVG drawing with a valid canvas declaration and a single ellipse primitive.
2. Keep the syntax and angle fields ordinary, then make the ellipse radii large enough that primitive tracing crosses the renderer allocation boundary.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[mvg]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[graphicsmagick-mvg-raw-file]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
