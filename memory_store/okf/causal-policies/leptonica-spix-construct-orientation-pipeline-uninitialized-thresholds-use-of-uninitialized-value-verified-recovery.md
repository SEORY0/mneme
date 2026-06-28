---
type: causal-policy
title: "Leptonica Spix Construct Orientation Pipeline Uninitialized Thresholds Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for leptonica-spix when generic_crash pairs with orientation_pipeline_uninitialized_thresholds."
failure_class: "generic_crash"
verifier_signal: "orientation_pipeline_uninitialized_thresholds"
candidate_family: "construct"
input_format: "leptonica-spix"
harness_convention: "libfuzzer-raw-spix"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "orientation-pipeline-uninitialized-thresholds", "leptonica-spix", "libfuzzer-raw-spix", "construct", "verified-recovery", "round-17"]
match_keys: ["generic-crash", "orientation-pipeline-uninitialized-thresholds", "leptonica-spix", "libfuzzer-raw-spix", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Leptonica Spix Construct Orientation Pipeline Uninitialized Thresholds Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x orientation_pipeline_uninitialized_thresholds`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[leptonica-spix]]
- related harness facts: [[libfuzzer-raw-spix]]

## Policy
When `generic_crash x orientation_pipeline_uninitialized_thresholds` appears for `leptonica-spix`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Provide a valid serialized 1-bpp PIX with a simple horizontal text-like pattern so the flip/orientation pipeline runs.
2. The harness passes uninitialized confidence-threshold locals into the orientation correction call, and a pattern that exercises the decision path exposes the uninitialized use.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[leptonica-spix]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-raw-spix]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
