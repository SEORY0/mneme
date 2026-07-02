---
type: causal-policy
title: "Libxml2 Lint Entity Envelope Construct Parser Reached Zlib Output Compression Uninitialized Value Memorysanitizer Use Of Uninitialized Value Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_zlib_output_compression_uninitialized_value."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_zlib_output_compression_uninitialized_value"
candidate_family: "construct"
input_format: "libxml2-lint-entity-envelope"
harness_convention: "libfuzzer"
vuln_class: "memorysanitizer-use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-zlib-output-compression-uninitialized-value", "libxml2-lint-entity-envelope", "libfuzzer", "construct", "memorysanitizer-use-of-uninitialized-value", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_zlib_output_compression_uninitialized_value", "libxml2-lint-entity-envelope", "libfuzzer", "memorysanitizer-use-of-uninitialized-value", "verified_recovery", "construct", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Libxml2 Lint Entity Envelope Construct Parser Reached Zlib Output Compression Uninitialized Value Memorysanitizer Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_zlib_output_compression_uninitialized_value`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the lint fuzzer envelope rather than raw XML. Set the front option word so xmllint enables output compression, leave unrelated controls empty, and provide an in-memory main XML entity that parses cleanly. The parsed document is then saved through libxml2's gzip output callback, which reaches the uninstrumented zlib path and produces the MemorySanitizer report while the fixed build exits normally.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[libxml2-lint-entity-envelope]]: The lint fuzzer input begins with option-control integers, then bounded numeric controls, then escaped strings for optional arguments, followed by URL/content string pairs for in-memory entities. Strings use a backslash-newline terminator with doubled backslashes for literal backslashes. The first URL/content pair is the main document, and the main URL must not look like a command-line option.
- Harness [[libfuzzer]]: The active target is the libxml2 xmllint libFuzzer harness. It reads integers from the front in big-endian order, consumes option bits least-significant-bit first within each word, then selects a parser mode from the remaining bits. The XML document is loaded through the fuzzer's in-memory entity loader; enabling the compression option routes output through gzip rather than requiring a compressed input file.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[libxml2-lint-entity-envelope]] and [[libfuzzer]].
