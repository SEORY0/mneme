---
type: causal-policy
title: "MRUBY Script Construct Parser Reached Target Fmt Setup Stack Overflow Stack Buffer Overflow Write Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_target_fmt_setup_stack_overflow."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_fmt_setup_stack_overflow"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer-raw-mruby-source"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-fmt-setup-stack-overflow", "mruby-script", "libfuzzer-raw-mruby-source", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_target_fmt_setup_stack_overflow", "mruby-script", "libfuzzer-raw-mruby-source", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# MRUBY Script Construct Parser Reached Target Fmt Setup Stack Overflow Stack Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_fmt_setup_stack_overflow`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mruby-script]]
- harnesses: [[libfuzzer-raw-mruby-source]]

## Failure Shape
Use a syntactically valid Ruby script that calls the standard sprintf path with a floating-point conversion. Keep the script valid, but make the format descriptor itself overlong by combining all legal numeric-format components at maximum-width decimal lengths, so the float branch rebuilds a C printf format string that exceeds its fixed stack buffer before the later size checks can reject the request.

## Policy
For `generic_crash x parser_reached_target_fmt_setup_stack_overflow` on `mruby-script`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `mruby-script` carrier and `libfuzzer-raw-mruby-source` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `mruby-script` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
mruby script input is parsed by mrb_load_string. Kernel#sprintf and String formatting accept flags, optional field width, optional precision, and a conversion specifier. Width and precision are parsed as decimal integers; the floating-point conversion branch reconstructs a native printf-style format string in a fixed stack buffer from those parsed components.

## Harness Contract
The libFuzzer harness passes the raw input bytes as an mruby source program. It allocates a copy, appends a NUL terminator, opens an mruby state, calls mrb_load_string, then closes the state. There is no leading selector byte, file wrapper, or FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
