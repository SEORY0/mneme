---
type: causal-policy
title: "Miff Construct Parser Reached Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "construct"
input_format: "miff"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-official-target-match", "miff", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "parser_reached_official_target_match", "miff", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Miff Construct Parser Reached Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_official_target_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[miff]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `miff` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_official_target_match` on `miff` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use a minimal MIFF image header that selects an uncompressed direct-color pixel import path. Declare a small image requiring a full pixel row, then provide a short non-empty pixel payload so the zero-copy blob read returns less data than the row importer consumes.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
MIFF uses a text header made of key-value image attributes followed by a header terminator and then pixel data. DirectClass RGB with no compression causes rows to be imported from raw channel bytes; the needed row byte count is derived from image width, depth, and channel layout.

## Harness Contract
The GraphicsMagick coder fuzzer passes the raw input as a Magick blob to the MIFF decoder. There is no outer file carving; the header and pixel payload are exactly the fuzzer bytes.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
