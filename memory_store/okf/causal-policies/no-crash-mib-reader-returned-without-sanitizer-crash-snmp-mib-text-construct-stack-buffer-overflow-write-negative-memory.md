---
type: negative-memory
title: "No Crash Mib Reader Returned Without Sanitizer Crash Snmp Mib Text Construct Stack Buffer Overflow Write Negative Memory"
description: "Round 27 diagnosed persistent failure for no_crash with verifier signal mib_reader_returned_without_sanitizer_crash."
failure_class: "no_crash"
verifier_signal: "mib_reader_returned_without_sanitizer_crash"
candidate_family: "construct"
input_format: "snmp-mib-text"
harness_convention: "honggfuzz-libfuzzer-compat"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: high
tags: ["no-crash", "mib-reader-returned-without-sanitizer-crash", "snmp-mib-text", "honggfuzz-libfuzzer-compat", "construct", "stack-buffer-overflow-write", "negative-memory", "round-27"]
match_keys: ["no_crash", "mib_reader_returned_without_sanitizer_crash", "snmp-mib-text", "honggfuzz-libfuzzer-compat", "stack-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# No Crash Mib Reader Returned Without Sanitizer Crash Snmp Mib Text Construct Stack Buffer Overflow Write Negative Memory

- key: `no_crash x mib_reader_returned_without_sanitizer_crash`
- outcome: diagnosed persistent failure; avoid repeating this basin without a new gate relation.
- success_count: 0

## Failure Shape
- The MIB reader accepted raw text inputs but did not produce a sanitizer crash for five distinct hypotheses: malformed SIZE range token-length confusion with label data, the same range path with quoted data, oversized valid DESCRIPTION text, recursive comment-token stress, and high-valued syntax tokens inside OBJECT-TYPE parsing.
- The likely missing piece is a more precise parser macro path that reaches the stack overwrite without being normalized or truncated by get_token.

## Format / Harness Contract
- A MIB file starts with a module label and DEFINITIONS ::= BEGIN, then records such as OBJECT IDENTIFIER and OBJECT-TYPE.
- OBJECT-TYPE parsing expects SYNTAX, ACCESS or MAX-ACCESS, STATUS, optional DESCRIPTION or DEFVAL clauses, and an object assignment in braces.
- Tokens are bounded labels, quoted strings are separately bounded, and SIZE ranges use nested parentheses inside SYNTAX.
- Harness [[honggfuzz-libfuzzer-compat]]:
  - The harness writes the raw input bytes to a temporary MIB file and calls read_mib on that path.
  - read_mib reads the first label as the module name, registers the module, reopens the same file, and parses it.
  - There is no mode byte, prefix, checksum, or FuzzedDataProvider splitting.

## Policy
Treat `no_crash x mib_reader_returned_without_sanitizer_crash` as a negative-memory key for `snmp-mib-text` under `honggfuzz-libfuzzer-compat`. A future candidate needs a different causal relation than the recorded `construct` attempt family, or explicit evidence that the missing parser/sink gate has changed.

## Procedure
1. First re-establish the exact parser or harness gate named by the verifier signal before changing payload scale.
2. If the prior basin was clean execution, search for the narrow branch that reaches the sink rather than sweeping larger mutations.
3. If the prior basin was fixed-image or both-image failure, narrow the mutation until the fixed build rejects or survives before submitting.

## Negative Memory
- Do not repeat the `construct` family against this failure key without a new gate hypothesis.
- Do not keep candidates that are clean, parser-not-reached, fixed-image crashes, or off-target wrapper failures.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one diagnosed round-27 persistent failure.
- Pair with [[snmp-mib-text]] and [[honggfuzz-libfuzzer-compat]].
