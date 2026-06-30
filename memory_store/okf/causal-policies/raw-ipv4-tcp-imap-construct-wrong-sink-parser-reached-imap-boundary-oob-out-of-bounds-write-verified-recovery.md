---
type: causal-policy
title: "Raw Ipv4 Tcp Imap Construct Wrong Sink Parser Reached Imap Boundary Oob Out Of Bounds Write Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_imap_boundary_oob."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_imap_boundary_oob"
candidate_family: "construct"
input_format: "raw-ipv4-tcp-imap"
harness_convention: "libfuzzer-ndpi-process-packet"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-imap-boundary-oob", "raw-ipv4-tcp-imap", "libfuzzer-ndpi-process-packet", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-imap-boundary-oob", "raw-ipv4-tcp-imap", "libfuzzer-ndpi-process-packet", "out-of-bounds-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Raw Ipv4 Tcp Imap Construct Wrong Sink Parser Reached Imap Boundary Oob Out Of Bounds Write Verified Recovery

- key: `wrong-sink x parser-reached-imap-boundary-oob`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[raw-ipv4-tcp-imap]]
- harnesses: [[libfuzzer-ndpi-process-packet]]

## Failure Shape
Build a coherent raw IPv4/TCP packet whose TCP payload is a syntactically valid tagged IMAP LOGIN command ending in the line terminator expected by the dissector. Keep the packet header lengths aligned with the payload, then make the IMAP line exactly reach the parser's fixed local copy-buffer boundary so the vulnerable terminator write lands just past that buffer while the fixed build rejects or bounds the copy.

## Policy
For `wrong-sink x parser-reached-imap-boundary-oob` on `raw-ipv4-tcp-imap`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `raw-ipv4-tcp-imap` carrier enough for the `libfuzzer-ndpi-process-packet` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `raw-ipv4-tcp-imap` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
