---
type: causal-policy
title: "Sip Construct Parser Reached Sink Match Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "sip"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "construct", "sip", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "sip", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Sip Construct Parser Reached Sink Match Verified Recovery

- key: `wrong_sink x parser_reached_sink_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[sip]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `sip` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_sink_match` on `sip` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use a syntactically plausible SIP request with the To header parsed as a bare URI token, then end
the raw fuzzer buffer inside a quoted To-parameter escape. The parser reaches the To-parameter state
machine and the final escape forces it to read past the available header body while deciding the
quoted value state.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The SIP parser accepts a request line followed by colon-delimited headers. Well-known From/To
headers are parsed eagerly; To parameters begin after a semicolon and support quoted parameter
values with backslash escapes. A complete message body is not required for the To parser to run.

## Harness Contract
The libFuzzer harness passes raw bytes directly to parse_msg and then frees the parsed message.
There is no file wrapper or length prefix; truncation at the end of the raw input is visible to the
header parser.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
