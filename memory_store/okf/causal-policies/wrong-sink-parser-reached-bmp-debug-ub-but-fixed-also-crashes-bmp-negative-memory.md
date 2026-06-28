---
type: causal-policy
title: "Wrong Sink Parser Reached Bmp Debug Ub But Fixed Also Crashes Bmp Negative Memory"
description: "Round 24 negative memory for wrong_sink with verifier signal parser_reached_bmp_debug_ub_but_fixed_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_bmp_debug_ub_but_fixed_also_crashes"
candidate_family: "seed_mutate"
input_format: "bmp"
harness_convention: "libfuzzer raw bytes"
vuln_class: "serenity-error-handling-or-wrong-bmp-debug-crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-bmp-debug-ub-but-fixed-also-crashes", "bmp", "libfuzzer-raw-bytes", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["wrong-sink", "parser-reached-bmp-debug-ub-but-fixed-also-crashes", "bmp", "libfuzzer-raw-bytes", "serenity-error-handling-or-wrong-bmp-debug-crash"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# Wrong Sink Parser Reached Bmp Debug Ub But Fixed Also Crashes Bmp Negative Memory

- key: `wrong_sink x parser_reached_bmp_debug_ub_but_fixed_also_crashes`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[bmp]]
- harnesses: [[libfuzzer-raw-bytes]]

## Dead-End Shape
The generated runtime target was FuzzBMPLoader even though the card described ErrnoCode/ErrorOr. Bundled malformed BMP samples reached Serenity debug-format UB in the vulnerable image, but the submitted sample also crashed the fixed image, so it was not the target bug.

## Policy
For `wrong_sink x parser_reached_bmp_debug_ub_but_fixed_also_crashes` on `bmp`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `wrong_sink x parser_reached_bmp_debug_ub_but_fixed_also_crashes` appears for `bmp`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
