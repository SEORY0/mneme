---
type: causal-policy
title: "YARA Dotnet CustomAttribute Type Index Unbounded MemberRef Out Of Bounds Read Verified Recovery"
description: "Verified recovery for no_crash where the .NET CustomAttribute Type index follows an unbounded MemberRef pointer into a wild address."
failure_class: "no_crash"
verifier_signal: "parser_reached_unbounded_table_index_wild_pointer"
candidate_family: "seed_mutate"
input_format: "dotnet-pe"
harness_convention: "yara-module-scan-mem"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "seed-mutate", "dotnet-pe", "out-of-bounds-read", "table-index", "verified-recovery"]
match_keys: ["no_crash", "parser_reached_unbounded_table_index_wild_pointer", "dotnet-pe", "yara-module-scan-mem", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# YARA Dotnet CustomAttribute Type Index Unbounded MemberRef Out Of Bounds Read Verified Recovery

## Policy
For `no_crash` on the YARA `dotnet` module fuzzer, the bug is a wild-pointer OOB read in
`dotnet_parse_tilde_2`: CustomAttribute-table parsing follows an attacker-controlled Type index into the
MemberRef table (`memberref_ptr + memberref_row_size * type_index`) with no `fits_in_pe` bounds check, so a
large index produces a multi-GB wild pointer that is dereferenced (SEGV). The fix adds a `fits_in_pe` break.

## Procedure
1. Seed from a minimal valid .NET PE (e.g. a hello-world managed binary in the corpus) so the dotnet module
   is selected and the metadata `#~` stream is parsed (reach proven at baseline).
2. Inflate the MemberRef table row count so the CustomAttribute Type column widens to 4 bytes; extend the
   data size with padding so the emulated table offsets stay in-bounds for the prefix.
3. Write a crafted CustomAttribute row whose Parent tag selects a valid owner and whose Type index is huge
   (a large coded index) so the computed MemberRef pointer is far out of the mapped image.
4. Minimum-margin: keep the PE/CLI headers and earlier tables valid; only the row count + the one oversized
   Type index differ. Confirm the fix exits 0 (bounds check rejects the index).

## Format Contract
- See [[dotnet-pe]]. Coded indices into metadata tables must be range-checked before pointer arithmetic;
  the harness scans raw bytes via the module, so a valid CLI/metadata prefix is required to reach the table.

## Negative Memory
- Do not break the PE/CLI/metadata prefix (module not selected / bad_format).
- Do not store raw bytes, offsets, table addresses, commit ids, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
