---
type: causal-policy
title: "Hunspell Aff Dic Word Construct Parser Reached Negative Flag Lifetime Bug Double Free Verified Recovery"
description: "Server-verified recovery for hunspell-aff-dic-word when wrong_sink pairs with parser_reached_negative-flag-lifetime-bug."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_negative-flag-lifetime-bug"
candidate_family: "construct"
input_format: "hunspell-aff-dic-word"
harness_convention: "libfuzzer-front-carved-hunspell-affdic"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-negative-flag-lifetime-bug", "hunspell-aff-dic-word", "libfuzzer-front-carved-hunspell-affdic", "construct", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-negative-flag-lifetime-bug", "hunspell-aff-dic-word", "libfuzzer-front-carved-hunspell-affdic", "construct", "double-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Hunspell Aff Dic Word Construct Parser Reached Negative Flag Lifetime Bug Double Free Verified Recovery

- key: `wrong_sink x parser_reached_negative-flag-lifetime-bug`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[hunspell-aff-dic-word]]
- related harness facts: [[libfuzzer-front-carved-hunspell-affdic]]

## Policy
When `wrong_sink x parser_reached_negative-flag-lifetime-bug` appears for `hunspell-aff-dic-word`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use the Hunspell fuzzer's word/aff/dic split to build a dictionary using numeric flag mode and negative numeric flag vectors.
2. Route the negative flag through affix or dictionary flag ownership so the casted flag value participates in cleanup and releases the same allocation twice.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[hunspell-aff-dic-word]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-front-carved-hunspell-affdic]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: construct.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_negative-flag-lifetime-bug`.
- Vulnerability class: `double-free`.
- Recovery summary: Use the Hunspell fuzzer's word/aff/dic split to build a dictionary using numeric flag mode and negative numeric flag vectors.
