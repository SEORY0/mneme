---
type: causal-policy
title: "Javascript Source Construct Sink Mismatch Stack Buffer Overflow Read Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "javascript-source"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "javascript-source", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "sink_mismatch", "javascript-source", "libfuzzer", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Javascript Source Construct Sink Mismatch Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[javascript-source]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `javascript-source` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `sink_mismatch` on `javascript-source` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Feed syntactically valid JavaScript that executes and creates substantial short-lived heap pressure. Repeated allocation and reference dropping triggers LibJS garbage collection under the sanitizer, and the conservative root scan reads past a stack object while gathering roots.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The input is plain JavaScript source text. It must parse successfully and run far enough to allocate many objects or arrays so the runtime enters garbage collection.

## Harness Contract
The LibJS fuzzer treats the raw buffer as JavaScript source. It parses and executes the script directly; there is no file envelope, mode selector, or length prefix.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
