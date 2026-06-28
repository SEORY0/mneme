---
type: causal-policy
title: "Ase Seed Mutate Parser Reached Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "seed_mutate"
input_format: "ase"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-official-target-match", "ase", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "parser_reached_official_target_match", "ase", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Ase Seed Mutate Parser Reached Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_official_target_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[ase]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `ase` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_official_target_match` on `ase` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Start from a valid ASE scene, switch it to the legacy parser mode, and append an old-format soft-skin section for an existing mesh. End the input inside the mesh-name token so the soft-skin parser scans past the available token data while looking for whitespace.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
ASE is a text scene format made of star-prefixed sections and brace-delimited blocks. The export version changes which parser paths are enabled. The legacy soft-skin block begins with a mesh name and then describes vertex and bone-weight records.

## Harness Contract
The Assimp harness passes raw fuzzer bytes to Importer::ReadFileFromMemory. The importer auto-detects the ASE text scene and runs normal parsing and postprocessing on the resulting scene.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
