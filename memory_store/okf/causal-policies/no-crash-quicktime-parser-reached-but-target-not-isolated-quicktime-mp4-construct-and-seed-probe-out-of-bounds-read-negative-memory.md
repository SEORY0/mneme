---
type: causal-policy
title: "No Crash Quicktime Parser Reached But Target Not Isolated Quicktime Mp4 Construct And Seed Probe Out Of Bounds Read Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal quicktime_parser_reached_but_target_not_isolated."
failure_class: "no_crash"
verifier_signal: "quicktime_parser_reached_but_target_not_isolated"
candidate_family: "construct_and_seed_probe"
input_format: "quicktime-mp4"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "quicktime-parser-reached-but-target-not-isolated", "quicktime-mp4", "libfuzzer", "construct-and-seed-probe", "negative-memory", "round-30"]
match_keys: ["no-crash", "quicktime-parser-reached-but-target-not-isolated", "quicktime-mp4", "libfuzzer", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Quicktime Parser Reached But Target Not Isolated Quicktime Mp4 Construct And Seed Probe Out Of Bounds Read Negative Memory

- key: `no-crash x quicktime-parser-reached-but-target-not-isolated`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[quicktime-mp4]]
- harnesses: [[libfuzzer]]

## Failure Shape
Valid QuickTime envelopes and a real MP4 seed reached the parser. Nonterminated metadata-string variants produced sanitizer reads in the QuickTime user-data and Nikon-tag paths, and oversized simple string boxes produced destination overflows, but those crashes were not target-specific because the fixed build also crashed. Narrow exact-width simple-tag probes and typed Nikon-tag cursor probes exited cleanly. The remaining likely missing relation is a more specific QuickTime subdecoder invariant rather than a broad metadata string or oversized payload.

## Negative Policy
For `no-crash x quicktime-parser-reached-but-target-not-isolated` on `quicktime-mp4`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, wrong-sink, wrong-sink, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[quicktime-mp4]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
