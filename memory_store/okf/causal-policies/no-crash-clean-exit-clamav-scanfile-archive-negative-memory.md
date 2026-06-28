---
type: causal-policy
title: "No Crash Clean Exit Clamav Scanfile Archive Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "clamav-scanfile-archive"
harness_convention: "libfuzzer"
vuln_class: "null-dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "clamav-scanfile-archive", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "clamav-scanfile-archive", "libfuzzer", "null-dereference", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit Clamav Scanfile Archive Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[clamav-scanfile-archive]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Archive and text-envelope candidates were consumed by the scanfile fuzzer and exited cleanly.
- They did not reach the EGG UTF-8 conversion state where a malformed encoded name is decoded
  through the vulnerable null path.

## Policy
Treat `no_crash x clean_exit` on `clamav-scanfile-archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The scanner fuzzer writes the input bytes to a temporary file and enables broad ClamAV parsing
  options.
- The target bug is in EGG archive name/string conversion, so the input must be recognized as an
  archive member format that routes a name through the UTF-8 conversion helper.

## Harness Contract
- The submitted file is passed to a libFuzzer-style single-input runner; the runner reads the file,
  writes those bytes to a temporary scan path, and calls cl_scanfile with archive and heuristic
  scanning enabled.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
