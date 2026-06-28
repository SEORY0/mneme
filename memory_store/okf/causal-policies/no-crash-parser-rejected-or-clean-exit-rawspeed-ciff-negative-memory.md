---
type: causal-policy
title: "No Crash Parser Rejected Or Clean Exit Rawspeed Ciff Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_rejected_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_rejected_or_clean_exit"
candidate_family: "construct"
input_format: "rawspeed-ciff"
harness_convention: "libfuzzer"
vuln_class: "overlapping-range-parse"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-rejected-or-clean-exit", "rawspeed-ciff", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_rejected_or_clean_exit", "rawspeed-ciff", "libfuzzer", "overlapping-range-parse", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Rejected Or Clean Exit Rawspeed Ciff Negative Memory

- key: `no_crash x parser_rejected_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-ciff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Minimal CIFF-shaped inputs with nested and overlapping sub-IFD descriptors did not reach the
  vulnerable recursive parse in the active binary. The verifier output showed the Threefr TIFF decoder
  fuzzer, so the CIFF parser may require a different dispatch path or a wrapper that causes this
  harness to select CIFF parsing.

## Policy
Treat `no_crash x parser_rejected_or_clean_exit` on `rawspeed-ciff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- CIFF parsing uses little-endian raw data. After a short header, the parser builds a root IFD from a
  substream. Each IFD stores value data before a directory area; directory entries can refer to inline
  data or offsets into the value area, and CIFF sub-IFD entry types recurse into child IFDs.

## Harness Contract
- The active executable reported by the verifier is a RawSpeed Threefr TIFF decoder fuzzer that
  consumes the raw file bytes. It does not use a FuzzedDataProvider layout. CIFF-shaped bytes alone
  were not enough to make the active target exercise the CIFF parser path.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_rejected_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
