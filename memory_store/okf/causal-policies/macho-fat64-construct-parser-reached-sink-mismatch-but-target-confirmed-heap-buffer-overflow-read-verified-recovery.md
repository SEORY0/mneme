---
type: causal-policy
title: "Macho Fat64 Construct Parser Reached Sink Mismatch But Target Confirmed Heap Buffer Overflow Read Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_target_confirmed"
candidate_family: "construct"
input_format: "macho-fat64"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-target-confirmed", "macho-fat64", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-but-target-confirmed", "macho-fat64", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Macho Fat64 Construct Parser Reached Sink Mismatch But Target Confirmed Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_but_target_confirmed`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[macho-fat64]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a minimal universal 64-bit Mach-O header that passes the magic and architecture-count sanity checks, then declare enough architecture records that the parser allocates storage using the smaller record shape but later walks it as the larger record shape. The invariant violated is agreement between allocation element size and the element size used by the 64-bit architecture-copy loop.

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_target_confirmed` on `macho-fat64`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `macho-fat64` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `macho-fat64` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 7 attempts.
- Scope: generator repair only.
