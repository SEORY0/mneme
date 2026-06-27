---
type: causal-policy
title: "Fluent Bit Http Fuzzer Buffer Construct Parser Reached Double Free Cleanup Heap Double Free Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_double_free_cleanup."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_double_free_cleanup"
candidate_family: "construct"
input_format: "fluent-bit-http-fuzzer-buffer"
harness_convention: "libfuzzer"
vuln_class: "heap-double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-double-free-cleanup", "fluent-bit-http-fuzzer-buffer", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_double_free_cleanup", "fluent-bit-http-fuzzer-buffer", "libfuzzer", "heap-double-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Fluent Bit Http Fuzzer Buffer Construct Parser Reached Double Free Cleanup Heap Double Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_double_free_cleanup`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Satisfy the fuzzer size gate and choose the branch that supplies a proxy string.
1. Keep the URI and method acceptable, but make the proxy syntactically unsupported so proxy parsing
  fails after the header buffer has been attached to the client object.
1. The vulnerable cleanup frees the same linked buffer twice; the fixed build avoids the second
  free.

## Format Contract
- The fuzzer input is a carved HTTP-client configuration buffer, not an HTTP request.
- A selector controls whether a fixed-width proxy field is consumed, followed by a fixed-width URI
  field and a one-byte method value.
- The remaining bytes are filler for size and allocator state.

## Harness Contract
- The libFuzzer harness requires a minimum input size, consumes fields front-to-back, uses an
  odd/even selector for proxy mode, then constructs a Fluent Bit HTTP client from the carved proxy,
  URI, and method fields.

## Related Knowledge
- Format facts: [[fluent-bit-http-fuzzer-buffer]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
