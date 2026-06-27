---
type: causal-policy
title: "Tftp Request Stream Construct Parser Reached Accept Input Segv Uninitialized Hook Pointer Dereference Verified Recovery"
description: "Round 19 verified recovery for generic_crash with verifier signal parser_reached_accept_input_segv."
failure_class: "generic_crash"
verifier_signal: "parser_reached_accept_input_segv"
candidate_family: "construct"
input_format: "tftp-request-stream"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-hook-pointer-dereference"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-accept-input-segv", "tftp-request-stream", "libfuzzer", "construct", "verified-recovery", "round-19"]
match_keys: ["generic-crash", "parser-reached-accept-input-segv", "tftp-request-stream", "libfuzzer", "uninitialized-hook-pointer-dereference"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# Tftp Request Stream Construct Parser Reached Accept Input Segv Uninitialized Hook Pointer Dereference Verified Recovery

- key: `generic_crash x parser_reached_accept_input_segv`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[tftp-request-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the verifier-selected TFTP parser and provide a minimal well-formed request so the generated Request unit reaches its completion hook. That hook calls the runtime accept-input callback; in the vulnerable image the callback state appears present but is not initialized, causing a pointer dereference crash. The fixed image initializes or guards the hook state.

## Policy
For `generic_crash x parser_reached_accept_input_segv` on `tftp-request-stream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `tftp-request-stream` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `tftp-request-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
