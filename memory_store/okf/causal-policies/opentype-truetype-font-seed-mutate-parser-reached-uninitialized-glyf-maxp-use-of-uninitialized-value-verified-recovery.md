---
type: causal-policy
title: "Opentype Truetype Font Seed Mutate Parser Reached Uninitialized Glyf Maxp Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for opentype-truetype-font when wrong_sink pairs with parser_reached_uninitialized_glyf_maxp."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_glyf_maxp"
candidate_family: "seed_mutate"
input_format: "opentype-truetype-font"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-uninitialized-glyf-maxp", "opentype-truetype-font", "libfuzzer", "seed-mutate", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-uninitialized-glyf-maxp", "opentype-truetype-font", "libfuzzer", "seed-mutate", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Opentype Truetype Font Seed Mutate Parser Reached Uninitialized Glyf Maxp Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_glyf_maxp`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opentype-truetype-font]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached_uninitialized_glyf_maxp` appears for `opentype-truetype-font`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Start from a small valid in-repository TrueType seed that already contains glyph, location, and maximum-profile tables.
2. Preserve the table directory and glyph data while changing the maximum-profile table version so the parser continues into simple glyph parsing but the version-specific maximum-profile fields are not initialized.
3. Recompute the font integrity fields needed for the mutated table directory so the fixed build can reject or guard the mismatch while the vulnerable build reaches the uninitialized read.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[opentype-truetype-font]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: seed_mutate.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_uninitialized_glyf_maxp`.
- Vulnerability class: `use-of-uninitialized-value`.
- Recovery summary: Start from a small valid in-repository TrueType seed that already contains glyph, location, and maximum-profile tables.
