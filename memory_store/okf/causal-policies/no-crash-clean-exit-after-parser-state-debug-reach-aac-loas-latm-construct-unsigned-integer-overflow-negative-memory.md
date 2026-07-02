---
type: causal-policy
title: "No Crash Clean Exit After Parser State Debug Reach Aac Loas Latm Construct Unsigned Integer Overflow Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal clean_exit_after_parser_state_debug_reach."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_parser_state_debug_reach"
candidate_family: "construct"
input_format: "aac-loas-latm"
harness_convention: "afl-stdin-libfuzzer-wrapper"
vuln_class: "unsigned-integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-after-parser-state-debug-reach", "aac-loas-latm", "afl-stdin-libfuzzer-wrapper", "construct", "negative-memory", "round-30"]
match_keys: ["no-crash", "clean-exit-after-parser-state-debug-reach", "aac-loas-latm", "afl-stdin-libfuzzer-wrapper", "unsigned-integer-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Clean Exit After Parser State Debug Reach Aac Loas Latm Construct Unsigned Integer Overflow Negative Memory

- key: `no-crash x clean-exit-after-parser-state-debug-reach`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[aac-loas-latm]]
- harnesses: [[afl-stdin-libfuzzer-wrapper]]

## Failure Shape
A constructed LOAS/LATM ER AAC carrier could reach the HCR escape-word state under debug instrumentation, but the official verifier kept exiting cleanly. Distinct attempts covered payload bit alignment, error-protection configuration, virtual-codebook syntax, short-window syntax, larger scalefactor-band layouts, spectral code patterns, targeted randomized HCR bodies, and a short coverage-guided fuzzing run. The remaining missing condition appears to be a narrower HCR side-info relation that converts the escape-word arithmetic into a sanitizer-visible target failure instead of a clean decode or internal error path.

## Negative Policy
For `no-crash x clean-exit-after-parser-state-debug-reach` on `aac-loas-latm`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[aac-loas-latm]] and [[afl-stdin-libfuzzer-wrapper]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
