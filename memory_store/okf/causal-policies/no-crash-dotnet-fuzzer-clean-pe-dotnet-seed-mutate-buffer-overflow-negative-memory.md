---
type: causal-policy
title: "No Crash Dotnet Fuzzer Clean Pe Dotnet Seed Mutate Buffer Overflow Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal dotnet-fuzzer-clean."
failure_class: "no_crash"
verifier_signal: "dotnet-fuzzer-clean"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dotnet-fuzzer-clean", "pe-dotnet", "libfuzzer", "seed-mutate", "negative-memory", "round-30"]
match_keys: ["no-crash", "dotnet-fuzzer-clean", "pe-dotnet", "libfuzzer", "buffer-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Dotnet Fuzzer Clean Pe Dotnet Seed Mutate Buffer Overflow Negative Memory

- key: `no-crash x dotnet-fuzzer-clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[pe-dotnet]]
- harnesses: [[libfuzzer]]

## Failure Shape
Valid in-repo managed PE seeds were accepted by the dotnet fuzzer, but distinct mutations did not produce a vulnerable-only crash. Tried preserving a valid PE/CLR envelope while retargeting CustomAttribute-to-MemberRef coded indexes, retargeting an existing attribute blob to a short non-NUL custom-attribute payload near EOF, forcing the module-name selector used by the harness rule, extending the metadata stream-header count, and repeating the custom-attribute blob idea on a different managed-PE carrier. All variants stayed in the same clean-exit basin, suggesting the missing relation is a more precise dotnet metadata stream/blob state or a sanitizer allocation-boundary condition not achieved by these seed mutations.

## Negative Policy
For `no-crash x dotnet-fuzzer-clean` on `pe-dotnet`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[pe-dotnet]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
