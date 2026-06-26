---
type: causal-policy
title: XInclude Processed No-Crash Negative Memory
description: Negative memory for XML XInclude candidates that process includes but miss the text-node lifetime bug.
failure_class: no_crash
verifier_signal: xinclude_processed_no_crash
candidate_family: construct
input_format: xml-xinclude-fuzzer-envelope
harness_convention: libfuzzer
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, xinclude_processed_no_crash, xml, xinclude, negative_memory]
match_keys: [no_crash, xinclude_processed_no_crash, xml-xinclude, text_node_lifetime]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
XInclude processing without a crash is negative memory for simple include and fallback patterns. The next candidate must create adjacent or copied text-node relationships across include or fallback cleanup, not merely enable XInclude.

## Procedure
1. Preserve the fuzzer envelope that selects main URL and resource mapping.
2. Keep XInclude and fallback syntax valid.
3. Arrange include and fallback trees so text nodes are copied, coalesced, or deleted across cleanup.
4. Mutate node adjacency and fallback deletion order before changing raw XML size.
5. Verify that XInclude processing still occurs after every mutation.

## Negative Memory
- Do not repeat empty fallback patterns that already processed cleanly.
- Do not remove the mapped resource envelope.
- Do not treat ordinary include success as sink reachability.
