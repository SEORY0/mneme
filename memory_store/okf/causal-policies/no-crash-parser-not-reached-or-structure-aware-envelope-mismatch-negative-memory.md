---
type: causal-policy
title: No Crash Parser Not Reached Or Structure Aware Envelope Mismatch Negative Memory
description: Negative memory for no_crash with verifier signal parser_not_reached_or_structure_aware_envelope_mismatch.
failure_class: no_crash
verifier_signal: parser_not_reached_or_structure_aware_envelope_mismatch
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached-or-structure-aware-envelope-mismatch, negative_memory]
match_keys: [no-crash, parser-not-reached-or-structure-aware-envelope-mismatch, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Not Reached Or Structure Aware Envelope Mismatch Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x parser_not_reached_or_structure_aware_envelope_mismatch`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: png

### Procedure
Treat this as an envelope or harness-shape failure. Rebuild the carrier around the exact fuzzer input contract, confirm parser reachability, then add one target invariant.

### Diagnosed Dead Ends
- Constructed valid PNG envelopes with eXIf chunks that violated the empty-payload invariant, including alternate chunk placement. The wrapper did not expose a sanitizer-visible eXIf crash, likely because the structure-aware harness envelope or parser path differed from raw PNG assumptions.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
