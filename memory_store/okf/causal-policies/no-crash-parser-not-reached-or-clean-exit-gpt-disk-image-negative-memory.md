---
type: causal-policy
title: "No Crash Parser Not Reached Or Clean Exit Gpt Disk Image Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_not_reached_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_clean_exit"
candidate_family: "construct"
input_format: "gpt-disk-image"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-clean-exit", "gpt-disk-image", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_not_reached_or_clean_exit", "gpt-disk-image", "libfuzzer", "integer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Not Reached Or Clean Exit Gpt Disk Image Negative Memory

- key: `no_crash x parser_not_reached_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpt-disk-image]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Constructed disk-image variants satisfied the protective-partition idea and varied the selected
  sector position to exercise multiplication wraparound, but the local libFuzzer path often exited
  before treating the mounted file as raw bytes and the official submissions exited cleanly.

## Policy
Treat `no_crash x parser_not_reached_or_clean_exit` on `gpt-disk-image` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The libmagic GPT recognizer first uses an MBR-style protective partition record to select a
  candidate GPT sector, then probes for a GPT header at a sector-size-scaled position.
- A useful trigger must preserve the MBR exclusion gates and protective-entry uniqueness before
  violating the sector-position arithmetic invariant.

## Harness Contract
- The wrapper invokes a libFuzzer target through the image entrypoint with the submitted path.
- In this environment the target may interpret the mounted file path as a corpus input argument
  instead of always consuming raw bytes.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
