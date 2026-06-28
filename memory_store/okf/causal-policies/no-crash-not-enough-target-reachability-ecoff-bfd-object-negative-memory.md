---
type: causal-policy
title: "No Crash Not Enough Target Reachability Ecoff BFD Object Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal not_enough_target_reachability."
failure_class: "no_crash"
verifier_signal: "not_enough_target_reachability"
candidate_family: "source_inspection"
input_format: "ecoff-bfd-object"
harness_convention: "libfuzzer-binutils-bfd"
vuln_class: "buffer-overrun-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "not-enough-target-reachability", "ecoff-bfd-object", "negative-memory", "round-15"]
match_keys: ["no_crash", "not_enough_target_reachability", "ecoff-bfd-object", "libfuzzer-binutils-bfd", "buffer-overrun-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Not Enough Target Reachability Ecoff BFD Object Negative Memory

- key: `no_crash x not_enough_target_reachability`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ecoff-bfd-object]]
- related harness facts: [[libfuzzer-binutils-bfd]]

## Failure Shape
- The source and harness point to a BFD object-file parser path, but no compact ECOFF object seed was
  identified in the extracted tree during this worker pass. The remaining path is to construct or
  locate a real ECOFF object with a valid file header, optional header, section table, and symbolic-
  header area, then mutate symbolic offsets whose counts are zero or whose ranges extend beyond the
  file.

## Policy
Treat `no_crash x not_enough_target_reachability` on `ecoff-bfd-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- ECOFF is a COFF-family object format with target-specific magic, file and optional headers, section
  headers, and an ECOFF symbolic header used for debug tables. The vulnerable logic is in the
  symbolic-info reader, where offsets and counts for debug sub-tables must either be ignored when
  count is zero or bounded against the object size when count is nonzero.

## Harness Contract
- The binutils task builds several libFuzzer targets over BFD-style object consumers. The relevant
  path writes the raw input as an object file and asks BFD/nm-style code to recognize and inspect it;
  there is no archive wrapper, text envelope, checksum, or FuzzedDataProvider contract.

## Negative Memory
- Do not resubmit variants that only reproduce `not_enough_target_reachability`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
