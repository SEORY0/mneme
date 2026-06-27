---
type: causal-policy
title: "No Crash Pkcs15 Reader Clean Exit Opensc Virtual Reader Chunk Stream Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal pkcs15_reader_clean_exit."
failure_class: "no_crash"
verifier_signal: "pkcs15_reader_clean_exit"
candidate_family: "construct_and_seed_sweep"
input_format: "opensc virtual-reader chunk stream"
harness_convention: "libfuzzer pkcs15 reader harness"
vuln_class: "state-corruption-side-effect"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15-reader-clean-exit", "opensc-virtual-reader-chunk-stream", "negative-memory", "round-16"]
match_keys: ["no_crash", "pkcs15_reader_clean_exit", "opensc virtual-reader chunk stream", "libfuzzer pkcs15 reader harness", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Pkcs15 Reader Clean Exit Opensc Virtual Reader Chunk Stream Negative Memory

## Policy
For `no_crash x pkcs15_reader_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- IDPrime ATR/chunk construction and the available pkcs15-reader corpus seeds executed cleanly; the attempts did not produce the specific IDPrime state mutation side effect described in the task.
- When `no_crash x pkcs15_reader_clean_exit` appears for `opensc virtual-reader chunk stream`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The IDPrime path is selected by a matching smart-card ATR, then further behavior depends on APDU response chunks that drive application selection, index processing, and private object list construction.
- Harness: The harness consumes the raw file as a sequence of virtual-reader chunks, with the first chunk becoming the ATR and later chunks serving card responses. PKCS#15 object operations are only reached after successful card connection and binding.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
