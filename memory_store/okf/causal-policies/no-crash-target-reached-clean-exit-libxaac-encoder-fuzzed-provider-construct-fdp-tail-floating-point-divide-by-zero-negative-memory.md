---
type: negative-memory
title: "No Crash Target Reached Clean Exit Libxaac Encoder Fuzzed Provider Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal target_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "target_reached_clean_exit"
candidate_family: "construct-fdp-tail"
input_format: "libxaac-encoder-fuzzed-provider"
harness_convention: "libfuzzer-fuzzed-data-provider"
vuln_class: "floating-point-divide-by-zero"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "target-reached-clean-exit", "libxaac-encoder-fuzzed-provider", "libfuzzer-fuzzed-data-provider", "construct-fdp-tail", "floating-point-divide-by-zero", "negative-memory", "round-28"]
match_keys: ["no_crash", "target_reached_clean_exit", "libxaac-encoder-fuzzed-provider", "libfuzzer-fuzzed-data-provider", "floating-point-divide-by-zero", "negative_memory", "construct", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Target Reached Clean Exit Libxaac Encoder Fuzzed Provider Negative Memory

- key: `no_crash x target_reached_clean_exit`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[libxaac-encoder-fuzzed-provider]]
- harnesses: [[libfuzzer-fuzzed-data-provider]]

## Dead-End Shape
The encoder configuration can be constructed to reach the USAC DRC STFT gain-calculator initializer and the later DRC process path, but the local build treats the vulnerable floating-point divisions as ordinary non-trapping FP operations. Tried identical zero coordinates, vertical same-x segments with nonzero gain and width, gain-sequence processing, a wider test-config-like DRC envelope, high-amplitude process input, and a nonzero-x vertical segment that forces the implicit terminal point; all executed cleanly without a sanitizer-visible failure.

## Policy
For `no_crash x target_reached_clean_exit` on `libxaac-encoder-fuzzed-provider`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct-fdp-tail` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[libxaac-encoder-fuzzed-provider]]: The input is an encoder configuration stream rather than an AAC bitstream. Back-consumed scalar fields choose bitrate, transport flags, tool flags, PCM width, channel count, sample-rate selection, frame length, USAC/AOT controls, SBR-related controls, DRC enablement, codec mode, and then a DRC config. A DRC config contains instruction records, coefficient records, gain-set records, per-band gain points, optional loudness records, channel-layout fields, downmix records, and extension flags. Multi-band gain sets select the STFT DRC gain-calculation path; equal x coordinates are accepted by the monotonicity check because it only rejects strictly decreasing x.
- Harness [[libfuzzer-fuzzed-data-provider]]: The libFuzzer harness wraps the entire file in FuzzedDataProvider. Integral, boolean, table-pick, and floating-point configuration fields are consumed from the back in source order, so the file stores those fields in reverse source order. Remaining front bytes, if any, drive encoder process iterations; the per-frame process selector is also read from the back of that remaining front region, while selected sample bytes can be copied from the front or synthesized from a back-consumed fill byte.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
