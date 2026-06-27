---
type: causal-policy
title: "Openstep Plist Seed Mutate Local Sink Mismatch But Official Target Match Heap Use After Free Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal local_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "local_sink_mismatch_but_official_target_match"
candidate_family: "seed_mutate"
input_format: "openstep-plist"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "local-sink-mismatch-but-official-target-match", "openstep-plist", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "local_sink_mismatch_but_official_target_match", "openstep-plist", "libfuzzer", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Openstep Plist Seed Mutate Local Sink Mismatch But Official Target Match Heap Use After Free Verified Recovery

- key: `wrong_sink x local_sink_mismatch_but_official_target_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[openstep-plist]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `openstep-plist` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `local_sink_mismatch_but_official_target_match` on `openstep-plist` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use an in-repo OpenStep plist seed that exercises legacy string/list parsing and cleanup. The important property is a parser path where an allocated plist node is freed on an error or conversion branch and later cleanup observes the stale pointer. Preserving the seed's valid OpenStep structure was more effective than synthesizing a small dictionary.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
OpenStep plist input is raw text containing dictionaries, arrays, strings, comments, separators, and legacy strings-style constructs. The parser accepts complete plist text directly, and valid seeds from the OpenStep/string test corpus reach deeper cleanup paths than tiny hand-built dictionaries.

## Harness Contract
The libFuzzer target passes the entire input buffer to plist_from_openstep and then calls plist_free on the returned root node. There is no selector byte or outer file envelope.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
