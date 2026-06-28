---
type: causal-policy
title: "Json Construct Parser Reached Target Function Heap Buffer Overflow Read Verified Recovery"
description: "Round 14 server-verified recovery for json keyed by wrong_sink x parser_reached_target_function."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_function"
candidate_family: "construct"
input_format: "json"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-function", "json", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-14"]
match_keys: ["wrong_sink", "parser_reached_target_function", "json", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Json Construct Parser Reached Target Function Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_function`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[json]]
- related harness facts: [[libfuzzer]]

## Policy
When `json` under `libfuzzer` reaches `parser_reached_target_function` from `wrong_sink`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[libfuzzer]]` and format contract `[[json]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Use a minimal object/string envelope that reaches the JSON string lexer, then terminate the input immediately after an escape introducer so the lexer advances as if an escaped character exists and reads beyond the supplied buffer.
3. Keep mutations focused on the gate relation: declared size versus available data, selector versus subparser, structure count versus actual records, lifetime ownership, or sink-specific state.
4. If local labels report `wrong_sink` while the same parser branch is reached, submit once to check the official target match before discarding the candidate.
5. If the fixed image also fails, shrink back to the smallest boundary relation and avoid broad randomization.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not promote this as a byte recipe; it is a format-gate and sink-invariant relation.

## Evidence Shape
- Support: one server-verified Round 14 solve.
- Candidate family: construct.
