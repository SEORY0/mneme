---
type: causal-policy
title: "Javascript Source Minimal Raw Target Sink Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal target_sink_crash."
failure_class: "generic_crash"
verifier_signal: "target_sink_crash"
candidate_family: "source_minimal_raw"
input_format: "javascript"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-crash", "javascript", "libfuzzer", "source-minimal-raw", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "target_sink_crash", "javascript", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "other", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Javascript Source Minimal Raw Target Sink Crash Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x target_sink_crash`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed the raw JavaScript evaluator a tiny source unit containing a normal string literal whose escape sequence enters braced Unicode-codepoint parsing. Keep the source otherwise syntactically simple, then put a non-hex character inside the braced escape before its terminator. The first lexer diagnostic reaches the runtime's simple error limit, forces EOF, and the vulnerable braced-codepoint loop continues from the forced end pointer.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[javascript]]: The input is JavaScript source text, not a container format. The lexer handles string literal backslash escapes directly; a braced Unicode codepoint escape consumes hexadecimal codepoint characters until a closing brace or EOF. Invalid non-hex characters inside the braced form report a lexer error while scanning the same string token. There are no magic, length, or checksum gates.
- Harness [[libfuzzer]]: The libFuzzer harness passes the PoC file's raw bytes as the JavaScript source buffer, rejects only empty input and Hermes bytecode-looking input, appends a NUL terminator internally, creates a Hermes runtime, and evaluates the source while swallowing JavaScript exceptions.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[javascript]] and [[libfuzzer]].
