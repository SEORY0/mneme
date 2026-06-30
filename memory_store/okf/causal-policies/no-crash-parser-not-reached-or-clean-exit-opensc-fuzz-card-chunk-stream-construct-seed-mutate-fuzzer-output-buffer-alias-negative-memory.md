---
type: causal-policy
title: "No Crash Parser Not Reached Or Clean Exit Opensc Fuzz Card Chunk Stream Construct Seed Mutate Fuzzer Output Buffer Alias Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal parser_not_reached_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_clean_exit"
candidate_family: "construct+seed_mutate"
input_format: "opensc-fuzz-card-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "fuzzer-output-buffer-alias"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-clean-exit", "opensc-fuzz-card-chunk-stream", "libfuzzer", "construct-seed-mutate", "negative-memory", "round-30"]
match_keys: ["no-crash", "parser-not-reached-or-clean-exit", "opensc-fuzz-card-chunk-stream", "libfuzzer", "fuzzer-output-buffer-alias", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Parser Not Reached Or Clean Exit Opensc Fuzz Card Chunk Stream Construct Seed Mutate Fuzzer Output Buffer Alias Negative Memory

- key: `no-crash x parser-not-reached-or-clean-exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[opensc-fuzz-card-chunk-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
The extracted fuzz_card harness already allocates separate buffers for wrap, unwrap, and challenge outputs, matching the hardening described by the bug card. Corpus-preserving mutations, challenge-length expansion, and MyEID wrap/challenge transcripts all exited cleanly. The likely missing condition is either a build/source mismatch with the vulnerable image or an aliasing pattern that corrupts later fuzz chunks without crossing an ASAN-detectable boundary.

## Negative Policy
For `no-crash x parser-not-reached-or-clean-exit` on `opensc-fuzz-card-chunk-stream`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[opensc-fuzz-card-chunk-stream]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
