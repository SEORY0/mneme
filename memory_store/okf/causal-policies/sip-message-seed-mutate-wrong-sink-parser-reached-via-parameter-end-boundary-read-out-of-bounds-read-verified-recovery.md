---
type: causal-policy
title: "Sip Message Seed Mutate Wrong Sink Parser Reached Via Parameter End Boundary Read Out Of Bounds Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_via_parameter_end_boundary_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_via_parameter_end_boundary_read"
candidate_family: "seed_mutate"
input_format: "sip-message"
harness_convention: "libfuzzer-opensips-message-parser"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-via-parameter-end-boundary-read", "sip-message", "libfuzzer-opensips-message-parser", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-via-parameter-end-boundary-read", "sip-message", "libfuzzer-opensips-message-parser", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Sip Message Seed Mutate Wrong Sink Parser Reached Via Parameter End Boundary Read Out Of Bounds Read Verified Recovery

- key: `wrong-sink x parser-reached-via-parameter-end-boundary-read`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[sip-message]]
- harnesses: [[libfuzzer-opensips-message-parser]]

## Failure Shape
Start from an in-repo valid SIP request so the generic message parser reaches Via parsing. Preserve the request line and Via transport and host syntax, then end the buffer immediately after a recognized Via parameter's value introducer so the value scanner advances into its value loop at the logical end of input. Do not add a line terminator or body after that boundary.

## Policy
For `wrong-sink x parser-reached-via-parameter-end-boundary-read` on `sip-message`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `sip-message` carrier enough for the `libfuzzer-opensips-message-parser` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `sip-message` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
