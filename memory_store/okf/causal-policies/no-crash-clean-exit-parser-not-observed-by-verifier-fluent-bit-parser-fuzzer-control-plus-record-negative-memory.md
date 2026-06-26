---
type: causal-policy
title: "No Crash Clean Exit Parser Not Observed By Verifier Fluent Bit Parser Fuzzer Control Plus Record Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal clean_exit_parser_not_observed_by_verifier."
failure_class: "no_crash"
verifier_signal: "clean_exit_parser_not_observed_by_verifier"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-record"
harness_convention: "honggfuzz-style-file-fuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-parser-not-observed-by-verifier", "fluent-bit-parser-fuzzer-control-plus-record", "negative-memory", "round-7"]
match_keys: ["no_crash", "clean_exit_parser_not_observed_by_verifier", "fluent-bit-parser-fuzzer-control-plus-record", "honggfuzz-style-file-fuzzer", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Clean Exit Parser Not Observed By Verifier Fluent Bit Parser Fuzzer Control Plus Record Negative Memory

- key: `no_crash x clean_exit_parser_not_observed_by_verifier`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-record]]
- related harness facts: [[honggfuzz-style-file-fuzzer]]

## Failure Shape
Plain JSON did not exercise the intended path because the harness consumes a control prefix before
parser input. After adding the control prefix, JSON, malformed JSON, typed-key JSON, decoder-enabled
JSON, and logfmt variants still exited cleanly, so the remaining missing condition is likely a
specific JSON parser ownership pattern or decoder/table combination rather than basic parser
reachability.

## Policy
Treat `no_crash x clean_exit_parser_not_observed_by_verifier` on `fluent-bit-parser-fuzzer-control-plus-record` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_parser_not_observed_by_verifier`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The fuzzer can select JSON, regex, LTSV, or logfmt parsing. Optional parser settings include time
fields, type coercions for fixed key names, and decoder rules; only the bytes after those control
fields become the record text parsed by Fluent Bit.

## Harness Contract
The harness rejects short inputs. It reads selector and option bytes from the front of the file,
optionally consumes fixed-size null-terminated time fields and decoder parameters, and then calls
the parser on the remaining bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
