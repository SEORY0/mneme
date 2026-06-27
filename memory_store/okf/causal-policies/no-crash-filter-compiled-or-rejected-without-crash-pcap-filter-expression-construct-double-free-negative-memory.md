---
type: causal-policy
title: "No Crash Filter Compiled Or Rejected Without Crash Pcap Filter Expression Construct Double Free Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal filter_compiled_or_rejected_without_crash."
failure_class: "no_crash"
verifier_signal: "filter_compiled_or_rejected_without_crash"
candidate_family: "construct"
input_format: "pcap-filter-expression"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "filter-compiled-or-rejected-without-crash", "pcap-filter-expression", "negative-memory", "round-14"]
match_keys: ["no_crash", "filter_compiled_or_rejected_without_crash", "pcap-filter-expression", "libfuzzer", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Filter Compiled Or Rejected Without Crash Pcap Filter Expression Construct Double Free Negative Memory

- key: `no_crash x filter_compiled_or_rejected_without_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pcap-filter-expression]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Arithmetic divide/modulo expressions, packet-load arithmetic expressions, protochain combinations, and large repeated boolean expressions all executed without triggering optimizer cleanup failure. The likely missing condition is an optimizer allocation or long-jump error after several cleanup-owned buffers have been allocated and partially released.

## Policy
Treat `no_crash x filter_compiled_or_rejected_without_crash` on `pcap-filter-expression` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
