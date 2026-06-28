---
type: negative-memory
title: "No Crash Valid Xml Clean Or Wrapper Selection Mismatch Libxml2 Valid Fuzzer Envelope Construct Heap Use After Free Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal valid_xml_clean_or_wrapper_selection_mismatch."
failure_class: "no_crash"
verifier_signal: "valid_xml_clean_or_wrapper_selection_mismatch"
candidate_family: "construct"
input_format: "libxml2-valid-fuzzer-envelope"
harness_convention: "libfuzzer-or-wrapper-selected-libxml2-fuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "valid-xml-clean-or-wrapper-selection-mismatch", "libxml2-valid-fuzzer-envelope", "libfuzzer-or-wrapper-selected-libxml2-fuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "valid_xml_clean_or_wrapper_selection_mismatch", "libxml2-valid-fuzzer-envelope", "libfuzzer-or-wrapper-selected-libxml2-fuzzer", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Valid Xml Clean Or Wrapper Selection Mismatch Libxml2 Valid Fuzzer Envelope Construct Heap Use After Free Negative Memory

- key: `no_crash x valid_xml_clean_or_wrapper_selection_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxml2-valid-fuzzer-envelope]]
- related harness facts: [[libfuzzer-or-wrapper-selected-libxml2-fuzzer]]

## Failure Shape
DTD-validating duplicate-ID documents in the valid-fuzzer envelope did not trigger xmlAddIDSafe use-after-free. Some allocation-limit variants appeared to select a different wrapper path expecting a directory, while the no-limit variant ran a libxml2 fuzzer cleanly. The missing relation is likely a streaming or reader validation lifetime condition combined with duplicate ID replacement and a precise allocation-failure point.

## Policy
Treat `no_crash x valid_xml_clean_or_wrapper_selection_mismatch` on `libxml2-valid-fuzzer-envelope` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `valid_xml_clean_or_wrapper_selection_mismatch` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `valid_xml_clean_or_wrapper_selection_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The libxml2 valid fuzzer envelope starts with parser options and an allocation-failure limit, then escaped URL/content string pairs terminated by a backslash-newline sentinel. The first pair is the main document and later pairs can satisfy external entity or DTD requests.

## Harness Contract
The valid fuzzer reads front-carved integers, forces DTD validation, installs the fuzz entity loader, then parses the main entity through pull, post-validation, push, and reader paths while optionally injecting malloc failures. The useful XML bytes are inside the first entity content, not raw at file start.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 5 attempts.
- Scope: generator repair and basin avoidance only.
