---
type: negative-memory
title: "No Crash Fuzztest Ir Accepted No Asan Webp Riff Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal fuzztest_ir_accepted_no_asan."
failure_class: "no_crash"
verifier_signal: "fuzztest_ir_accepted_no_asan"
candidate_family: "seed_mutate"
input_format: "webp-riff"
harness_convention: "fuzztest"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "fuzztest-ir-accepted-no-asan", "webp-riff", "fuzztest", "seed-mutate", "out-of-bounds-read", "negative-memory", "round-28"]
match_keys: ["no_crash", "fuzztest_ir_accepted_no_asan", "webp-riff", "fuzztest", "out-of-bounds-read", "negative_memory", "seed-mutate", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Fuzztest Ir Accepted No Asan Webp Riff Negative Memory

- key: `no_crash x fuzztest_ir_accepted_no_asan`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[webp-riff]]
- harnesses: [[fuzztest]]

## Dead-End Shape
Raw WebP bytes were rejected by the FuzzTest corpus parser, so later attempts wrapped real WebP seeds as the string argument and set the mux/demux selector through the FuzzTest IR. Mutations covered trailing chunks outside the RIFF boundary, metadata chunks crossing the boundary, declared metadata reaching physical EOF, VP8X metadata-flag consistency, partial RIFF sizes larger than the buffer, mux copy-mode selection, and animation-frame boundary variants. All accepted inputs exited without an ASAN-visible crash.

## Policy
For `no_crash x fuzztest_ir_accepted_no_asan` on `webp-riff`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `seed_mutate` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[webp-riff]]: WebP containers use a RIFF envelope with a WEBP form tag and chunk records. Chunks carry a four-character tag, a little-endian payload length, payload bytes, and padding for odd payload sizes. Extended WebP starts with VP8X and feature flags; metadata chunks are only stored by demux when the matching feature flag is present, and animation files combine VP8X, ANIM, and ANMF records.
- Harness [[fuzztest]]: The generated target is a FuzzTest harness, not a raw libFuzzer byte contract. Reproducer files must be serialized as FuzzTest IR containing a string argument for the WebP bytes and a boolean argument selecting mux versus demux. Inside the harness, the mux path calls WebPMuxCreate and then chunk/frame accessors; the demux path uses WebPDemux or WebPDemuxPartial depending on the WebP string length and then queries metadata chunks and frames.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
