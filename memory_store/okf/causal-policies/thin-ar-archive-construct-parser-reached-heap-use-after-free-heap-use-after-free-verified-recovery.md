---
type: causal-policy
title: "Thin Ar Archive Construct Parser Reached Heap Use After Free Heap Use After Free Verified Recovery"
description: "Server-verified recovery for thin-ar-archive when wrong_sink pairs with parser_reached_heap_use_after_free."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_heap_use_after_free"
candidate_family: "construct"
input_format: "thin-ar-archive"
harness_convention: "libfuzzer-tempfile-readelf"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-heap-use-after-free", "thin-ar-archive", "libfuzzer-tempfile-readelf", "construct", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-heap-use-after-free", "thin-ar-archive", "libfuzzer-tempfile-readelf", "construct", "heap-use-after-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Thin Ar Archive Construct Parser Reached Heap Use After Free Heap Use After Free Verified Recovery

- key: `wrong_sink x parser_reached_heap_use_after_free`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[thin-ar-archive]]
- related harness facts: [[libfuzzer-tempfile-readelf]]

## Policy
When `wrong_sink x parser_reached_heap_use_after_free` appears for `thin-ar-archive`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Construct a thin archive whose long-name and nested-member metadata makes readelf set up a cached nested archive, then take the error path for another nested member.
2. The error path releases the cached archive fields without clearing them; subsequent qualified-name construction observes the stale file-name pointer.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[thin-ar-archive]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-tempfile-readelf]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: construct.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_heap_use_after_free`.
- Vulnerability class: `heap-use-after-free`.
- Recovery summary: Construct a thin archive whose long-name and nested-member metadata makes readelf set up a cached nested archive, then take the error path for another nested member.
