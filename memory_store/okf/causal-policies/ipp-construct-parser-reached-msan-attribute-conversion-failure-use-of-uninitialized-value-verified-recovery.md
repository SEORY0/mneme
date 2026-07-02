---
type: causal-policy
title: "Ipp Construct Parser Reached Msan Attribute Conversion Failure Use Of Uninitialized Value Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_msan_attribute_conversion_failure."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_msan_attribute_conversion_failure"
candidate_family: "construct"
input_format: "ipp"
harness_convention: "libfuzzer-file-fuzzipp"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-msan-attribute-conversion-failure", "ipp", "libfuzzer-file-fuzzipp", "construct", "use-of-uninitialized-value", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_msan_attribute_conversion_failure", "ipp", "libfuzzer-file-fuzzipp", "use-of-uninitialized-value", "verified_recovery", "construct", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Ipp Construct Parser Reached Msan Attribute Conversion Failure Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_msan_attribute_conversion_failure`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal raw IPP request with a valid header, an operation attribute group, and one repeated named attribute. The first value should be a normal text-family string value. The second value should reuse the current attribute by using an empty name but change the value tag to a language-qualified name form, with a well-formed composite language/text payload. This asks the reader to perform a text-to-name-with-language conversion that the conversion helper rejects; the vulnerable reader ignores that failure and continues parsing the new composite value, leaving inconsistent string state that later reaches the sanitizer during string interning. Avoid broader malformed IPP fields so the fixed build exits through the clean parse-error path instead of crashing.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[ipp]]: An IPP message starts with a fixed-size request header, followed by group tags and value-tagged attributes, ending with an end tag. Attribute records encode a value tag, a big-endian name length, the attribute name, a big-endian value length, and the typed value bytes. A zero name length on a subsequent value means the value belongs to the current attribute. Language-qualified text/name values are composite values containing a language length and language string followed by a text length and text string.
- Harness [[libfuzzer-file-fuzzipp]]: The harness writes the fuzz input bytes directly to a temporary file and passes that file to the libcups IPP fuzzer. There is no leading selector byte, archive wrapper, or FuzzedDataProvider carving. The fuzzer reads the file with ippReadIO, then resets the parsed request state and writes it back with ippWriteIO, so parser-accepted inconsistent attributes can crash during either read-side string handling or later serialization.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ipp]] and [[libfuzzer-file-fuzzipp]].
