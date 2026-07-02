---
type: causal-policy
title: "Perfetto Trace Protobuf Construct Wrong Sink Sink Mismatch Stack Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "perfetto-trace-protobuf"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "perfetto-trace-protobuf", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "sink_mismatch", "perfetto-trace-protobuf", "libfuzzer", "stack-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Perfetto Trace Protobuf Construct Wrong Sink Sink Mismatch Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[perfetto-trace-protobuf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a minimal Perfetto Trace protobuf that reaches memory tracker snapshot import. Include allocator dump nodes and an ownership edge where one endpoint maps to the implicit process-root allocator name rather than to a graph row emitted in the node table. EOF finalization then emits graph edges and dereferences a missing node-table entry in the vulnerable processor path. The fixed build guards or skips the missing endpoint.

## Policy
When `wrong_sink x sink_mismatch` appears for `perfetto-trace-protobuf` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[perfetto-trace-protobuf]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `perfetto-trace-protobuf` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 6 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
