---
type: causal-policy
title: "MVG Construct No Crash MVG Parser Reached Clean Exit Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for mvg candidates that ended in no_crash with verifier signal mvg_parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "mvg_parser_reached_clean_exit"
candidate_family: "construct"
input_format: "mvg"
harness_convention: "afl-file-mvg-coder"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mvg-parser-reached-clean-exit", "mvg", "afl-file-mvg-coder", "construct", "heap-buffer-overflow-read", "negative-memory", "round-32"]
match_keys: ["no-crash", "mvg-parser-reached-clean-exit", "mvg", "afl-file-mvg-coder", "construct", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# MVG Construct No Crash MVG Parser Reached Clean Exit Heap Buffer Overflow Read Negative Memory

- key: `no_crash x mvg_parser_reached_clean_exit`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[mvg]]
- related harness facts: [[afl-file-mvg-coder]]

## Policy
Treat `no_crash x mvg_parser_reached_clean_exit` for `[[mvg]]` under `[[afl-file-mvg-coder]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Constructed MVG inputs reached the MVG coder and dash renderer but exited cleanly. Exact dash-period offsets landed the dash index past the logical terminator, but the first stale dash slot did not stay positive long enough to walk to a sanitizer-visible allocation boundary. Heap grooming with prior dash arrays, alternate line/polyline/polygon primitives, tiny dash intervals, long segments, and a same-size positive double-array prime did not change the clean-exit signal.
3. Rebuild around `[[mvg]]` and `[[afl-file-mvg-coder]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- MVG is line-oriented drawing text. A recognized input begins with a viewbox/canvas declaration, then drawing-state directives such as stroke, fill, stroke-width, stroke-dasharray, and stroke-dashoffset precede primitives such as line, polyline, polygon, path, and bezier. The dash parser accepts numeric lists, duplicates odd-length dash arrays internally, and appends a zero terminator; DrawDashPolygon advances through the dash pattern while splitting stroked segments.

## Harness Contract
- The GraphicsMagick MVG coder fuzzer feeds the entire file as raw bytes to the MVG image reader. There is no leading selector, archive wrapper, checksum, or FuzzedDataProvider split. The accepted MVG text is rendered by the coder_MVG_fuzzer binary in a file/stdin style harness.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 11.
