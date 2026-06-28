---
type: causal-policy
title: "Ssh Server Byte Stream Construct Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 22 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "ssh-server-byte-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached", "ssh-server-byte-stream", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["wrong-sink", "parser-reached", "ssh-server-byte-stream", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Ssh Server Byte Stream Construct Parser Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ssh-server-byte-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Model the input as the server side of an SSH handshake. Send a valid server identification line, a framed KEXINIT whose algorithm lists force an ECDH NIST curve exchange with a compatible signing host key and ordinary transport methods, then send an ECDH reply whose host-key string length exceeds the remaining packet payload. The vulnerable ECDH reply parser copies the advertised host-key length before checking that the packet actually contains it.

## Policy
For `wrong_sink x parser_reached` on `ssh-server-byte-stream`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `ssh-server-byte-stream` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ssh-server-byte-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 1 attempts.
- Scope: generator repair only.
