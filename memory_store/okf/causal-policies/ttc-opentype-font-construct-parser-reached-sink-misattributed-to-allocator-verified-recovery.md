---
type: causal-policy
title: "Ttc Opentype Font Construct Parser Reached Sink Misattributed To Allocator Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_sink_misattributed_to_allocator."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_misattributed_to_allocator"
candidate_family: "construct"
input_format: "ttc-opentype-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-misattributed-to-allocator", "construct", "ttc-opentype-font", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_sink_misattributed_to_allocator", "ttc-opentype-font", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Ttc Opentype Font Construct Parser Reached Sink Misattributed To Allocator Verified Recovery

- key: `wrong_sink x parser_reached_sink_misattributed_to_allocator`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[ttc-opentype-font]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `ttc-opentype-font` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_sink_misattributed_to_allocator` on `ttc-opentype-font` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use a TrueType collection envelope with a valid collection header and a single subfont entry. Choose
the subfont offset so adding the fixed sfnt offset-table size wraps the bounds check, then let the
parser read the table-count field from outside the provided buffer.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
A TTC file starts with collection magic, version/count fields, and subfont offsets. Serenity's TTF
loader follows each subfont offset into an sfnt offset table and reads the table count after a
fixed-size header check.

## Harness Contract
The harness passes raw input bytes directly to the TTF memory loader. There is no file-name
extension, mode selector, or FuzzedDataProvider split; collection magic and subfont offset
arithmetic control the path.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
