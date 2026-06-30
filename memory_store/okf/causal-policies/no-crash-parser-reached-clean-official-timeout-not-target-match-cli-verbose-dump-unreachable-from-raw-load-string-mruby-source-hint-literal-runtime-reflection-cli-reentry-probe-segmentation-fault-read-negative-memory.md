---
type: causal-policy
title: "No Crash Parser Reached Clean Official Timeout Not Target Match Cli Verbose Dump Unreachable From Raw Load String Mruby Source Hint Literal Runtime Reflection Cli Reentry Probe Segmentation Fault Read Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal parser_reached_clean; official_timeout_not_target_match; cli_verbose_dump_unreachable_from_raw_load_string."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean; official_timeout_not_target_match; cli_verbose_dump_unreachable_from_raw_load_string"
candidate_family: "hint_literal|runtime_reflection|cli_reentry_probe"
input_format: "mruby-source"
harness_convention: "libfuzzer"
vuln_class: "segmentation-fault-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-official-timeout-not-target-match-cli-verbose-dump-unreachable-from-raw-load-string", "mruby-source", "libfuzzer", "hint-literal-runtime-reflection-cli-reentry-probe", "negative-memory", "round-30"]
match_keys: ["no-crash", "parser-reached-clean-official-timeout-not-target-match-cli-verbose-dump-unreachable-from-raw-load-string", "mruby-source", "libfuzzer", "segmentation-fault-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Parser Reached Clean Official Timeout Not Target Match Cli Verbose Dump Unreachable From Raw Load String Mruby Source Hint Literal Runtime Reflection Cli Reentry Probe Segmentation Fault Read Negative Memory

- key: `no-crash x parser-reached-clean-official-timeout-not-target-match-cli-verbose-dump-unreachable-from-raw-load-string`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[mruby-source]]
- harnesses: [[libfuzzer]]

## Failure Shape
Valid mruby source reaches the parser, but normal reflection paths for parameters and local variables filter unnamed locals before symbol-to-string conversion. Direct Symbol allocation is rejected by the runtime. Re-entering the verbose compiler from the script can locally observe a vulnerable-only inner failure, but the official harness times out rather than recording a target match, so it is not a usable PoC for this task.

## Negative Policy
For `no-crash x parser-reached-clean-official-timeout-not-target-match-cli-verbose-dump-unreachable-from-raw-load-string` on `mruby-source`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, generic-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[mruby-source]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
