---
type: causal-policy
title: "WKT Plus WKB Split Stream Construct Parser Reached Edge Noding Builder Stack Lifetime Bug Stack Use After Scope Read Verified Recovery"
description: "Round 20 verified recovery for wrong_sink with verifier signal parser_reached_edge_noding_builder_stack_lifetime_bug."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_edge_noding_builder_stack_lifetime_bug"
candidate_family: "construct"
input_format: "wkt-plus-wkb-split-stream"
harness_convention: "libfuzzer"
vuln_class: "stack-use-after-scope-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-edge-noding-builder-stack-lifetime-bug", "wkt-plus-wkb-split-stream", "libfuzzer", "construct", "verified-recovery", "round-20"]
match_keys: ["wrong-sink", "parser-reached-edge-noding-builder-stack-lifetime-bug", "wkt-plus-wkb-split-stream", "libfuzzer", "stack-use-after-scope-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# WKT Plus WKB Split Stream Construct Parser Reached Edge Noding Builder Stack Lifetime Bug Stack Use After Scope Read Verified Recovery

- key: `wrong_sink x parser_reached_edge_noding_builder_stack_lifetime_bug`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[wkt-plus-wkb-split-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a valid WKT geometry prefix and a valid WKB geometry suffix under the harness split contract so both geometries enter GEOS overlay operations. Use geometries whose overlay path invokes edge noding and clipping; the trigger is the overlay builder retaining or consulting a clipping envelope after its stack lifetime rather than a malformed WKB record.

## Policy
For `wrong_sink x parser_reached_edge_noding_builder_stack_lifetime_bug` on `wkt-plus-wkb-split-stream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `wkt-plus-wkb-split-stream` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `wkt-plus-wkb-split-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.
