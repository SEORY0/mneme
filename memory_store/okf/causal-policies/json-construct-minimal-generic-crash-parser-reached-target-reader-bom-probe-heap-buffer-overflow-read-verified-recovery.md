---
type: causal-policy
title: "Json Construct Minimal Generic Crash Parser Reached Target Reader Bom Probe Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_target_reader_bom_probe."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_reader_bom_probe"
candidate_family: "construct-minimal"
input_format: "json"
harness_convention: "afl-libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct-minimal", "json", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-target-reader-bom-probe", "json", "afl-libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Json Construct Minimal Generic Crash Parser Reached Target Reader Bom Probe Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_target_reader_bom_probe` on `json` under `afl-libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Satisfy the harness entrance with its leading parser-settings word, then provide a JSON payload shorter than the reader's BOM probe.
2. The vulnerable parser checks for an optional UTF-8 BOM with a fixed-width comparison before proving that enough payload bytes remain, so the comparison reads past the heap buffer while the fixed build rejects the short-prefix invariant cleanly.

## Format Contract
- Input format: [[json]].
- Harness contract: [[afl-libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `json` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
