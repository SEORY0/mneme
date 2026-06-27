---
type: causal-policy
title: "No Crash Parser Reached No Target Crash IPP Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "ipp"
harness_convention: "libfuzzer"
vuln_class: "logic-bug-error-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "ipp", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "ipp", "libfuzzer", "logic-bug-error-handling", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached No Target Crash IPP Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ipp]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Minimal IPP requests with repeated attributes and incompatible continuation value tags parsed and
  wrote back without producing the target failure. The remaining likely path is a conversion where
  ippSetValueTag fails internally for an existing attribute but ippReadIO continues instead of rolling
  back; the simple tag-mismatch cases either converted successfully or were accepted as compatible.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `ipp` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- IPP messages start with a version, operation/status, request id, then group tags and attributes.
  Each attribute has a value tag, big-endian name length and name, big-endian value length, and value
  bytes. A repeated value for the current attribute is encoded with an empty name, allowing setOf
  values and type-conversion logic to run.

## Harness Contract
- The fuzz target reads the raw input as an IPP file using ippReadIO, then resets the request state
  and writes it to a null output using ippWriteIO. There is no front selector or FuzzedDataProvider
  layout; the complete file must be a syntactically plausible IPP message.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
