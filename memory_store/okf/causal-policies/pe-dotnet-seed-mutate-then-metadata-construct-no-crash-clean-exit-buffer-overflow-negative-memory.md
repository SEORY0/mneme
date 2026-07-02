---
type: causal-policy
title: "Pe Dotnet Seed Mutate Then Metadata Construct No Crash Clean Exit Buffer Overflow Negative Memory"
description: "Negative memory for pe-dotnet candidates that ended in no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "seed_mutate_then_metadata_construct"
input_format: "pe-dotnet"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "pe-dotnet", "libfuzzer", "seed-mutate-then-metadata-construct", "buffer-overflow", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit", "pe-dotnet", "libfuzzer", "seed-mutate-then-metadata-construct", "buffer-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Pe Dotnet Seed Mutate Then Metadata Construct No Crash Clean Exit Buffer Overflow Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[pe-dotnet]]
- related harness facts: [[libfuzzer]]

## Policy
Treat `no_crash x clean_exit` for `[[pe-dotnet]]` under `[[libfuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Valid managed PE seeds reached the dotnet module cleanly, but neither corpus replay, malformed stream-name/count mutations, nor constructed custom-attribute metadata produced a sanitizer signal. The most plausible remaining gap is that the attempted custom-attribute blob relation did not map to the exact fixed-buffer sink condition in this harness, or the local input buffer shape masked the over-read style attempted.
3. Rebuild around `[[pe-dotnet]]` and `[[libfuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The format is a PE32 managed assembly. The PE data directory points to a CLI header, which points to CLR metadata beginning with the metadata magic and a version string. Metadata then declares named streams such as the table stream, string heap, blob heap, user-string heap, and GUID heap. The dotnet parser walks the table stream by the Valid bitmask and row counts; custom attributes can reference MemberRef and TypeRef rows and a blob heap value.

## Harness Contract
- The libFuzzer harness compiles a fixed YARA rule that imports the dotnet module and checks the module_name field. Each raw input is scanned as an in-memory buffer with SCAN_FLAGS_NO_TRYCATCH. The dotnet module load path finds a PE image in the raw bytes, sets the PE data pointer and size from the memory block, and calls the dotnet CLR metadata parser. There is no carved prefix, no FuzzedDataProvider, and no filename-based parsing.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 15.
