---
type: "negative-memory"
title: "Javascript Construct No Crash Parser Reached No Target Typed Array Branding Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_reached_no_target."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target"
candidate_family: "construct"
input_format: "javascript"
harness_convention: "libfuzzer"
vuln_class: "typed-array-branding"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-reached-no-target", "javascript", "libfuzzer", "construct", "typed-array-branding", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_reached_no_target", "javascript", "libfuzzer", "typed-array-branding", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Javascript Construct No Crash Parser Reached No Target Typed Array Branding Negative Memory

- key: `no_crash x parser_reached_no_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[javascript]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The raw JS harness does not instantiate LibWeb objects, and the vulnerable LibJS global object does not expose Uint8ClampedArray as a constructor. Direct references therefore become ordinary JS exceptions or undefined-name behavior rather than sanitizer crashes; typed-array prototype, species, ArrayBuffer, DataView, and garbage-collection paths only exercised the existing typed arrays.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_reached_no_target` on `[[javascript]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_target` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 10 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
