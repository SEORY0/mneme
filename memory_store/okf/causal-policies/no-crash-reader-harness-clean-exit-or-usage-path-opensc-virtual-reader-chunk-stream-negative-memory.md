---
type: causal-policy
title: "No Crash Reader Harness Clean Exit Or Usage Path Opensc Virtual Reader Chunk Stream Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal reader_harness_clean_exit_or_usage_path."
failure_class: "no_crash"
verifier_signal: "reader_harness_clean_exit_or_usage_path"
candidate_family: "construct_and_seed_sweep"
input_format: "opensc virtual-reader chunk stream"
harness_convention: "honggfuzz-style pkcs15 reader harness"
vuln_class: "out-of-bounds-read-before-buffer"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "reader-harness-clean-exit-or-usage-path", "opensc-virtual-reader-chunk-stream", "negative-memory", "round-16"]
match_keys: ["no_crash", "reader_harness_clean_exit_or_usage_path", "opensc virtual-reader chunk stream", "honggfuzz-style pkcs15 reader harness", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Reader Harness Clean Exit Or Usage Path Opensc Virtual Reader Chunk Stream Negative Memory

## Policy
For `no_crash x reader_harness_clean_exit_or_usage_path`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Constructed ITACNS ATR/chunk streams and shipped pkcs15-reader corpus seeds did not bind a card state that reached the described ITACNS backward-read path under the selected wrapper.
- When `no_crash x reader_harness_clean_exit_or_usage_path` appears for `opensc virtual-reader chunk stream`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The OpenSC virtual reader consumes two-byte little-endian chunk lengths followed by chunk data. The first chunk supplies the ATR; later chunks emulate APDU responses with status bytes at the end of each response chunk.
- Harness: The selected binary is the pkcs15-reader harness. It builds an in-memory reader from the raw bytes, connects a card based on the ATR, binds PKCS#15 state, then exercises object crypto operations only if binding produces objects.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
