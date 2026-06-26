---
type: causal-policy
title: Blosc2 Frame Trailer Extent
description: Verified recovery for no_crash with local_wrapper_mismatch_official_target_match on c-blosc2-frame inputs.
failure_class: no_crash
verifier_signal: local_wrapper_mismatch_official_target_match
candidate_family: seed_mutate
input_format: c-blosc2-frame
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [no-crash, local-wrapper-mismatch-official-target-match, seed-mutate, c-blosc2-frame, verified_recovery]
match_keys: [no-crash, local-wrapper-mismatch-official-target-match, c-blosc2-frame, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Blosc2 Frame Trailer Extent

- key: `no_crash x local_wrapper_mismatch_official_target_match`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[c-blosc2-frame]]

## Failure Shape
A prior candidate family produced `no_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `c-blosc2-frame` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Start from a valid contiguous c-blosc2 frame so the frame header, magic, declared frame size, codec metadata, and trailer marker are accepted. Mutate only the trailer metadata so the parser believes a trailer extends beyond the actual frame boundary; the vulnerable build trusts that trailer extent while constructing the super-chunk, while the fixed build rejects the inconsistent frame.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `no_crash` toward `local_wrapper_mismatch_official_target_match`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.
