---
type: causal-policy
title: "Json With Settings Prefix Construct Target Sink Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 14 server-verified recovery for json-with-settings-prefix keyed by generic_crash x target_sink_reached."
failure_class: "generic_crash"
verifier_signal: "target_sink_reached"
candidate_family: "construct"
input_format: "json-with-settings-prefix"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-reached", "json-with-settings-prefix", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-14"]
match_keys: ["generic_crash", "target_sink_reached", "json-with-settings-prefix", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Json With Settings Prefix Construct Target Sink Reached Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[json-with-settings-prefix]]
- related harness facts: [[libfuzzer]]

## Policy
When `json-with-settings-prefix` under `libfuzzer` reaches `target_sink_reached` from `generic_crash`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[libfuzzer]]` and format contract `[[json-with-settings-prefix]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Use the fuzzer's small settings prefix to enable parser options, then provide a minimal syntactically valid JSON value. The bug is triggered after value parsing when trailing-space or extra-token scanning uses an end pointer derived from the original fuzz buffer rather than the carved JSON payload, causing the scanner to read past the heap allocation.
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
