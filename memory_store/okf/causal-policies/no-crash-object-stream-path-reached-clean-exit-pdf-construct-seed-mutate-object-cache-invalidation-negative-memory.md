---
type: causal-policy
title: "No Crash Object Stream Path Reached Clean Exit Pdf Construct Seed Mutate Object Cache Invalidation Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal object_stream_path_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "object_stream_path_reached_clean_exit"
candidate_family: "construct+seed_mutate"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "object-cache-invalidation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "object-stream-path-reached-clean-exit", "pdf", "libfuzzer", "construct-seed-mutate", "negative-memory", "round-30"]
match_keys: ["no-crash", "object-stream-path-reached-clean-exit", "pdf", "libfuzzer", "object-cache-invalidation", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Object Stream Path Reached Clean Exit Pdf Construct Seed Mutate Object Cache Invalidation Negative Memory

- key: `no-crash x object-stream-path-reached-clean-exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer]]

## Failure Shape
Seed PDFs and incremental mutations reached QPDF object-stream preservation/generation paths and produced warnings for older compressed objects coexisting with newer generation entries, but the sanitizer did not report the target crash. The remaining gap is likely the precise traversal/cache lifetime pattern needed after getCompressibleObjGens removes an older object while another generation of the same object number is cached.

## Negative Policy
For `no-crash x object-stream-path-reached-clean-exit` on `pdf`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[pdf]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
