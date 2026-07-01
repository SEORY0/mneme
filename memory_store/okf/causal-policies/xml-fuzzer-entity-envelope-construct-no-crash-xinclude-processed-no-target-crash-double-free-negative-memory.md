---
type: negative-memory
title: "XML Fuzzer Entity Envelope Construct No Crash Xinclude Processed No Target Crash Double Free Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal xinclude_processed_no_target_crash."
failure_class: "no_crash"
verifier_signal: "xinclude_processed_no_target_crash"
candidate_family: "construct"
input_format: "xml-fuzzer-entity-envelope"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "xinclude-processed-no-target-crash", "xml-fuzzer-entity-envelope", "libfuzzer", "construct", "double-free", "negative-memory", "round-36"]
match_keys: ["no_crash", "xinclude_processed_no_target_crash", "xml-fuzzer-entity-envelope", "libfuzzer", "double-free", "no-crash", "xinclude-processed-no-target-crash", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# XML Fuzzer Entity Envelope Construct No Crash Xinclude Processed No Target Crash Double Free Negative Memory

- key: `no_crash x xinclude_processed_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[xml-fuzzer-entity-envelope]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The XML envelope and XInclude option gate were exercised with empty fallback variants, namespace-owned fallback variants, adjacent text/sibling arrangements, document-root include, old and current XInclude namespaces, successful include followed by empty fallback, and parser flag variants. All stayed clean locally. The missing condition is likely a narrower reader-side ownership or traversal state than plain empty fallback processing.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x xinclude_processed_no_target_crash` on `xml-fuzzer-entity-envelope` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `xinclude_processed_no_target_crash` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `xinclude_processed_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 17 attempts.
- Scope: generator repair and basin avoidance only.
