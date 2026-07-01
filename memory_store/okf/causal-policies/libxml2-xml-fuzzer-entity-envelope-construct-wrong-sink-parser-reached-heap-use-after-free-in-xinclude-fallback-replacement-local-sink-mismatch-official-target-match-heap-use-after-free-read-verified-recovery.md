---
type: "causal-policy"
title: "Libxml2 XML Fuzzer Entity Envelope Construct Wrong Sink Parser Reached Heap Use After Free In Xinclude Fallback Replacement Local Sink Mismatch Official Target Match Heap Use After Free Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_heap_use_after_free_in_xinclude_fallback_replacement_local_sink_mismatch_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_heap_use_after_free_in_xinclude_fallback_replacement_local_sink_mismatch_official_target_match"
candidate_family: "construct"
input_format: "libxml2-xml-fuzzer-entity-envelope"
harness_convention: "honggfuzz-compatible-libxml2-xml-fuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-heap-use-after-free-in-xinclude-fallback-replacement-local-sink-mismatch-official-target-match", "libxml2-xml-fuzzer-entity-envelope", "honggfuzz-compatible-libxml2-xml-fuzzer", "construct", "heap-use-after-free-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_heap_use_after_free_in_xinclude_fallback_replacement_local_sink_mismatch_official_target_match", "libxml2-xml-fuzzer-entity-envelope", "honggfuzz-compatible-libxml2-xml-fuzzer", "heap-use-after-free-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Libxml2 XML Fuzzer Entity Envelope Construct Wrong Sink Parser Reached Heap Use After Free In Xinclude Fallback Replacement Local Sink Mismatch Official Target Match Heap Use After Free Read Verified Recovery

- key: `wrong_sink x parser_reached_heap_use_after_free_in_xinclude_fallback_replacement_local_sink_mismatch_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[libxml2-xml-fuzzer-entity-envelope]]
- related harness facts: [[honggfuzz-compatible-libxml2-xml-fuzzer]]

## Failure Shape
Use the XML fuzzer entity envelope, not raw XML. Enable XInclude processing together with the option that removes generated XInclude marker nodes. Make the main document a valid XML document whose outer include falls back; inside that fallback, place an inner include with an empty fallback between ordinary text siblings. The failed inner include is reprocessed while the outer fallback is being materialized, adjacent text coalesces through the tree helper, and a node reference retained by the XInclude replacement logic becomes stale before it is read.

## Policy
When `wrong_sink x parser_reached_heap_use_after_free_in_xinclude_fallback_replacement_local_sink_mismatch_official_target_match` appears for `[[libxml2-xml-fuzzer-entity-envelope]]` under `[[honggfuzz-compatible-libxml2-xml-fuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[libxml2-xml-fuzzer-entity-envelope]]` format contract and `[[honggfuzz-compatible-libxml2-xml-fuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[libxml2-xml-fuzzer-entity-envelope]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 18 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
