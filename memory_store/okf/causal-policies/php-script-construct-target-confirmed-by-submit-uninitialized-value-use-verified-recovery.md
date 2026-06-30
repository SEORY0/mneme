---
type: causal-policy
title: "PHP Script Construct Target Confirmed By Submit Uninitialized Value Use Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "target_confirmed_by_submit"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value-use"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-confirmed-by-submit", "php-script", "libfuzzer", "construct", "uninitialized-value-use", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "target_confirmed_by_submit", "php-script", "libfuzzer", "uninitialized-value-use", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# PHP Script Construct Target Confirmed By Submit Uninitialized Value Use Verified Recovery

## Policy
For `generic_crash x target_confirmed_by_submit`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use raw PHP source that enables visible error handling, installs a user error handler that converts an undefined-variable warning into an exception, then evaluates a nullsafe property access on an undefined variable inside an exception-capable expression.
2. This reaches the nullsafe JMP_NULL exceptional path before the result temporary is initialized; unwinding/destruction then observes the uninitialized zval.
3. Keeping the script minimal avoids unrelated parser or runtime crashes.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is PHP source text, not a serialized or bytecode container.
- The nullsafe object operator compiles through a JMP_NULL path.
- Undefined variable access normally reports a warning and continues, but a script-level error handler can turn that warning into an exception, which is the important control-flow edge for this bug.
- Harness [[libfuzzer]]:
  - The PHP execute fuzzer feeds the raw input bytes as a PHP script buffer and executes them directly.
  - There is no FuzzedDataProvider split or length-prefixed envelope.
  - The harness suppresses normal error reporting through configuration, so the PoC must establish its own error-reporting and exception-conversion behavior in the script.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[php-script]] and [[libfuzzer]].
