---
type: causal-policy
title: "Pac Construct Parser Reached Sink Mismatch Out Of Bounds Read Verified Recovery"
description: "Round 22 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "pac"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch", "pac", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch", "pac", "libfuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Pac Construct Parser Reached Sink Mismatch Out Of Bounds Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pac]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a PAC envelope that passes the harness size bounds and the PAC parser's initial header checks, then choose the counted-buffer relationship so descriptor allocation and descriptor iteration disagree. The vulnerable build proceeds into descriptor parsing and reads beyond the allocated metadata area; the fixed build rejects the count and length relationship before the read.

## Policy
For `wrong_sink x parser_reached_sink_mismatch` on `pac`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `pac` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pac` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 1 attempts.
- Scope: generator repair only.
