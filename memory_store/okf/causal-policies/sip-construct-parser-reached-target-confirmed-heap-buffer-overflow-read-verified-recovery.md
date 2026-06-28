---
type: causal-policy
title: "SIP Construct Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for sip keyed by wrong_sink x parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "construct"
input_format: "sip"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "sip", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "sip", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# SIP Construct Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[sip]]
- related harness facts: [[libfuzzer]]

## Policy
When `sip` under `libfuzzer` reaches `parser_reached_target_confirmed` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Build a syntactically valid SIP message so the message parser accepts the envelope and
   dispatches the To-header parameter parser. Put a To parameter value into quoted-string parsing
   and end the input immediately after an escape character, causing the vulnerable parser to read
   the following byte past the buffer.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- A SIP request needs a request line, headers, CRLF line endings, and an empty line terminator. The To
  header accepts address parameters after semicolons; parameter names and values are separated by an
  equals sign, and quoted parameter values use backslash escapes.

## Harness Contract
- The libFuzzer harness passes the raw buffer to the SIP message parser and then exercises selected
  parsed header/address paths. There is no leading selector byte and no FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
