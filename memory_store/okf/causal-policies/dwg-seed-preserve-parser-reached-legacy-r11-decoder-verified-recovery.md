---
type: causal-policy
title: "Dwg Seed Preserve Parser Reached Legacy R11 Decoder Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached_legacy_r11_decoder."
failure_class: "generic_crash"
verifier_signal: "parser_reached_legacy_r11_decoder"
candidate_family: "seed_preserve"
input_format: "dwg"
harness_convention: "libfuzzer-raw-dwg-dxf-json-dispatcher"
vuln_class: "legacy-dwg-decoder-bounds-failure"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-legacy-r11-decoder", "seed-preserve", "dwg", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached_legacy_r11_decoder", "dwg", "libfuzzer-raw-dwg-dxf-json-dispatcher", "legacy-dwg-decoder-bounds-failure", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Dwg Seed Preserve Parser Reached Legacy R11 Decoder Verified Recovery

- key: `generic_crash x parser_reached_legacy_r11_decoder`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[dwg]]
- harnesses: [[libfuzzer-raw-dwg-dxf-json-dispatcher]]

## Failure Shape
The verifier-confirmed candidate preserved the `dwg` parser envelope under `libfuzzer-raw-dwg-dxf-json-dispatcher` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached_legacy_r11_decoder` on `dwg` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use a real legacy R11 DWG seed rather than a modern DWG or random header. The old-version header
selects the pre-R13 decoder and preserves enough table/entity structure to reach the vulnerable
legacy post-header and entity-processing path; the fixed build handles that legacy structure
cleanly.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
DWG inputs start with an ASCII version marker that selects the decoder generation. Legacy R11 files
use pre-R13 section and table metadata, including header variables, entity ranges, block ranges, and
legacy table records. Modern DWG headers route to different decoders and miss this bug class.

## Harness Contract
The fuzzer dispatches raw bytes by leading syntax: DWG version marker, JSON opening syntax, or DXF
text fallback. It appends termination where needed but does not otherwise carve the input.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
