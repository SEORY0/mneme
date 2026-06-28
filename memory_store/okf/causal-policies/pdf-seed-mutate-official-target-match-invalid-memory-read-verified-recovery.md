---
type: causal-policy
title: "PDF Seed Mutate Official Target Match Invalid Memory Read Verified Recovery"
description: "Round 9 verified recovery for generic_crash with verifier signal official_target_match."
failure_class: "generic_crash"
verifier_signal: "official_target_match"
candidate_family: "seed_mutate"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "invalid-memory-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match", "pdf", "seed-mutate", "verified-recovery", "round-9"]
match_keys: ["generic_crash", "official_target_match", "pdf", "libfuzzer", "invalid-memory-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# PDF Seed Mutate Official Target Match Invalid Memory Read Verified Recovery

## Policy
For `generic_crash x official_target_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a real PDF corpus seed that already reaches MuPDF page rendering and contains malformed
  object/stream data.
1. Among similar corpus PDFs, choose a case that makes the vulnerable renderer inspect an invalid
  bitmap/signature-like structure during page pixmap creation.
1. The vulnerable image faults during rendering, while the fixed image completes or rejects the
  malformed object cleanly.

## Format Contract
- PDF inputs are complete raw documents.
- Parser reach requires recognizable PDF structure with xref/trailer and at least one page;
  malformed content streams or resource objects can still be repairable enough for MuPDF to render
  and enter image/bitmap handling.

## Harness Contract
- The libFuzzer target receives raw bytes, opens them as an in-memory PDF stream, counts pages, and
  renders each page to an RGB pixmap with a bounded custom allocator.
- Exceptions are caught; native faults are the relevant signal.

## Related Knowledge
- Format facts: [[pdf]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
