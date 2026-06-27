---
type: causal-policy
title: "Json Construct Parser Reached Target Accepted By Submit Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for json keyed by wrong_sink x parser_reached_target_accepted_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_accepted_by_submit"
candidate_family: "construct"
input_format: "json"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-accepted-by-submit", "json", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_accepted_by_submit", "json", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Json Construct Parser Reached Target Accepted By Submit Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_accepted_by_submit`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[json]]
- related harness facts: [[libfuzzer]]

## Policy
When `json` under `libfuzzer` reaches `parser_reached_target_accepted_by_submit` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use a top-level JSON primitive that reaches the numeric fraction path rather than object or
   keyword handling. The primitive is syntactically valid enough for tokenization, then the
   fractional scan dereferences the cursor before confirming that it is still inside the token. The
   fixed build performs the bounds check first.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The JSON plist parser accepts raw JSON text. Primitive numbers, booleans, and null are handled by a
  shared primitive parser, but the numeric floating path has a distinct scan over the fractional
  portion. A top-level primitive is sufficient; no enclosing object or array is required.

## Harness Contract
- The libFuzzer target forwards the entire input buffer to the JSON plist parser. There is no leading
  selector, length prefix, FuzzedDataProvider split, or external file envelope.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
