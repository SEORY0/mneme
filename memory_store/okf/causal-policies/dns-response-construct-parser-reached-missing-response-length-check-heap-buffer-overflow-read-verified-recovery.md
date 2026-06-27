---
type: causal-policy
title: "DNS Response Construct Parser Reached Missing Response Length Check Heap Buffer Overflow Read Verified Recovery"
description: "Round 19 verified recovery for wrong_sink with verifier signal parser_reached_missing_response_length_check."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_missing_response_length_check"
candidate_family: "construct"
input_format: "dns-response"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-missing-response-length-check", "dns-response", "libfuzzer", "construct", "verified-recovery", "round-19"]
match_keys: ["wrong-sink", "parser-reached-missing-response-length-check", "dns-response", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# DNS Response Construct Parser Reached Missing Response Length Check Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_missing_response_length_check`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[dns-response]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use raw resolver-response bytes rather than a wrapped file. A very short or truncated DNS response reaches the resolver record parser before the vulnerable build has validated that enough header and record bytes are present; the fixed build rejects the short response cleanly.

## Policy
For `wrong_sink x parser_reached_missing_response_length_check` on `dns-response`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `dns-response` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `dns-response` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
