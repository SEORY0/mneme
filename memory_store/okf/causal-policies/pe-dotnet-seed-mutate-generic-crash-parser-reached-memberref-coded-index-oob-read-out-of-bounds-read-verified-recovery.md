---
type: causal-policy
title: "Pe Dotnet Seed Mutate Generic Crash Parser Reached Memberref Coded Index Oob Read Out Of Bounds Read Verified Recovery"
description: "Server-verified recovery for pe-dotnet when generic_crash pairs with parser_reached_memberref_coded_index_oob_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_memberref_coded_index_oob_read"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-memberref-coded-index-oob-read", "pe-dotnet", "libfuzzer", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-memberref-coded-index-oob-read", "pe-dotnet", "libfuzzer", "seed-mutate", "out-of-bounds-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Pe Dotnet Seed Mutate Generic Crash Parser Reached Memberref Coded Index Oob Read Out Of Bounds Read Verified Recovery

- key: `generic_crash x parser_reached_memberref_coded_index_oob_read`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pe-dotnet]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_memberref_coded_index_oob_read` appears for `pe-dotnet`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `pe-dotnet` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Start from a valid managed PE seed so the YARA dotnet module reaches the CLR metadata table stream. Preserve the DOS/PE headers, section mapping, CLR directory, metadata root, stream headers, string heap, blob heap, TypeRef table, and initial MemberRef table. Widen the CustomAttribute coded-index layout by increasing the MemberRef table row count and pad the file so the parser's shifted CustomAttribute table remains inside the scanned buffer. Add a CustomAttribute row with an assembly parent and a MemberRef-tagged Type value whose row index is far beyond the actual MemberRef data, leaving the fixed build to reject the bounds violation.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[pe-dotnet]]. The input is a PE32 managed .NET assembly. Parser reachability requires coherent DOS and PE headers, section-to-file mapping, a CLR data-directory entry, a CLI metadata root, and stream headers for the table stream plus string, blob, GUID, and user-string heaps. The table stream declares a Valid bitmask, row counts in bit order, and compact table rows whose coded-index widths depend on related table row counts. CustomAttribute rows contain Parent, Type, and Value coded indexes; Type can reference MemberRef, whose row then references TypeRef and string/blob heaps.

## Harness Contract
Use [[libfuzzer]]. The YARA dotnet libFuzzer target compiles a fixed rule importing the dotnet module and scans the raw input bytes directly with yr_rules_scan_mem. There is no mode selector, archive wrapper, path-based parsing, checksum wrapper, or FuzzedDataProvider layout; all bytes are interpreted as the scanned PE image.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `generic_crash x parser_reached_memberref_coded_index_oob_read`.
- Vulnerability class: `out-of-bounds-read`.
- Recovery summary: Start from a valid managed PE seed so the YARA dotnet module reaches the CLR metadata table stream. Preserve the DOS/PE headers, section mapping, CLR directory, metadata root, stream headers, string heap, blob heap, TypeRef table, and initial MemberRef table. Widen the CustomAttribute coded-index layout by increasing the MemberRef table row count and pad the file so the parser's shifted CustomAttribute table remains inside the scanned buffer. Add a CustomAttribute row with an assembly parent and a MemberRef-tagged Type value whose row index is far beyond the actual MemberRef data, leaving the fixed build to reject the bounds violation.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
