---
type: causal-policy
title: "No Crash Clean Exit Liblouis Generic Table Plus Escaped Text Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "liblouis-generic-table-plus-escaped-text"
harness_convention: "libfuzzer"
vuln_class: "negative-size-memcpy"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "liblouis-generic-table-plus-escaped-text", "negative-memory", "round-7"]
match_keys: ["no_crash", "clean_exit", "liblouis-generic-table-plus-escaped-text", "libfuzzer", "negative-size-memcpy", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Clean Exit Liblouis Generic Table Plus Escaped Text Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[liblouis-generic-table-plus-escaped-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Standalone escaped text did not match the active generic harness, which first builds a table from
the input. After switching to minimal custom table definitions plus escaped text, long words,
Unicode escapes, null escapes, pass rules, context rules, and swap rules all exited cleanly. The
missing trigger is likely a more precise compiled table rule that makes a pass or swap replacement
length negative during translation.

## Policy
Treat `no_crash x clean_exit` on `liblouis-generic-table-plus-escaped-text` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The generic liblouis fuzzer file is split into a table-definition region and an escaped character
stream. The escaped stream is parsed by liblouis into wide characters before translation, so
arbitrary binary bytes are not the direct translated text.

## Harness Contract
The active harness writes the leading portion of the fuzz input to a temporary table file, parses
the remaining bytes with the liblouis extended character parser, and calls lou_translateString with
an output buffer derived from the parsed input length.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
