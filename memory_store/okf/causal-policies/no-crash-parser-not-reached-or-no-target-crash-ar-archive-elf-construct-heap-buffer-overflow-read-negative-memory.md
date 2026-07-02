---
type: causal-policy
title: "No Crash Parser Not Reached Or No Target Crash Ar Archive Elf Construct Heap Buffer Overflow Read Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal parser_not_reached_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_no_target_crash"
candidate_family: "construct"
input_format: "ar-archive-elf"
harness_convention: "libfuzzer-tempfile-bfd"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-no-target-crash", "ar-archive-elf", "libfuzzer-tempfile-bfd", "construct", "negative-memory", "round-30"]
match_keys: ["no-crash", "parser-not-reached-or-no-target-crash", "ar-archive-elf", "libfuzzer-tempfile-bfd", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Parser Not Reached Or No Target Crash Ar Archive Elf Construct Heap Buffer Overflow Read Negative Memory

- key: `no-crash x parser-not-reached-or-no-target-crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[ar-archive-elf]]
- harnesses: [[libfuzzer-tempfile-bfd]]

## Failure Shape
Constructed raw ELF and GNU ar archive carriers clean-exited across ARM, x86-64, RISC-V, and MIPS attribute-section variants. Attempts covered processor-specific and GNU attribute sections, small attribute sections, string-valued attributes, and int-plus-string compatibility attributes. The archive wrapper was structurally valid, but the scoring harness did not produce a sanitizer-visible crash in the attribute parser for these carriers.

## Negative Policy
For `no-crash x parser-not-reached-or-no-target-crash` on `ar-archive-elf`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[ar-archive-elf]] and [[libfuzzer-tempfile-bfd]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
