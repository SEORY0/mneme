---
type: causal-policy
title: "Bam Seed Mutate Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for bam when wrong_sink pairs with parser_reached_target_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_crash"
candidate_family: "seed_mutate"
input_format: "bam"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-crash", "bam", "libfuzzer", "seed-mutate", "verified-recovery", "round-17"]
match_keys: ["wrong-sink", "parser-reached-target-crash", "bam", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Bam Seed Mutate Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[bam]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached_target_crash` appears for `bam`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Start from a valid BAM seed so BGZF, header, reference, and record framing are accepted.
2. Mutate one record so the declared read-name length is a multiple of the alignment unit, preventing the reader from adding implicit NUL padding, then ensure subsequent record data contains no early terminator.
3. Force a record validation error that logs the read name with an unbounded string formatter; the fixed build rejects or terminates the name safely.
4. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[bam]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: seed_mutate.
