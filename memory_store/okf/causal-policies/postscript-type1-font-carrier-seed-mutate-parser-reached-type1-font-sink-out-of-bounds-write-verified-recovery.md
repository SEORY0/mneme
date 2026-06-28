---
type: causal-policy
title: "Postscript Type1 Font Carrier Seed Mutate Parser Reached Type1 Font Sink Out Of Bounds Write Verified Recovery"
description: "Server-verified recovery for postscript-type1-font-carrier when generic_crash pairs with parser_reached_type1_font_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_type1_font_sink"
candidate_family: "seed_mutate"
input_format: "postscript-type1-font-carrier"
harness_convention: "libfuzzer-gstoraster-stdin"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-type1-font-sink", "postscript-type1-font-carrier", "libfuzzer-gstoraster-stdin", "seed-mutate", "verified-recovery", "round-18"]
match_keys: ["generic-crash", "parser-reached-type1-font-sink", "postscript-type1-font-carrier", "libfuzzer-gstoraster-stdin", "seed-mutate", "out-of-bounds-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Postscript Type1 Font Carrier Seed Mutate Parser Reached Type1 Font Sink Out Of Bounds Write Verified Recovery

- key: `generic_crash x parser_reached_type1_font_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[postscript-type1-font-carrier]]
- related harness facts: [[libfuzzer-gstoraster-stdin]]

## Policy
When `generic_crash x parser_reached_type1_font_sink` appears for `postscript-type1-font-carrier`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Feed Ghostscript a document that reaches FreeType Type 1 font parsing with a custom Encoding array.
2. Include an encoding entry whose numeric character code passes the digit parser but becomes invalid when narrowed, so the parser writes outside the encoding table.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[postscript-type1-font-carrier]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-gstoraster-stdin]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: seed_mutate.

## Round 18 Verified Evidence
- Verifier key: `generic_crash x parser_reached_type1_font_sink`.
- Vulnerability class: `out-of-bounds-write`.
- Recovery summary: Feed Ghostscript a document that reaches FreeType Type 1 font parsing with a custom Encoding array.
