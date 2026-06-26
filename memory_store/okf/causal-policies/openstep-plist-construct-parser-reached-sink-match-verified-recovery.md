---
type: causal-policy
title: "Openstep Plist Construct Parser Reached Sink Match Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "openstep-plist"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "construct", "openstep-plist", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "openstep-plist", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Openstep Plist Construct Parser Reached Sink Match Verified Recovery

- key: `wrong_sink x parser_reached_sink_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[openstep-plist]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `openstep-plist` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_sink_match` on `openstep-plist` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Feed a minimal OpenStep plist node that starts a quoted string but never provides the closing quote.
The quoted-string scanner reaches the end of the supplied buffer, then the parser checks the current
character as if a closing delimiter were still available.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
OpenStep plist accepts dictionaries, arrays, data groups, quoted strings, and unquoted atoms. Quoted
strings use either quote delimiter and support backslash escapes; the parser scans until an
unescaped matching delimiter before constructing a string node.

## Harness Contract
The libFuzzer harness passes the raw byte buffer and its exact size to plist_from_openstep, then
frees any resulting root node. The input is not NUL-terminated by the harness.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
