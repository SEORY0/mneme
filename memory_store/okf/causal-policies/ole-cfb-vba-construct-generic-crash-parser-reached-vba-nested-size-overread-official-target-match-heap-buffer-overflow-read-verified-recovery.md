---
type: causal-policy
title: "Ole Cfb Vba Construct Generic Crash Parser Reached Vba Nested Size Overread Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_vba_nested_size_overread_official_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_vba_nested_size_overread_official_target_match"
candidate_family: "construct"
input_format: "ole-cfb-vba"
harness_convention: "libfuzzer-scanfile"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct", "ole-cfb-vba", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-vba-nested-size-overread-official-target-match", "ole-cfb-vba", "libfuzzer-scanfile", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Ole Cfb Vba Construct Generic Crash Parser Reached Vba Nested Size Overread Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_vba_nested_size_overread_official_target_match` on `ole-cfb-vba` under `libfuzzer-scanfile`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Build a minimal OLE compound-file document whose directory tree exposes VBA-related streams, including a compressed dir stream and a module stream.
2. Encode the VBA dir stream with literal-only compression so top-level project and module records parse normally, then make a nested Unicode module-name size exceed the remaining decompressed dir data while keeping the enclosing record accepted.
3. The vulnerable parser passes that unchecked nested size into character conversion and reads past the decompressed heap buffer; the fixed build rejects the inconsistent nested record.

## Format Contract
- Input format: [[ole-cfb-vba]].
- Harness contract: [[libfuzzer-scanfile]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `ole-cfb-vba` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
