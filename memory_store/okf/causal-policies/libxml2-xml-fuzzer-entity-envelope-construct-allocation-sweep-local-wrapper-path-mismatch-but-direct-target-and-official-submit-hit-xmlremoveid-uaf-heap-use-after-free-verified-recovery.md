---
type: causal-policy
title: "Libxml2 XML Fuzzer Entity Envelope Construct Allocation Sweep Local Wrapper Path Mismatch But Direct Target And Official Submit Hit Xmlremoveid Uaf Heap Use After Free Verified Recovery"
description: "Round 29 verified recovery for no_crash with verifier signal local_wrapper_path_mismatch_but_direct_target_and_official_submit_hit_xmlRemoveID_uaf."
failure_class: "no_crash"
verifier_signal: "local_wrapper_path_mismatch_but_direct_target_and_official_submit_hit_xmlRemoveID_uaf"
candidate_family: "construct_allocation_sweep"
input_format: "libxml2-xml-fuzzer-entity-envelope"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-wrapper-path-mismatch-but-direct-target-and-official-submit-hit-xmlremoveid-uaf", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "construct-allocation-sweep", "heap-use-after-free", "verified-recovery", "round-29"]
match_keys: ["no_crash", "local_wrapper_path_mismatch_but_direct_target_and_official_submit_hit_xmlRemoveID_uaf", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "heap-use-after-free", "no-crash", "local-wrapper-path-mismatch-but-direct-target-and-official-submit-hit-xmlremoveid-uaf", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "heap-use-after-free", "verified_recovery", "construct_allocation_sweep", "construct-allocation-sweep"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Libxml2 XML Fuzzer Entity Envelope Construct Allocation Sweep Local Wrapper Path Mismatch But Direct Target And Official Submit Hit Xmlremoveid Uaf Heap Use After Free Verified Recovery

- key: `no_crash x local_wrapper_path_mismatch_but_direct_target_and_official_submit_hit_xmlRemoveID_uaf`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[libxml2-xml-fuzzer-entity-envelope]]
- related harness facts: [[libfuzzer]]

## Policy
For `no_crash x local_wrapper_path_mismatch_but_direct_target_and_official_submit_hit_xmlRemoveID_uaf` on `libxml2-xml-fuzzer-entity-envelope`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the libxml2 XML fuzzer entity envelope with entity expansion and DTD ID detection enabled. The main document defines an element with a DTD-declared ID attribute and an internal entity whose replacement element carries both xml:id and that declared ID attribute with the same value. Reference the entity from the document so reader-mode entity parsing creates two attributes sharing one ID object, then use the harness allocation-failure field to make entity-copy cleanup free the first ID reference and immediately remove the second attribute, producing the stale ID read in xmlRemoveID.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[libxml2-xml-fuzzer-entity-envelope]]: The XML fuzzer input is not plain XML. It starts with big-endian parser options and a big-endian allocation-failure control, followed by escaped URL/content string pairs. The first pair is the main XML resource and later pairs can provide external resources. String fields end with the fuzzer's backslash-newline sentinel, and entity contents are ordinary XML text inside that envelope.
- Harness [[libfuzzer]]: The active wrapper runs the libxml2 xml fuzzer. That target masks out DTD validation and XInclude, applies the allocation limit around pull, push, and XML reader parsing, installs the fuzzer entity loader, and traverses reader nodes plus attribute values. The local runner verify path can report a /tmp/poc wrapper error even when direct execution of the same target and official submit exercise the real crash.

## Negative Memory
- Do not corrupt the outer `libxml2-xml-fuzzer-entity-envelope` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[libxml2-xml-fuzzer-entity-envelope]] and [[libfuzzer]].
