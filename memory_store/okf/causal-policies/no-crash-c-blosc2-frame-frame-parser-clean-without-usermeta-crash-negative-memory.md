---
type: causal-policy
title: "No Crash C Blosc2 Frame Frame Parser Clean Without Usermeta Crash Negative Memory"
description: "Negative memory for no_crash with frame_parser_clean_without_usermeta_crash on c-blosc2-frame inputs."
failure_class: no_crash
verifier_signal: frame_parser_clean_without_usermeta_crash
candidate_family: seed_mutate
input_format: c-blosc2-frame
harness_convention: libfuzzer-decompress-frame
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, frame-parser-clean-without-usermeta-crash, c-blosc2-frame, heap-buffer-overflow-read, negative_memory]
match_keys: [no-crash, frame-parser-clean-without-usermeta-crash, c-blosc2-frame, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash C Blosc2 Frame Frame Parser Clean Without Usermeta Crash Negative Memory

- key: `no_crash x frame_parser_clean_without_usermeta_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[c-blosc2-frame]]

## Dead End
Valid in-repo Blosc2 frame seeds reached the decompress-frame target, but mutating only the trailer usermeta length across boundary and large regimes, and mutating only the trailer length field across short and overlong regimes, exited cleanly. Official submit for the largest bounded usermeta-length mutation also exited clean, so the missing trigger is likely another accepted frame-size/trailer-offset relation rather than the usermeta length field alone.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
