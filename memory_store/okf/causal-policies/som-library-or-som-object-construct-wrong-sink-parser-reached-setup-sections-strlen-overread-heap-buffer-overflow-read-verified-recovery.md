---
type: causal-policy
title: "Som Library Or Som Object Construct Wrong Sink Parser Reached Setup Sections Strlen Overread Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_setup_sections_strlen_overread."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_setup_sections_strlen_overread"
candidate_family: "construct"
input_format: "som-library-or-som-object"
harness_convention: "libfuzzer-tempfile-bfd"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "som-library-or-som-object", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-setup-sections-strlen-overread", "som-library-or-som-object", "libfuzzer-tempfile-bfd", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Som Library Or Som Object Construct Wrong Sink Parser Reached Setup Sections Strlen Overread Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_setup_sections_strlen_overread` on `som-library-or-som-object` under `libfuzzer-tempfile-bfd`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Construct a normal archive whose SOM library map is sufficient for BFD's archive-format check to open the first member as an object.
2. The member is a minimal big-endian SOM relocatable object with coherent header, one space, one subspace, and a valid shared space-string table.
3. Keep the parent space name in bounds, but set the subspace name index just beyond the extra terminator appended after the loaded string table so setup_sections forms an out-of-bounds string pointer before strlen.

## Format Contract
- Input format: [[som-library-or-som-object]].
- Harness contract: [[libfuzzer-tempfile-bfd]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `som-library-or-som-object` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
The first constructed archive reached the SOM parser but used the first invalid subspace-name index, which landed on BFD's appended terminator and therefore exited cleanly. Moving the same field by the minimum additional margin reached the sanitizer read while preserving the archive and object gates.
