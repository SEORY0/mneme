---
type: causal-policy
title: "Spix Construct Parser Reached Target Sink Local Sink Mismatch Use Of Uninitialized Value Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal parser_reached_target_sink_local_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink_local_sink_mismatch"
candidate_family: "construct"
input_format: "spix"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-sink-local-sink-mismatch", "spix", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "parser-reached-target-sink-local-sink-mismatch", "spix", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Spix Construct Parser Reached Target Sink Local Sink Mismatch Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_target_sink_local_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[spix]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a valid serialized pix with a color map and raster data that passes SPIX parsing, then select a shallow indexed image shape that drives the pix4 fuzzer into the rectangle histogram path. The vulnerable build uses an uninitialized local pix pointer when the histogram helper is reached.

## Policy
For `wrong_sink x parser_reached_target_sink_local_sink_mismatch` on `spix`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `spix` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `spix` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 2 attempts.
- Scope: generator repair only.
