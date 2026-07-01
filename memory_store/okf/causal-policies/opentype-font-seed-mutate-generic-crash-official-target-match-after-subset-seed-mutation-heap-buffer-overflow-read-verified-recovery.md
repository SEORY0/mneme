---
type: "causal-policy"
title: "Opentype Font Seed Mutate Generic Crash Official Target Match After Subset Seed Mutation Heap Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal official_target_match_after_subset_seed_mutation."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_subset_seed_mutation"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "official-target-match-after-subset-seed-mutation", "opentype-font", "libfuzzer-harfbuzz-subset", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "official_target_match_after_subset_seed_mutation", "opentype-font", "libfuzzer-harfbuzz-subset", "heap-buffer-overflow-read", "verified-recovery", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Opentype Font Seed Mutate Generic Crash Official Target Match After Subset Seed Mutation Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x official_target_match_after_subset_seed_mutation`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-subset]]

## Failure Shape
Start from a real sfnt font seed that already reaches HarfBuzz layout subsetting. Preserve a valid table directory and layout table envelope, keep layout tables retained during subsetting, and append the subset-fuzzer trailer with relevant codepoints. The useful seed reaches malformed contextual layout closure in the subset component; the vulnerable build crashes while the fixed build handles or rejects the relation.

## Policy
When `generic_crash x official_target_match_after_subset_seed_mutation` appears for `[[opentype-font]]` under `[[libfuzzer-harfbuzz-subset]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opentype-font]]` format contract and `[[libfuzzer-harfbuzz-subset]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[opentype-font]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 7 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
