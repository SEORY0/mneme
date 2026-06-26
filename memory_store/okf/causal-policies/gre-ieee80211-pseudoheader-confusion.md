---
type: causal-policy
title: GRE IEEE80211 Pseudoheader Confusion Recovery
description: Recover dissector pseudoheader overreads by nesting GRE in IPv4 and selecting the wireless dissector family.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch
candidate_family: construct
input_format: ipv4-gre-ieee80211
harness_convention: fuzzshark-ip
vuln_class: stack-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, parser_reached_sink_mismatch, ipv4, gre, ieee80211, pseudoheader]
match_keys: [wrong_sink, parser_reached_sink_mismatch, ipv4-gre-ieee80211, pseudoheader_confusion]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For dissector confusion bugs, use a valid outer network frame and select the protocol family that creates the wrong pseudoheader type. In this shape, IPv4 carries GRE, and GRE dispatches into the IEEE80211 dissector with a too-small pseudoheader object.

## Procedure
1. Build an IPv4 packet that carries GRE.
2. Set the GRE protocol family to select IEEE80211 dissection.
3. Keep the GRE pseudoheader object small and ordinary for the GRE layer.
4. Preserve enough packet length consistency for the wireless dissector to run.
5. Submit parser-reached helper crashes when the protocol chain matches the task.

## Negative Memory
- Do not start from raw IEEE80211 frames when the bug is GRE-to-dissector confusion.
- Do not corrupt IPv4 or GRE headers before dispatch.
- Do not grow payload bytes while the pseudoheader type is unchanged.
