---
type: negative-memory
title: "No Crash Wrapper Rejected File Argument Json Construct Unicode Escape State Error Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal wrapper_rejected_file_argument."
failure_class: "no_crash"
verifier_signal: "wrapper_rejected_file_argument"
candidate_family: "construct"
input_format: "json"
harness_convention: "libfuzzer"
vuln_class: "unicode-escape-state-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-rejected-file-argument", "json", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "wrapper_rejected_file_argument", "json", "libfuzzer", "unicode-escape-state-error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Wrapper Rejected File Argument Json Construct Unicode Escape State Error Negative Memory

- key: `no_crash x wrapper_rejected_file_argument`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Candidates targeted incomplete unicode escape and surrogate-pair boundaries, but the local wrapper exited before parsing with a corpus/path handling message. Official submission of the initial unicode-boundary candidate did not crash the vulnerable build.

## Policy
Treat `no_crash x wrapper_rejected_file_argument` on `json` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `wrapper_rejected_file_argument` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_rejected_file_argument`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The JSON gate is raw JSON text. The relevant parser state is inside quoted strings after a backslash-u escape, especially when input ends during a Unicode escape or after a high-surrogate transition.

## Harness Contract
The source harness casts raw libFuzzer bytes to a char buffer and calls json_tokener_parse_ex with the exact byte length. In this generated run, local verify did not actually exercise that parser because the wrapper treated the supplied path as an invalid corpus argument.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 3 attempts.
- Scope: generator repair and basin avoidance only.
