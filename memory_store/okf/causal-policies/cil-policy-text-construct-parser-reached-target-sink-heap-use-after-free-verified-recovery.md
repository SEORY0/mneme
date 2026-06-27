---
type: causal-policy
title: "Cil Policy Text Construct Parser Reached Target Sink Heap Use After Free Verified Recovery"
description: "Server-verified recovery for cil-policy-text when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 2
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "cil-policy-text", "libfuzzer", "construct", "verified-recovery", "round-17"]
match_keys: ["generic-crash", "parser-reached-target-sink", "cil-policy-text", "libfuzzer", "construct", "heap-use-after-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Cil Policy Text Construct Parser Reached Target Sink Heap Use After Free Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[cil-policy-text]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_target_sink` appears for `cil-policy-text`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Build a minimal valid CIL policy that declares a class outside an optional block.
2. Inside the optional block, declare a common permission set and associate it to the outer class, then include an unresolved statement so the optional subtree is discarded.
3. Later class reset logic still follows the stale class-common relationship and reads freed common-permission state; the fixed build clears or guards that relationship.
4. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[cil-policy-text]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_target_sink`.
- Vulnerability class: `heap-use-after-free`.
- Recovery summary: Use a syntactically valid CIL policy scaffold with an optional block that contains both a resolvable blockinherit and an unresolved blockinherit.
