---
type: causal-policy
title: "Postscript Eps Construct Wrong Sink Parser Reached Failed Dos Eps Header Read Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_failed_dos_eps_header_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_failed_dos_eps_header_read"
candidate_family: "construct"
input_format: "postscript-eps"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "postscript-eps", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-failed-dos-eps-header-read", "postscript-eps", "libfuzzer", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Postscript Eps Construct Wrong Sink Parser Reached Failed Dos Eps Header Read Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_failed_dos_eps_header_read` on `postscript-eps` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a minimal DOS EPS carrier that satisfies only the special EPS wrapper recognizer, then ends before the fixed-width wrapper header fields are fully read.
2. The vulnerable parser trusts the partially read header state and later line-scanning logic observes uninitialized stack data; the fixed build rejects or initializes that failed-read path cleanly.

## Format Contract
- Input format: [[postscript-eps]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `postscript-eps` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
