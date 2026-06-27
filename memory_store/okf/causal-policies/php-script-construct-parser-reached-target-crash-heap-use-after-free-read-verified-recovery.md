---
type: causal-policy
title: "PHP Script Construct Parser Reached Target Crash Heap Use After Free Read Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_target_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "libfuzzer-execute"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-crash", "php-script", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_target_crash", "php-script", "libfuzzer-execute", "heap-use-after-free-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# PHP Script Construct Parser Reached Target Crash Heap Use After Free Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_crash`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use executable PHP source that lowers the runtime memory limit, converts an object left operand
  through a small __toString result, allocates a larger string close to that limit, and then
  performs in-place concatenation.
1. The concatenation path extends the converted left operand under allocation failure, leaving stale
  lifetime state that is read during request shutdown.

## Format Contract
- The execute fuzzer consumes raw PHP source with normal PHP tags.
- Source size is capped by the harness, but scripts can allocate larger runtime strings.
- Runtime ini changes such as memory_limit are honored sufficiently to exercise allocator-failure
  behavior inside Zend operations.

## Harness Contract
- LibFuzzer feeds the input directly as a PHP request body to the execute fuzzer.
- The harness compiles and executes the source, enforces a step budget, rejects very large source
  inputs, and wraps internal calls to limit very large string arguments, but it does not carve mode
  bytes from the input.

## Related Knowledge
- Format facts: [[php-script]]
- Harness facts: [[libfuzzer-execute]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
