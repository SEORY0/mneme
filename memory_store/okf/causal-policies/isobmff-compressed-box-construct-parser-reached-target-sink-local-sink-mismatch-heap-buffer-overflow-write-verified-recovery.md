---
type: causal-policy
title: "Isobmff Compressed Box Construct Parser Reached Target Sink Local Sink Mismatch Heap Buffer Overflow Write Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal parser_reached_target_sink_local_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink_local_sink_mismatch"
candidate_family: "construct"
input_format: "isobmff-compressed-box"
harness_convention: "afl-libfuzzer-file"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-sink-local-sink-mismatch", "isobmff-compressed-box", "afl-libfuzzer-file", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "parser-reached-target-sink-local-sink-mismatch", "isobmff-compressed-box", "afl-libfuzzer-file", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Isobmff Compressed Box Construct Parser Reached Target Sink Local Sink Mismatch Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_target_sink_local_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[isobmff-compressed-box]]
- harnesses: [[afl-libfuzzer-file]]

## Failure Shape
Build an ISO BMFF root replacement box that selects GPAC's compressed-box parsing path. The compressed payload must inflate to exactly the initial decompression buffer size so the vulnerable decompressor writes its trailing terminator one byte past the allocation before later box validation matters.

## Policy
For `wrong_sink x parser_reached_target_sink_local_sink_mismatch` on `isobmff-compressed-box`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `isobmff-compressed-box` carrier enough for the `afl-libfuzzer-file` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `isobmff-compressed-box` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 1 attempts.
- Scope: generator repair only.
