---
type: causal-policy
title: "Tga Construct No Crash Clean Exit After Tga Short Read And Large Raw Read Hypotheses Readrawdata Failure Handling Negative Memory"
description: "Negative memory for tga candidates that ended in no_crash with verifier signal clean_exit_after_tga_short_read_and_large_raw_read_hypotheses."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_tga_short_read_and_large_raw_read_hypotheses"
candidate_family: "construct"
input_format: "tga"
harness_convention: "afl-style-raw-kimageformats-multi-handler-fuzzer"
vuln_class: "readRawData-failure-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-after-tga-short-read-and-large-raw-read-hypotheses", "tga", "afl-style-raw-kimageformats-multi-handler-fuzzer", "construct", "readrawdata-failure-handling", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit-after-tga-short-read-and-large-raw-read-hypotheses", "tga", "afl-style-raw-kimageformats-multi-handler-fuzzer", "construct", "readrawdata-failure-handling", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Tga Construct No Crash Clean Exit After Tga Short Read And Large Raw Read Hypotheses Readrawdata Failure Handling Negative Memory

- key: `no_crash x clean_exit_after_tga_short_read_and_large_raw_read_hypotheses`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[tga]]
- related harness facts: [[afl-style-raw-kimageformats-multi-handler-fuzzer]]

## Policy
Treat `no_crash x clean_exit_after_tga_short_read_and_large_raw_read_hypotheses` for `[[tga]]` under `[[afl-style-raw-kimageformats-multi-handler-fuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Distinct TGA hypotheses stayed clean: short RLE run pixels, short RLE raw packets, truncated indexed palette/RLE data, failed image-ID seek, oversized raw image read lengths, and official submissions of the strongest short-read and oversized-read families. Short reads appear to return byte counts rather than read errors in this QBuffer harness, and oversized raw-image candidates did not reach the vulnerable read path before clean exit.
3. Rebuild around `[[tga]]` and `[[afl-style-raw-kimageformats-multi-handler-fuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- TGA inputs use a fixed little-endian header with image type, optional color-map descriptor, dimensions, pixel depth, descriptor flags, optional image ID, optional palette, and then raw or RLE pixel data. The handler supports raw and RLE indexed, true-color, and greyscale images after checking color-map rules, nonzero dimensions, and supported pixel depths. RLE packets use a packet header to select run or raw packet form and derive a pixel count.

## Harness Contract
- The kimageformats fuzzer feeds the same raw byte buffer through several QImageIOHandler implementations using QBuffer, including TGA. There is no filename extension, outer container, mode byte, checksum, or FuzzedDataProvider split; TGA reachability depends entirely on the bytes passing the TGA handler support checks inside the shared raw buffer.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 10.
