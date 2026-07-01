---
type: causal-policy
title: "Libxml2 XML Fuzzer Entity Envelope Construct Generic Crash Reader Xinclude Text Cache Copy After Reader Frees Text Node Heap Use After Free Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal reader_xinclude_text_cache_copy_after_reader_frees_text_node."
failure_class: "generic_crash"
verifier_signal: "reader_xinclude_text_cache_copy_after_reader_frees_text_node"
candidate_family: "construct"
input_format: "libxml2-xml-fuzzer-entity-envelope"
harness_convention: "honggfuzz-compatible-libxml2-xml-fuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "reader-xinclude-text-cache-copy-after-reader-frees-text-node", "libxml2-xml-fuzzer-entity-envelope", "honggfuzz-compatible-libxml2-xml-fuzzer", "construct", "heap-use-after-free-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "reader_xinclude_text_cache_copy_after_reader_frees_text_node", "libxml2-xml-fuzzer-entity-envelope", "honggfuzz-compatible-libxml2-xml-fuzzer", "heap-use-after-free-read", "generic-crash", "reader-xinclude-text-cache-copy-after-reader-frees-text-node", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Libxml2 XML Fuzzer Entity Envelope Construct Generic Crash Reader Xinclude Text Cache Copy After Reader Frees Text Node Heap Use After Free Read Verified Recovery

- key: `generic_crash x reader_xinclude_text_cache_copy_after_reader_frees_text_node`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[libxml2-xml-fuzzer-entity-envelope]]
- related harness facts: [[honggfuzz-compatible-libxml2-xml-fuzzer]]

## Failure Shape
Build the libxml2 XML fuzzer envelope with parser options that enable XInclude in the reader path and keep reader-owned nodes eligible for cleanup. Make the first fuzz entity the main XML document and provide a second fuzz entity for the included text resource. In the main document, use XInclude text inclusion twice with the same href, separated by enough normal XML structure for the reader to advance past and free the first included text node. The second include reuses the cached text node and the vulnerable build copies from freed memory; the fixed build avoids the stale-node copy.

## Policy
When `generic_crash x reader_xinclude_text_cache_copy_after_reader_frees_text_node` appears for `libxml2-xml-fuzzer-entity-envelope` under `honggfuzz-compatible-libxml2-xml-fuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[libxml2-xml-fuzzer-entity-envelope]]` format contract and `[[honggfuzz-compatible-libxml2-xml-fuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `libxml2-xml-fuzzer-entity-envelope` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 5 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
