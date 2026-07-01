---
type: causal-policy
title: "Pe Dotnet Seed Mutate Generic Crash Parser Reached Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for pe-dotnet when generic_crash pairs with parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer-yara-dotnet-scan-mem"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "pe-dotnet", "libfuzzer-yara-dotnet-scan-mem", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-target-match", "pe-dotnet", "libfuzzer-yara-dotnet-scan-mem", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Pe Dotnet Seed Mutate Generic Crash Parser Reached Target Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pe-dotnet]]
- related harness facts: [[libfuzzer-yara-dotnet-scan-mem]]

## Policy
When `generic_crash x parser_reached_target_match` appears for `pe-dotnet`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-yara-dotnet-scan-mem` harness contract and the `pe-dotnet` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Start from a valid managed PE seed so the YARA dotnet module accepts the PE and CLR metadata streams. Preserve the outer PE and metadata stream headers, widen the metadata coded-index width by increasing the relevant table row count, then make a CustomAttribute Type coded index select MemberRef with an out-of-range row. The vulnerable parser follows that unchecked relation during CustomAttribute parsing and reads past the metadata table area; the fixed build rejects the out-of-range relation.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[pe-dotnet]]. The input is a PE32 managed assembly. The PE data directory points to a CLI header, which points to CLR metadata beginning with the metadata magic and a padded version string. Metadata stream headers name streams such as the table stream, string heap, user-string heap, GUID heap, and blob heap. The dotnet parser walks the table stream in Valid-bit order, derives coded-index widths from table row counts, records TypeRef and MemberRef table bases, and parses CustomAttribute rows whose Parent and Type fields are coded indexes.

## Harness Contract
Use [[libfuzzer-yara-dotnet-scan-mem]]. The libFuzzer harness compiles a fixed YARA rule importing the dotnet module and scans the raw input bytes directly with yr_rules_scan_mem. There is no filename contract, mode byte, checksum wrapper, or FuzzedDataProvider split; every byte in the PoC is the scanned in-memory PE image.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `generic_crash x parser_reached_target_match`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Start from a valid managed PE seed so the YARA dotnet module accepts the PE and CLR metadata streams. Preserve the outer PE and metadata stream headers, widen the metadata coded-index width by increasing the relevant table row count, then make a CustomAttribute Type coded index select MemberRef with an out-of-range row. The vulnerable parser follows that unchecked relation during CustomAttribute parsing and reads past the metadata table area; the fixed build rejects the out-of-range relation.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
