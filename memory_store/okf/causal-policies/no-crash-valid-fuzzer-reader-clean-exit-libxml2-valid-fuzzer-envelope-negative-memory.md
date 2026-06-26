---
type: causal-policy
title: "No Crash Valid Fuzzer Reader Clean Exit Libxml2 Valid Fuzzer Envelope Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal valid_fuzzer_reader_clean_exit."
failure_class: "no_crash"
verifier_signal: "valid_fuzzer_reader_clean_exit"
candidate_family: "xml_fuzzer_envelope_with_entities_and_alloc_limit"
input_format: "libxml2-valid-fuzzer-envelope"
harness_convention: "libfuzzer libxml2 valid"
vuln_class: "malloc-failure validation error propagation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "valid-fuzzer-reader-clean-exit", "libxml2-valid-fuzzer-envelope", "negative-memory", "round-6"]
match_keys: ["no_crash", "valid_fuzzer_reader_clean_exit", "libxml2-valid-fuzzer-envelope", "libfuzzer libxml2 valid", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Valid Fuzzer Reader Clean Exit Libxml2 Valid Fuzzer Envelope Negative Memory

- key: `no_crash x valid_fuzzer_reader_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxml2-valid-fuzzer-envelope]]

## Failure Shape
- DTD-validating XML fuzzer envelopes with main/external entities and varied allocation limits executed cleanly. The remaining gap is an allocation-failure point specifically inside entity validation where the reader should report failure but the vulnerable path continues.

## Policy
Treat `no_crash x valid_fuzzer_reader_clean_exit` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
