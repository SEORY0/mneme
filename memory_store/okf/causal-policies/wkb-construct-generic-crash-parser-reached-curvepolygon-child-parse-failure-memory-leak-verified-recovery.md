---
type: causal-policy
title: "Wkb Construct Generic Crash Parser Reached Curvepolygon Child Parse Failure Memory Leak Verified Recovery"
description: "Round 34 verified recovery for wkb when generic_crash pairs with parser_reached_curvepolygon_child_parse_failure."
failure_class: "generic_crash"
verifier_signal: "parser_reached_curvepolygon_child_parse_failure"
candidate_family: "construct"
input_format: "wkb"
harness_convention: "libfuzzer"
vuln_class: "memory-leak"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-curvepolygon-child-parse-failure", "wkb", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-curvepolygon-child-parse-failure", "wkb", "libfuzzer", "construct", "memory-leak", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Wkb Construct Generic Crash Parser Reached Curvepolygon Child Parse Failure Memory Leak Verified Recovery

- key: `generic_crash x parser_reached_curvepolygon_child_parse_failure`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[wkb]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_curvepolygon_child_parse_failure`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `memory-leak`
- related format facts: [[wkb]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x parser_reached_curvepolygon_child_parse_failure` appears for `wkb`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[wkb]] format contract before changing sink fields.
2. Recreate the verified causal relation: Build a raw WKB CurvePolygon that first contains a structurally valid curve ring so the CurvePolygon object owns allocated ring state, then declare another contained geometry and make that child incomplete at the point where its point array would be read. This reaches the CurvePolygon parser state and exercises the cleanup difference: the vulnerable build aborts while the fixed build handles the malformed child without leaking/crashing.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
WKB records are endian-tagged and type-tagged. A CurvePolygon record carries a contained-geometry count, then each ring is itself a nested WKB geometry. Valid ring members are lines, circular strings, or compound curves; counts and point arrays must stay coherent until the target nested child relation is reached.

### Harness Contract
The libFuzzer target passes the raw file bytes directly to the PostGIS WKB importer with no selector byte, no FuzzedDataProvider carving, and no outer file container. Normal parser errors are caught by the harness, so a useful input must reach the specific parser state before violating the narrow child-geometry invariant.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `generic_crash x parser_reached_curvepolygon_child_parse_failure`.
- Vulnerability class: `memory-leak`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
