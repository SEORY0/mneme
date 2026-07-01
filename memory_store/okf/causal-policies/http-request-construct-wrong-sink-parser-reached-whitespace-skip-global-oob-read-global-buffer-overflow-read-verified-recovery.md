---
type: causal-policy
title: "Http Request Construct Wrong Sink Parser Reached Whitespace Skip Global Oob Read Global Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for http-request when wrong_sink pairs with parser_reached_whitespace_skip_global_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_whitespace_skip_global_oob_read"
candidate_family: "construct"
input_format: "http-request"
harness_convention: "afl/libfuzzer raw request parser"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-whitespace-skip-global-oob-read", "http-request", "afl-libfuzzer-raw-request-parser", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-whitespace-skip-global-oob-read", "http-request", "afl-libfuzzer-raw-request-parser", "construct", "global-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Http Request Construct Wrong Sink Parser Reached Whitespace Skip Global Oob Read Global Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_whitespace_skip_global_oob_read`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[http-request]]
- related harness facts: [[afl-libfuzzer-raw-request-parser]]

## Policy
When `wrong_sink x parser_reached_whitespace_skip_global_oob_read` appears for `http-request`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `afl-libfuzzer-raw-request-parser` harness contract and the `http-request` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the raw request-parser harness contract. Build an accepted request buffer made only of leading HTTP whitespace while still satisfying the complete-header terminator gate away from the start. The finalizer accepts the buffer, then the parser skips whitespace without rechecking that a method remains, so the vulnerable build reads past the fixed internal request copy; the fixed build rejects it cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[http-request]]. The Lwan request parser expects a method, path, HTTP version, header lines, and a blank-line terminator. Its fuzz finalizer treats the terminator as evidence of a complete request unless the terminator is at the initial buffer position, while the later parser first ignores leading HTTP whitespace before method identification.

## Harness Contract
Use [[afl-libfuzzer-raw-request-parser]]. The fuzz target copies raw input bytes into a fixed internal request buffer and calls the request finalizer before parsing. There is no FuzzedDataProvider, mode byte, checksum, or outer envelope; the PoC file bytes are the request bytes.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_whitespace_skip_global_oob_read`.
- Vulnerability class: `global-buffer-overflow-read`.
- Recovery summary: Use the raw request-parser harness contract. Build an accepted request buffer made only of leading HTTP whitespace while still satisfying the complete-header terminator gate away from the start. The finalizer accepts the buffer, then the parser skips whitespace without rechecking that a method remains, so the vulnerable build reads past the fixed internal request copy; the fixed build rejects it cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
