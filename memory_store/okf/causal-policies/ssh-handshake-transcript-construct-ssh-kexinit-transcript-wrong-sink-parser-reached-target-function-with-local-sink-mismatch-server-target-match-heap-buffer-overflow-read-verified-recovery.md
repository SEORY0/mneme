---
type: causal-policy
title: "Ssh Handshake Transcript Construct Ssh Kexinit Transcript Wrong Sink Parser Reached Target Function With Local Sink Mismatch Server Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_function_with_local_sink_mismatch_server_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_function_with_local_sink_mismatch_server_target_match"
candidate_family: "construct_ssh_kexinit_transcript"
input_format: "ssh-handshake-transcript"
harness_convention: "aflplusplus-libfuzzer-compat"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-function-with-local-sink-mismatch-server-target-match", "ssh-handshake-transcript", "aflplusplus-libfuzzer-compat", "construct-ssh-kexinit-transcript", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-function-with-local-sink-mismatch-server-target-match", "ssh-handshake-transcript", "aflplusplus-libfuzzer-compat", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Ssh Handshake Transcript Construct Ssh Kexinit Transcript Wrong Sink Parser Reached Target Function With Local Sink Mismatch Server Target Match Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-target-function-with-local-sink-mismatch-server-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ssh-handshake-transcript]]
- harnesses: [[aflplusplus-libfuzzer-compat]]

## Failure Shape
Feed the client harness a server banner followed by one plaintext SSH binary packet whose payload is a server KEXINIT. The packet only needs to satisfy the early KEXINIT scanner: message type, cookie, and a first name-list. Make that KEX name-list long enough to pass the strict-KEX search precheck, include one comma, and end with a non-matching method fragment so the stale comma-search length scans past the end of the allocated payload. Suppressing SSH packet padding keeps the logical name-list end aligned with the allocation boundary, so the vulnerable read is visible to ASan while the fixed build rejects it cleanly.

## Policy
For `wrong-sink x parser-reached-target-function-with-local-sink-mismatch-server-target-match` on `ssh-handshake-transcript`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct-ssh-kexinit-transcript` while this format and harness contract are present.

## Procedure
1. Preserve the `ssh-handshake-transcript` carrier enough for the `aflplusplus-libfuzzer-compat` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `ssh-handshake-transcript` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
