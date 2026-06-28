---
type: causal-policy
title: "ZIP Archive Construct Parser Reached Heap Use After Free Heap Use After Free Verified Recovery"
description: "Server-verified recovery for zip-archive when wrong_sink pairs with parser_reached_heap_use_after_free."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_heap_use_after_free"
candidate_family: "construct"
input_format: "zip-archive"
harness_convention: "afl-style file fuzzer for kimgio/karchive"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-heap-use-after-free", "zip-archive", "afl-style-file-fuzzer-for-kimgio-karchive", "construct", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-heap-use-after-free", "zip-archive", "afl-style-file-fuzzer-for-kimgio-karchive", "construct", "heap-use-after-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# ZIP Archive Construct Parser Reached Heap Use After Free Heap Use After Free Verified Recovery

- key: `wrong_sink x parser_reached_heap_use_after_free`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[zip-archive]]
- related harness facts: [[afl-style-file-fuzzer-for-kimgio-karchive]]

## Policy
When `wrong_sink x parser_reached_heap_use_after_free` appears for `zip-archive`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use an archive carrier parsed by KArchive.
2. Place an empty file at a nested path first, then add a later member below that same path so recovery tries to replace the earlier file with a directory.
3. The stale nested entry remains owned by its original directory while recovery also deletes it, producing a double lifetime release during directory teardown.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[zip-archive]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[afl-style-file-fuzzer-for-kimgio-karchive]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: construct.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_heap_use_after_free`.
- Vulnerability class: `heap-use-after-free`.
- Recovery summary: Use an archive carrier parsed by KArchive.
