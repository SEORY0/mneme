---
type: causal-policy
title: "No Crash Parser Clean Or Rejected Openexr File Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_clean_or_rejected."
failure_class: "no_crash"
verifier_signal: "parser_clean_or_rejected"
candidate_family: "construct"
input_format: "openexr-file"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-clean-or-rejected", "openexr-file", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_clean_or_rejected", "openexr-file", "libfuzzer", "out-of-bounds-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Clean Or Rejected Openexr File Negative Memory

- key: `no_crash x parser_clean_or_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openexr-file]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A minimal OpenEXR header with a malformed channel-list attribute executed cleanly. The likely
  missing gate is a deeper exrcorecheck-valid image structure that reaches full channel-name
  comparison against a byte-count-limited buffer rather than only header parsing.

## Policy
Treat `no_crash x parser_clean_or_rejected` on `openexr-file` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- OpenEXR files start with magic/version words followed by typed attributes such as channels,
  compression, data/display windows, line order, pixel aspect, and screen-window fields, then offset
  tables and chunk data. Channel lists contain NUL-terminated names and fixed channel metadata
  records.

## Harness Contract
- The selected libFuzzer target was the OpenEXR core-check fuzzer. It consumes a raw EXR-like file and
  runs structural file checks; there is no pcap, archive wrapper, or front selector byte.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_clean_or_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
