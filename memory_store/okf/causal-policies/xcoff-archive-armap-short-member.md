---
type: causal-policy
title: XCOFF Archive Short Armap Recovery
description: Recover BFD XCOFF archive crashes by using a recognized archive and undersizing only the symbol-map member.
failure_class: generic_crash
verifier_signal: official_target_match
candidate_family: construct
input_format: xcoff-archive
harness_convention: fuzz-bfd
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, official_target_match, xcoff, archive, armap]
match_keys: [generic_crash, official_target_match, xcoff-archive, armap_short_member]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For BFD archive tasks, format recognition is the hard gate. Keep the XCOFF archive magic and member header coherent, then direct archive-map metadata to a symbol table member whose body is too short for the reader's minimum count and entry assumptions.

## Procedure
1. Start from an archive envelope that BFD recognizes as XCOFF.
2. Preserve member boundaries and names enough for archive enumeration.
3. Point the archive map at a deliberately undersized symbol-table member.
4. Do not corrupt the top-level archive wrapper while shrinking the symbol-table body.
5. Treat official target match as the authoritative signal when local crash detail is generic.

## Negative Memory
- Do not use a generic archive shell that never enters XCOFF armap reading.
- Do not append random members after a clean recognition miss.
- Do not make every member malformed at once; the armap member is the causal field.
