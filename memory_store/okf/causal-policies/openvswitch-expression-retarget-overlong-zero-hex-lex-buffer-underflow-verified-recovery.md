---
type: causal-policy
title: "Openvswitch Expression Retarget Overlong Zero Hex Lex Buffer Underflow Verified Recovery"
description: "Round 20 retarget recovery for no_crash with verifier signal parser_reached_without_sanitizer_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_without_sanitizer_crash"
candidate_family: "retarget_construct"
input_format: "openvswitch-expression"
harness_convention: "afl-raw-stdin"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "parser-reached-without-sanitizer-crash", "openvswitch-expression", "afl-raw-stdin", "verified-recovery", "retarget", "round-20"]
match_keys: ["no-crash", "parser-reached-without-sanitizer-crash", "openvswitch-expression", "afl-raw-stdin", "buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# Openvswitch Expression Retarget Overlong Zero Hex Lex Buffer Underflow Verified Recovery

- key: `no_crash x parser_reached_without_sanitizer_crash`
- outcome: verified retarget recovery
- success_count: 1
- failure_count: 0
- formats: [[openvswitch-expression]]
- harnesses: [[afl-raw-stdin]]

## Failure Shape
Short overlong hexadecimal constants can reach the lexer but exit cleanly because the out-of-bounds access does not land in poisoned stack memory. The verified recovery is to keep the bare hexadecimal-token gate and extend the all-zero high-nibble run far enough past the fixed integer storage that the zero-valued write/read crosses the stack redzone while still avoiding the nonzero overflow guard.

## Policy
For `no_crash x parser_reached_without_sanitizer_crash` on `openvswitch-expression`, do not switch to unrelated field comparisons, masks, or expression syntax first. Preserve a single NUL-terminated expression token accepted by the raw stdin harness, then scale the all-zero hexadecimal token beyond the token value storage until the lexer reports the stack-buffer-underflow/overflow at the hex parser.

## Procedure
1. Use the raw Open vSwitch expression harness contract: no newline, NUL-terminated input, and a token that starts with the hexadecimal prefix.
2. Keep every high-order digit zero so the nonzero overflow diagnostic is not triggered before the vulnerable write/read.
3. Increase the zero run past the fixed integer storage rather than adding semantic expression context.
4. Submit only after local verify reaches the lexer hex parser with a vulnerable-only sanitizer signal; clean syntax errors remain non-success.

## Verifier Contract
Local verify may classify the crash as `wrong_sink` even though the stack trace reaches the intended lexer hex parser. The official vulnerable-versus-fixed target match is the confirmation gate.

## Negative Memory
- Do not stop at short all-zero hex tokens that merely parse or produce syntax errors.
- Do not replace the carrier with decimal, mask, or comparison syntax before proving the hex token gate.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 official retarget solve from round 20 consolidation.
- Scope: generator repair only.
