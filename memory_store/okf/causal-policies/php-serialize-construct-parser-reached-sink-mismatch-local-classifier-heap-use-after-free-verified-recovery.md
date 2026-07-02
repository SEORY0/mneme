---
type: causal-policy
title: "Php Serialize Construct Parser Reached Sink Mismatch Local Classifier Heap Use After Free Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_local_classifier."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_local_classifier"
candidate_family: "construct"
input_format: "php-serialize"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-local-classifier", "php-serialize", "libfuzzer", "construct", "heap-use-after-free", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_local_classifier", "php-serialize", "libfuzzer", "heap-use-after-free", "verified_recovery", "construct", "use-after-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Php Serialize Construct Parser Reached Sink Mismatch Local Classifier Heap Use After Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_local_classifier`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a single PHP serialized value for the unserialize fuzzer. Use a destructor-bearing SPL iterator object kept alive by a reference cycle so forced GC treats it as destructor garbage. Give it an SPL object-storage container whose custom serialized storage has a recursive object-storage value early in the outer storage, followed by additional live objects. This satisfies normal unserialize parsing, reaches GC nested-data removal, then the recursive get_gc call reuses the shared temporary GC buffer while the outer removal loop still has entries to walk, producing a vulnerable-only heap use-after-free. Keep the storage sizes small and structurally valid so the fixed build exits cleanly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[php-serialize]]: PHP serialize wire values include objects, arrays, object references, and reference wrappers. SPL containers that implement Serializable use custom C records with a storage section and a members section; SplObjectStorage records contain an object entry and optional associated info value, followed by serialized object properties. Object-reference opcodes and regular reference opcodes are distinct: object references target objects, while reference wrappers can target arrays or other zvals. Internal classes that implement Serializable should use the custom-object form for their internal storage rather than plain object properties.
- Harness [[libfuzzer]]: The libFuzzer target copies the raw input bytes, NUL-terminates them, calls php_var_unserialize on the entire buffer, destroys the top-level result, then forces PHP GC twice before request shutdown. There is no leading mode byte, no filename, and no FuzzedDataProvider split; the payload is exactly one serialized PHP value.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[php-serialize]] and [[libfuzzer]].
