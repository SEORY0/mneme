---
type: causal-policy
title: "Raw Ipv4 Tcp Xcsl Packet Construct Wrong Sink Parser Reached Target Xcsl Stack Write Stack Buffer Overflow Write Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_target_xcsl_stack_write."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_xcsl_stack_write"
candidate_family: "construct"
input_format: "raw-ipv4-tcp-xcsl-packet"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "raw-ipv4-tcp-xcsl-packet", "stack-buffer-overflow-write", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-target-xcsl-stack-write", "raw-ipv4-tcp-xcsl-packet", "libfuzzer", "stack-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Raw Ipv4 Tcp Xcsl Packet Construct Wrong Sink Parser Reached Target Xcsl Stack Write Stack Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_target_xcsl_stack_write` on `raw-ipv4-tcp-xcsl-packet` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. The harness target is IP, so wrap the XCSL text in a minimal raw IPv4/TCP packet instead of feeding the text directly.
2. Preserve coherent IP total length and TCP data-offset fields, start the TCP payload with the XCSL heuristic marker, and make the first semicolon-separated item exactly fill the parser's fixed item buffer while one trailing byte remains.
3. The vulnerable build writes the terminator past the stack buffer at premature loop exit; the fixed build exits cleanly.

## Format Contract
- Input format: [[raw-ipv4-tcp-xcsl-packet]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `raw-ipv4-tcp-xcsl-packet` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
