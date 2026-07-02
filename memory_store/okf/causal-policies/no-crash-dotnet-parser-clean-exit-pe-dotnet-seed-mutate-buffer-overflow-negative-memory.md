---
type: causal-policy
title: "No Crash Dotnet Parser Clean Exit Pe Dotnet Seed Mutate Buffer Overflow Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal dotnet_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "dotnet_parser_clean_exit"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer-yara-dotnet-scan-mem"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dotnet-parser-clean-exit", "pe-dotnet", "libfuzzer-yara-dotnet-scan-mem", "seed-mutate", "negative-memory", "round-30"]
match_keys: ["no-crash", "dotnet-parser-clean-exit", "pe-dotnet", "libfuzzer-yara-dotnet-scan-mem", "buffer-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Dotnet Parser Clean Exit Pe Dotnet Seed Mutate Buffer Overflow Negative Memory

- key: `no-crash x dotnet-parser-clean-exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[pe-dotnet]]
- harnesses: [[libfuzzer-yara-dotnet-scan-mem]]

## Failure Shape
Valid managed PE corpus inputs reached the YARA dotnet scanner, but mutations of the CustomAttribute Type relation, MemberRef row-count widening, GuidAttribute name selection, oversized custom-attribute string length, long blob envelope, and metadata stream-header walking all stayed in the clean-exit basin. The missing relation appears to be a precise custom-attribute/blob inconsistency that is accepted deeply enough by the vulnerable copy/read path while still producing a sanitizer-visible overrun.

## Negative Policy
For `no-crash x dotnet-parser-clean-exit` on `pe-dotnet`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[pe-dotnet]] and [[libfuzzer-yara-dotnet-scan-mem]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
