---
type: causal-policy
title: "Ssl Ctx Api Command Stream Construct Wrong Sink Parser Reached Target Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_overread."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_overread"
candidate_family: "construct"
input_format: "ssl-ctx-api-command-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-overread", "ssl-ctx-api-command-stream", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-overread", "ssl-ctx-api-command-stream", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Ssl Ctx Api Command Stream Construct Wrong Sink Parser Reached Target Overread Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-target-overread`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ssl-ctx-api-command-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Select the SSL context API operation that forwards the remaining input directly to the sigalgs-list parser, then provide a syntactically valid signature-algorithm token stream that ends without an in-buffer string terminator. The vulnerable build scans for a terminator past the fuzzer-owned buffer, while the fixed build uses a bounded string copy before parsing.

## Policy
For `wrong-sink x parser-reached-target-overread` on `ssl-ctx-api-command-stream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `ssl-ctx-api-command-stream` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `ssl-ctx-api-command-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
