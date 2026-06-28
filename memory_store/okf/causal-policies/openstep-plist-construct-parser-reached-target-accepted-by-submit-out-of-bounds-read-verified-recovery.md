---
type: causal-policy
title: "Openstep Plist Construct Parser Reached Target Accepted By Submit Out Of Bounds Read Verified Recovery"
description: "Round 15 server-verified recovery for openstep-plist keyed by wrong_sink x parser_reached_target_accepted_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_accepted_by_submit"
candidate_family: "construct"
input_format: "openstep-plist"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-accepted-by-submit", "openstep-plist", "libfuzzer", "construct", "out-of-bounds-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_accepted_by_submit", "openstep-plist", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Openstep Plist Construct Parser Reached Target Accepted By Submit Out Of Bounds Read Verified Recovery

- key: `wrong_sink x parser_reached_target_accepted_by_submit`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[openstep-plist]]
- related harness facts: [[libfuzzer]]

## Policy
When `openstep-plist` under `libfuzzer` reaches `parser_reached_target_accepted_by_submit` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Feed the OpenStep plist parser directly with a minimal quoted scalar and withhold the
   terminating delimiter. This satisfies the raw plist dispatch while forcing the string scanner to
   test past the bounded input; the fixed build stops the scan at the buffer end.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The OpenStep plist harness accepts raw plist text without a file wrapper. Quoted strings are parsed
  as scalar nodes, and the scanner advances until a matching delimiter or input end. No checksum or
  container length gate was needed for this path.

## Harness Contract
- The libFuzzer target passes the complete input buffer directly to the OpenStep plist parser. There
  is no mode byte, FuzzedDataProvider carving, or filename container around the supplied bytes.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
